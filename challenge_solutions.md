# Challenge Solutions

## Challenge A: Import your file

``` python
# Path to the GeoJSON file
file_path =  output_path

# Load the layer in
rice_layer = iface.addVectorLayer(file_path,   # path to the file
                                 baseName= "Rice Crops",  # name of the layer in QGIS
                                 providerKey="ogr") # how to read it
if not rice_layer:
    print("Layer failed to load!")
else:
    print("Layer loaded successfully!")
```

## Challenge B: Writing to a Shapefile

```python

# Define the output file path for the Shapefile
output_path_shp = 'path_to_output/rice_subset.shp'

error = QgsVectorFileWriter.writeAsVectorFormat(layer = rice_layer, 
                    fileName = output_path_shp, 
                    fileEncoding = "UTF-8", 
                    destCRS = rice_layer.crs(),  
                    driverName = "ESRI Shapefile",  
                     output file format
                    onlySelected=True) 

if error_shp[0] == QgsVectorFileWriter.NoError:
    print("Success: Shapefile has been created.")
else:
    print("Error: Failed to write Shapefile.")
```


## Challenge C: Count observations by field size

```python
 
# Path to the GeoJSON file
file_path = '/mnt/bigdrive/Dropbox/Presentations/YouthMappers_Thailand_2024/Tanzania/tz_labels.geojson'

# Load the layer
rice_layer = iface.addVectorLayer(file_path, 
                                 baseName= "Rice Crops", 
                                 providerKey="ogr")
iface.addVectorLayer
if not rice_layer:
    print("Layer failed to load!")
else:
    print("Layer loaded successfully!")
# Initialize a dictionary to hold the count of each crop type
crop_counts = {}

# Access the features (rows) in the layer
for feature in rice_layer.getFeatures():
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

## Challenge D: Calculate the total area of each crop type

```python
layer_path = "/mnt/bigdrive/Dropbox/Presentations/YouthMappers_Thailand_2024/South_Africa/sa_labels.geojson"  # Change this to the actual file path

# Load the layer into QGIS
sa_labels_layer = iface.addVectorLayer(layer_path, "SA Labels", "ogr")

# Initialize a dictionary to hold the total area for each crop type
area_by_crop = {}

# Iterate through each feature in the layer
for feature in sa_labels_layer.getFeatures():
    crop_type = feature['crop_name']  # Adjust the field name if different
    area_sqm = feature.geometry().area()  # Area in the CRS's units (e.g., square meters)

    # Convert the area to acres
    area_acres = area_sqm * 0.000247105

    # Update the area_by_crop dictionary for the crop type
    if crop_type in area_by_crop:
        area_by_crop[crop_type] += area_acres
    else:
        area_by_crop[crop_type] = area_acres

# Print the total area for each crop type
for crop, area in area_by_crop.items():
    print(f"{crop}: {area:.2f} acres")
```