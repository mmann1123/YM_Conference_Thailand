 # Machine Learning - Supervised Examples

## Country Cuisine Classifier
As in the last example we will use the following variables:
- Country
- Region
- Staple Food
- Preferred Cuisine
- Climate

However this time we will use supervised classfication methods to classify the data.

Copy and paste the following in the QGIS Python console to create the dataset called `data`:

``` python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.cluster import KMeans,MeanShift
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import pandas as pd

# Sample data with regional variations
data = {
    "Country": [
        "Japan",
        "Japan",
        "Japan",
        "Mexico",
        "Mexico",
        "Mexico",
        "India",
        "India",
        "India",
        "USA",
        "USA",
        "USA",
    ],
    "Region": [
        "North Japan",
        "South Japan",
        "Central Japan",
        "North Mexico",
        "South Mexico",
        "Central Mexico",
        "North India",
        "South India",
        "Central India",
        "North USA",
        "South USA",
        "Central USA",
    ],
    "Staple Food": [
        "Rice",
        "Rice",
        "Rice",
        "Corn",
        "Corn",
        "Corn",
        "Wheat",
        "Wheat",
        "Rice",  # regional variation within India
        "Wheat",
        "Corn",
        "Wheat",  # regional variation within USA
    ],
    "Preferred Cuisine": [
        "Sushi",
        "Ramen",
        "Tempura",
        "Tacos",
        "Enchiladas",
        "Tamales",
        "Curry",
        "Dosa",
        "Biryani",
        "Burgers",
        "BBQ",
        "Pizza",
    ],
    "Climate": [
        "Temperate",
        "Subtropical",
        "Temperate",
        "Tropical",
        "Tropical",
        "Arid",
        "Tropical",
        "Subtropical",
        "Tropical",
        "Temperate",
        "Arid",
        "Temperate",
    ],
}
data = pd.DataFrame(data)
print(data)
```

Example data:

|--|Country|Region|Staple Food|Preferred Cuisine|Climate|
|--|-------|------|-----------|-----------------|-------|
|0|Japan|North Japan|Rice|Sushi|Temperate|
|1|Japan|South Japan|Rice|Ramen|Subtropical|
|2|Japan|Central Japan|Rice|Tempura|Temperate|
|...|...|...|...|...|...|

Here we are defining a function that can visualize our classification model in a 2D space. This function will take the data, the `x` and `x2` columns to use as features, and the target variable. It will encode the categorical data, fit the model, and plot the results.

``` python

def visualize_classifier(
    data,
    classifier="DecisionTreeClassifier",
    cmap="rainbow",
    y="Country",
    x="Staple Food",
    x2="Climate",
):
    ax = plt.gca()

    # create a dictionary to map the classifier to the model
    classifier_dict = {
        "KMeans": KMeans(4, random_state=0),
        "MeanShift": MeanShift(),
        "RandomForestClassifier": RandomForestClassifier(
            random_state=0, n_estimators=100
        ),
        "DecisionTreeClassifier": DecisionTreeClassifier(random_state=0),
        "GaussianNB": GaussianNB(),
        "LogisticRegression": LogisticRegression(
            multi_class="multinomial", solver="lbfgs", max_iter=200, random_state=0
        ),
    }

    # Check if classifier is valid
    if classifier not in classifier_dict.keys():
        raise ValueError(
            f"{classifier} is not a valid classifier, please choose one of {classifier_dict.keys()}"
        )

    # throw error if x and x2 are not columns in data
    if x not in data.columns:
        raise ValueError(
            f"{x} is not a column in the data, please choose one of {data.columns}"
        )

    # Encode the categorical data
    le_x = LabelEncoder()
    le_x2 = LabelEncoder()
    le_y = LabelEncoder()

    X = le_x.fit_transform(data[x])
    X2 = le_x2.fit_transform(data[x2])
    y = le_y.fit_transform(data[y])

    # Combine features
    X = np.c_[X, X2]

    # Create and fit the model
    model = classifier_dict[classifier]
    model.fit(X, y)

    # Add jitter to avoid overlapping
    jitter_strength = 0.2
    X_jittered = X + jitter_strength * np.random.randn(*X.shape)

    # Plot the training points
    scatter = ax.scatter(
        X_jittered[:, 0],
        X_jittered[:, 1],
        c=y,
        s=30,
        cmap=cmap,
        clim=(y.min(), y.max()),
        zorder=3,
    )
    for i, txt in enumerate(le_y.inverse_transform(y)):
        ax.annotate(txt, (X_jittered[i, 0], X_jittered[i, 1]), fontsize=9, ha="right")

    ax.axis("tight")
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    # Fit the estimator
    xx, yy = np.meshgrid(np.linspace(*xlim, num=200), np.linspace(*ylim, num=200))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

    # Create a color plot with the results
    n_classes = len(np.unique(y))
    contours = ax.contourf(
        xx, yy, Z, alpha=0.3, levels=np.arange(n_classes + 1) - 0.5, cmap=cmap, zorder=1
    )

    # Label the contour lines
    contour_lines = ax.contour(xx, yy, Z, colors="k", linewidths=0.5)

    # Add x and y axis labels
    ax.set_xlabel(x)
    ax.set_ylabel(x2)

    # print accuracy
    try:
        print(f"Accuracy: {model.score(X, y)}")
    except:
        pass

    ax.set(xlim=xlim, ylim=ylim)
    plt.show()
```

