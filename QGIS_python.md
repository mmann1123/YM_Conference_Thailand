# Introduction to Python in QGIS

Welcome to our tutorial on using Python with QGIS! QGIS is a powerful open-source geographic information system (GIS) that supports various GIS operations and spatial data management. One of the fantastic features of QGIS is its built-in Python console, which allows you to enhance your GIS projects with programming.

QGIS brings a Python API (see [PyQGIS Developer Cookbook](https://docs.qgis.org/latest/en/docs/pyqgis_developer_cookbook/) for some code samples) to let the user 
 interact with its objects (layers, features, or interface). QGIS also has a Python console.


## Accessing the Python Console in QGIS

To get started with Python in QGIS, you first need to access the Python console. Here’s how you can do it:

1. **Open QGIS**: Start by launching the QGIS application on your computer.
2. **Open the Python Console**: Look for a button on the toolbar that resembles a Python logo or go to the menu bar and select `Plugins` -> `Python Console`. This will open a small scripting window at the bottom or side of your QGIS workspace.

The Python console in QGIS is split into two main parts:
- **The command line**: This is where you can type single lines of Python code and execute them immediately.
- **The editor**: Here, you can write more complex scripts, save them, and run them as needed.

This dual setup allows you to quickly test small pieces of code and develop more extensive scripts for automating tasks.

## QGIS Python Console

The console is a Python interpreter that allows you to execute Python commands. Modules from QGIS (analysis, core, gui, server, processing, 3d) and Qt (QtCore, QtGui, QtNetwork, QtWidgets, QtXml) as well as Python's math, os, re, and sys modules are already imported and can be used directly.

The interactive console is composed of a toolbar, an input area, and an output area.
![The Python Console](https://github.com/qgis/QGIS-Documentation/blob/master/docs/user_manual/plugins/img/python_console.png?raw=true)


### Toolbar

The toolbar proposes the following tools:
- Clear Console ![clearConsole](https://github.com/qgis/QGIS-Documentation/blob/master//static/common/iconClearConsole.png?raw=true) to wipe the output area;

- Run Command ![start](https://github.com/qgis/QGIS-Documentation/blob/master//static/common/mActionStart.png?raw=true) available in the input area: same as pressing Enter;

- Show Editor ![showEditorConsole](https://github.com/qgis/QGIS-Documentation/blob/master//static/common/iconShowEditorConsole.png?raw=true): toggles console editor visibility;

- Options... ![options](https://github.com/qgis/QGIS-Documentation/blob/master//static/common/mActionOptions.png?raw=true): opens a dialog to configure console properties;

- Help... ![helpContents](https://github.com/qgis/QGIS-Documentation/blob/master//static/common/mActionHelpContents.png?raw=true) provides a menu to access various documentation:
  - [Python Console Help](https://docs.qgis.org/latest/en/docs/user_manual/plugins/python_console.html)
  - [PyQGIS API documentation](https://qgis.org/api/)
  - [PyQGIS Cookbook](https://docs.qgis.org/latest/en/docs/pyqgis_developer_cookbook/)

Dock Code Editor ![dock](https://github.com/qgis/QGIS-Documentation/blob/master//static/common/dock.png?raw=true) to dock or undock the panel in QGIS interface.


#### Why Use Python in QGIS?
Using Python in QGIS allows you to automate repetitive tasks, manipulate spatial data in ways that are cumbersome or impossible with the GUI alone, and extend the functionality of QGIS through custom scripts and plugins.

Throughout this tutorial, we will explore simple Python commands and scripts that you can execute in the Python console to interact with QGIS and perform basic GIS operations. These activities are designed to be fun and engaging, providing you with a hands-on introduction to programming within a GIS environment.

Let’s get started with some basic commands to familiarize you with the Python console in QGIS!

---

## Introduction to Python Modules

In Python, a module is a file containing Python code that defines functions, classes, or variables, which can be accessed and utilized in other Python scripts. 

Python has a vast standard library of modules that you can use for various tasks, from mathematical operations to handling internet data. Additionally, third-party modules can be installed and used in your projects, greatly extending Python's capabilities.

### Importing Modules in Python

To use a module in Python, you need to import it into your script using the `import` statement. Once a module is imported, you can call its functions or access its classes and variables using the dot notation.

For example, to import the Python `math` module, you would write:

```python
import math
```

Now you can use functions within the `math` module:

```python
result = math.sqrt(25)  # Computes the square root of 25
print(result)
```

Paste these lines into the Python console in QGIS to see the output and press ![start](https://github.com/qgis/QGIS-Documentation/blob/master//static/common/mActionStart.png?raw=true)

### Using Python with QGIS

QGIS extends Python’s capabilities by providing a specialized module called `qgis`. This module allows you to interact with the QGIS application, manipulating geographical data and automating tasks.

To start scripting with Python in QGIS, you'll first need to import the necessary modules provided by QGIS. These typically include:

- `qgis.core`: Provides core functionality like managing and manipulating vector and raster layers.
- `qgis.utils`: Contains utility functions for interacting with the QGIS interface.
- `iface`: A special variable from the `qgis.utils` module representing the QGIS interface, allowing you to interact with the application itself, like opening and displaying layers.

Here’s how to import these modules into your QGIS Python script:

```python
from qgis.core import *
import qgis.utils
```

With these imports, you’re now ready to use the QGIS Python API to enhance your GIS projects with automated scripts and customized functionality!

---

## Tutorial: Working with Crop Types in QGIS Python

In this part of our tutorial, we'll learn how to read a GeoJSON file that contains various crop types, subset the data for rice crops, and then write the results to a new file. We will also explore a variant where you'll learn to write the results to a Shapefile instead by reading the QGIS API documentation.

### Step 1: Reading the GeoJSON File

First, we need to load our GeoJSON file into QGIS. We'll use the `iface` object, which is a part of the QGIS Python API that represents the main interface of QGIS.

```python
from qgis.core import *
import qgis.utils

# Path to the GeoJSON file
file_path = 'path_to_your_file/tz_labels.geojson'

# Load the layer in 
rice_layer = iface.addVectorLayer(file_path,   # path to the file
                                 baseName= "Rice Crops",  # name of the layer in QGIS
                                 providerKey="ogr") # how to read it
if not rice_layer:
    print("Layer failed to load!")
else:
    print("Layer loaded successfully!")
```

Paste these lines into the Python console in QGIS to see the output and press ![start](https://github.com/qgis/QGIS-Documentation/blob/master//static/common/mActionStart.png?raw=true)

You should now see `Rice Crops` in your QGIS Layers Panel. This layer contains the crop types data from the GeoJSON file.

![Crop ](images/rice_crops.png)

From this point on we will be refering this layer by the name `rice_layer` in our code.

<br>

>  *Where do I find the path to my file?*  

In order to load a file into python you will need to find the 'path' to the `tz_labels.geojson` file.  Start by `Layer` > `Add Layer` > `Add Vector Layer`. Then in your layers list `right-click` on `tz_labels` and select `Properties`.  In the `General` tab you will find the `Layer Source` which is the path to your file.  Copy and paste this path into the `file_path` variable in the code above.


![Layer Properties](https://github.com/mmann1123/YM_Conference_Thailand/blob/main/images/layer_path.png?raw=true)
*Make sure your path doesn't include ``'file://'`` at the beginning.*


### Step 2: Subsetting the Data for Maize Crops

Next, we'll filter out the rice crops from our dataset. We'll assume that the crop types are stored in a field named `crop_type`.

```python
# Select features where the crop type is 'Rice'
rice_layer.selectByExpression("\"primary_crop\" = 'maize'")
# Print the number of selected rows
print(f"Number of selected rows: {rice_layer.selectedFeatureCount()}")
```

Paste these lines into the Python console in QGIS to see the output and press ![start](https://github.com/qgis/QGIS-Documentation/blob/master//static/common/mActionStart.png?raw=true)

> **Note:**
For more on how to create expressions in Qgis see [Select Expressions](https://mmann1123.github.io/YM_Conference_Thailand/select_expressions.html)


### Step 3: Writing the Subset to a New GeoJSON File

After subsetting the data, let's write the selected features to a new GeoJSON file.

```python
# Define the output file path
output_path = 'path_to_output/rice_subset.geojson'

# Write the selected features to a new GeoJSON
error = QgsVectorFileWriter.writeAsVectorFormat(layer = rice_layer, 
                    fileName = output_path, # path and name of the output file
                    fileEncoding = "UTF-8", # encoding of the output file
                    destCRS = rice_layer.crs(),  # projection of the output file
                    driverName ="GeoJSON", # output file format
                    onlySelected=True) # write only selected features

if error[0] == QgsVectorFileWriter.NoError:
    print("Success: GeoJSON file has been created.")
else:
    print("Error: Failed to write GeoJSON.")
```

Your `output_path` should be a new file in the same directory as the original file. You can now load this new file into QGIS to see the subset of rice crops.

---

#### Challenge A: Import your file

Now that you've created a new GeoJSON file with the subset of rice crops, try loading it into QGIS and exploring the data using `output_path` and `iface.addVectorLayer()`

#### Challenge B: Writing to a Shapefile

If you want to write the output to a Shapefile instead, you'll need to consult the QGIS API documentation to learn about the parameters required for writing a Shapefile. Here's how you might start:

1. Open the QGIS Python API documentation: [QGIS Cook Book](https://docs.qgis.org/3.34/en/docs/pyqgis_developer_cookbook/vector.html#creating-vector-layers)
2. Search for `QgsVectorFileWriter` and read about the different parameters you can use, especially how to specify the output format for a Shapefile.

Here’s a hint on how you might adjust the code for writing a Shapefile:

```python
# Define the output file path for the Shapefile
output_path_shp = 'path_to_output/rice_subset.shp'

error = QgsVectorFileWriter.writeAsVectorFormat(layer = rice_layer, 
                    fileName = output_path_shp, # path and name of the output file
                    fileEncoding = "UTF-8", # encoding of the output file
                    destCRS = rice_layer.crs(),  # projection of the output file
                    driverName = __________________, # output file format
                    onlySelected=True) # write only selected features

if error_shp[0] == QgsVectorFileWriter.NoError:
    print("Success: Shapefile has been created.")
else:
    print("Error: Failed to write Shapefile.")

```

### Recap 

In this tutorial, we learned how to use Python in QGIS to read a GeoJSON file, subset the data for rice crops, and write the results to a new file. We also explored how to write the output to a Shapefile by consulting the QGIS API documentation.

---
