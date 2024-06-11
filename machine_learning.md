
# Machine Learning - Examples

## Country Cuisine Classifier
In this example, we will create a dataset with regional variations in food and climate. The dataset will have the following columns:
- Country
- Region
- Staple Food
- Preferred Cuisine
- Climate

The dataset will have the following regional variations:
- North, South, Central
 
Copy and paste the following in the QGIS python console to create the dataset called `data`:

``` python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.cluster import KMeans
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
    x="Staple Food",
    x2="Climate",
):
    ax = plt.gca()

    # create a dictionary to map the classifier to the model
    classifier_dict = {
        "KMeans": KMeans(4),
        "RandomForestClassifier": RandomForestClassifier(),
        "GaussianNB": GaussianNB(),
        "LogisticRegression": LogisticRegression(
            multi_class="multinomial", solver="lbfgs", max_iter=200
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
    y = le_y.fit_transform(data["Country"])

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
    print(f"Accuracy: {model.score(X, y)}")

    ax.set(xlim=xlim, ylim=ylim)
    plt.show()

```

We will use the `Staple Food` and `Climate` columns as features and the `Country` column as the target variable. We will use a decision tree classifier to fit the model and plot the results.

There are 5 classifiers available:
- 'KMeans'
- 'RandomForestClassifier'
- 'GaussianNB'
- 'LogisticRegression'

``` python
# Visualize the classifier
visualize_classifier(
    data, 
    classifier="LogisticRegression", 
    x="Staple Food", 
    x2="Climate"
)
```

The function will plot the data points and the decision boundaries of the classifier. The accuracy of the model will be printed in the console.