We will use the `Staple Food` and `Climate` columns as features and the `Country` column as the target variable. We will use a decision tree classifier to fit the model and plot the results.

There are 4 supervised classifiers available:
- 'RandomForestClassifier'
- 'GaussianNB'
- 'LogisticRegression'
- 'DecisionTreeClassifier'

Try using different supervised classifiers to see how they perform with the given data.

``` python
visualize_classifier(
    data, 
    classifier="RandomForestClassifier", 
    x="Preferred Cuisine", 
    x2="Climate"
)
```

> Try using different classifiers and features to see how they perform with the given data.


## Wine Data Classifier

In this section, we will use the wine dataset from scikit-learn to find the ideal classifier and best two features for classification. The wine dataset is a classic dataset for classification and contains chemical analysis of wines grown in the same region in Italy.

First, we need to load the wine dataset:

```python
from sklearn.datasets import load_wine
import pandas as pd

# Load Wine dataset
wine = load_wine()
wine_data = pd.DataFrame(wine.data, columns=wine.feature_names)
wine_data['target'] = wine.target
print(wine_data.head())
```

The dataset contains 13 features:

- alcohol
- malic_acid
- ash
- alcalinity_of_ash
- magnesium
- total_phenols
- flavanoids
- nonflavanoid_phenols
- proanthocyanins
- color_intensity
- hue
- od280/od315_of_diluted_wines
- proline
 
Now let's use the `alcohol` and `malic_acid` columns as features and the `y` column as the target variable. We will use different classifiers to see which one performs best.

First, let's try using the `DecisionTreeClassifier`:

```python
# Visualize the classifier with DecisionTreeClassifier
visualize_classifier(
    wine_data,
    classifier="DecisionTreeClassifier",
    y="target",
    x="alcohol",
    x2="malic_acid",
)
```

Next, let's try using the `LogisticRegression` :

```python
# Visualize the classifier with LogisticRegression
visualize_classifier(
    wine_data,
    classifier="LogisticRegression",
    y="target",
    x="alcohol",
    x2="malic_acid"
)
```
and so on...

You can try other combinations of features and classifiers to find the best model and features for the wine dataset. For example, you can use `color_intensity` and `hue` as features and the `GaussianNB` classifier:

```python
# Visualize the classifier with GaussianNB and different features
visualize_classifier(
    wine_data,
    classifier="GaussianNB",
    y="target",
    x="color_intensity",
    x2="hue"
)
```

This tutorial allows students to explore different classifiers and feature combinations to find the best model for classifying the wine dataset.

