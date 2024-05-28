
#### Tutorial 1: Full Script
The following is the full script that you can run in the QGIS Python console to read a GeoJSON file, subset the data for rice crops, and write the results to a new file.

```python
from qgis.core import *
import qgis.utils

# Path to the GeoJSON file
file_path = r'path_to_your_file/tz_labels.geojson'

# Load the layer in
all_crops = iface.addVectorLayer(file_path,   # path to the file
                                 baseName= "Rice Crops",  # name of the layer in QGIS
                                 providerKey="ogr") # how to read it
if not all_crops:
    print("Layer failed to load!")
else:
    print("Layer loaded successfully!")

# Select features where the crop type is 'Rice'
all_crops.selectByExpression("\"primary_crop\" = 'maize'")
# Print the number of selected rows
print(f"Number of selected rows: {all_crops.selectedFeatureCount()}")


# Define the output file path
output_path = r'path_to_output/rice_subset.geojson'

# Write the selected features to a new GeoJSON
error = QgsVectorFileWriter.writeAsVectorFormat(layer = all_crops, 
                    fileName = output_path, # path and name of the output file
                    fileEncoding = "UTF-8", # encoding of the output file
                    destCRS = all_crops.crs(),  # projection of the output file
                    driverName ="GeoJSON", # output file format
                    onlySelected=True) # write only selected features

if error[0] == QgsVectorFileWriter.NoError:
    print("Success: GeoJSON file has been created.")
else:
    print("Error: Failed to write GeoJSON.")
```

