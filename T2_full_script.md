
#### Full Script
The following is the full script that you can run in the QGIS Python console to read a GeoJSON file, count the number of observations for each crop type, and print the results.

```python
from qgis.core import *
import qgis.utils
 
# Load the tz_labels.geojson file
layer_path = r"/path/to/tz_labels.geojson"  # Update this path to your file's location
tz_labels_layer = iface.addVectorLayer(layer_path, "TZ Labels", "ogr")
if not tz_labels_layer:
    print("Failed to load the layer.")
else:
    print("Layer loaded successfully.")

# Suppose we have a layer loaded as tz_labels_layer and it contains a field 'primary_crop'

# Initialize a dictionary to hold the count of each crop type
crop_counts = {}

# Access the features (rows) in the layer
for feature in tz_labels_layer.getFeatures():
    # Get the value of the 'primary_crop' field
    crop_type = feature['primary_crop']
    
    # Use the dictionary counting method
    if crop_type in crop_counts:
        crop_counts[crop_type] += 1
    else:
        crop_counts[crop_type] = 1

# Print the counts for each crop type
for crop, count in crop_counts.items():
    print(f"{crop}: {count}")

```
