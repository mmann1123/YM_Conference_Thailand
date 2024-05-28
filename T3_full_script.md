
#### Tuturial 3: Full Script
The following is the full script that you can run in the QGIS Python console to read a GeoJSON file, calculate the total area of polygons in acres, and print the results.

```python
from qgis.core import *
import qgis.utils

 # Path to the sa_labels.geojson file
layer_path = r"/path/to/sa_labels.geojson"  # Change this to the actual file path

# Load the layer into QGIS
sa_labels_layer = iface.addVectorLayer(layer_path, "SA Labels", "ogr")
if not sa_labels_layer:
    print("Failed to load the layer.")
else:
    print("Layer loaded successfully.")


# Assuming 'sa_labels_layer' is the layer you've loaded
crs = sa_labels_layer.crs()

# Print the CRS description
print(f"Unit name: {crs.description()}")

# Print the Proj4 string with linear unit
print(f"Proj4 description: {crs.toProj()}")


# Initialize a variable to hold the total area in square meters
total_area_sqm = 0

# Iterate through each feature in the layer
for feature in sa_labels_layer.getFeatures():
    # Get the geometry of the feature
    geom = feature.geometry()
    
    # Add the area of the geometry to the total area
    total_area_sqm += geom.area()

# Convert square meters to acres (1 square meter = 0.000247105 acres)
total_area_acres = total_area_sqm * 0.000247105

# Print the total area in acres
print(f"Total area of crops: {total_area_acres:.2f} acres")
```
