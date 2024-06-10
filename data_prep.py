# %%
import geopandas as gpd
from shapely.geometry import box

# Load the GeoJSON file with geopandas
gdf = gpd.read_file(
    r"/mnt/bigdrive/Dropbox/Presentations/YouthMappers_Thailand_2024/South_Africa/labels.geojson"
)

# %%

# Get the bounding box
bbox = gdf.total_bounds

# Create a GeoDataFrame with the bounding box
bbox_gdf = gpd.GeoDataFrame({"geometry": [box(*bbox)]}, crs=gdf.crs)

# Reproject to WGS84 (EPSG:4326)
bbox_gdf = bbox_gdf.to_crs(epsg=4326)

# Save the bounding box as a shapefile
output_path = "/mnt/bigdrive/Dropbox/Presentations/YouthMappers_Thailand_2024/South_Africa//bbox_shapefile.shp"
bbox_gdf.to_file(output_path)

output_path

# %%


a = gpd.read_file(
    r"/mnt/bigdrive/Dropbox/Tanzania_data/Projects/YM_Tanzania_Field_Boundaries/kobo_field_collections/combined_data_reviewed_xy_LC_RPN_Final.shp"
)
a.to_crs(epsg=4326).to_file(
    r"/mnt/bigdrive/Dropbox/Presentations/YouthMappers_Thailand_2024/Tanzania/field_boundaries.geojson",
    driver="GeoJSON",
)

# %% clip images to bounding box
from glob import glob
import geowombat as gw
import geopandas as gpd
import os
from rasterio.coords import BoundingBox

bbox = gpd.read_file(
    r"/home/mmann1123/Dropbox/Presentations/YouthMappers_Thailand_2024/South_Africa/bbox_shapefile.shp"
).to_crs(epsg=32634)

# Create a BoundingBox object
bounding_box = BoundingBox(*bbox.total_bounds)

images = glob(
    r"/home/mmann1123/Downloads/download/LC08_L2SP_174084_20171003_20200903_02_T1/LC08_L2SP_174084_20171003_20200903_02_T1_SR_B*.TIF"
)
images
for image in images:

    with gw.config.update(ref_bounds=bounding_box):
        with gw.open(image) as src:
            display(src)
            src.gw.save(
                os.path.join(
                    "/home/mmann1123/Dropbox/Presentations/YouthMappers_Thailand_2024",
                    os.path.basename(image).replace(".TIF", ".tif"),
                )
            )
# %% clean field names of tz data
import geopandas as gpd

points = gpd.read_file(
    r"/mnt/bigdrive/Dropbox/Presentations/YouthMappers_Thailand_2024/Tanzania/tz_labels.geojson"
)
points.columns
# %%
points = points[
    [
        "Picture_of",
        "primar",
        "Secondary_",
        "Field_size",
        "geometry",
    ]
]
points.rename(
    {
        "Picture_of": "pic_url",
        "primar": "primary_crop",
        "Secondary_": "secondary_crop",
        "Field_size": "field_size",
    },
    axis=1,
    inplace=True,
)
points
# %%
points.to_file(
    r"/mnt/bigdrive/Dropbox/Presentations/YouthMappers_Thailand_2024/Tanzania/tz_labels.geojson",
    driver="GeoJSON",
)
# %%  Tanzania

import geopandas as gpd

bbox = gpd.read_file(
    "/home/mmann1123/Dropbox/Presentations/YouthMappers_Thailand_2024/Tanzania/bbox.gpkg",
)
bbox.explore()

# %%
import pandas as pd

a = gpd.read_file(
    "/home/mmann1123/Dropbox/Tanzania_data/Projects/YM_Tanzania_Field_Boundaries/kobo_field_collections/combined_data_reviewed_xy_LC_RPN_Final.shp"
)[["primar", "geometry"]]
a.columns = ["lc_name", "geometry"]
b = gpd.read_file(
    "/home/mmann1123/Dropbox/Tanzania_data/Projects/YM_Tanzania_Field_Boundaries/kobo_field_collections/other_training.gpkg"
)[["lc_name", "geometry"]]
b.columns = ["lc_name", "geometry"]
c = gpd.read_file(
    "/home/mmann1123/Dropbox/Tanzania_data/Projects/YM_Tanzania_Field_Boundaries/kobo_field_collections/exported_classified_points.geojson"
)[["landCover", "geometry"]]
c.columns = ["lc_name", "geometry"]

lc = pd.concat([a, b, c])
lc

# %%
set(lc.lc_name)
# %%

keep = [
    "rice",
    "maize",
    "cassava",
    "sunflower",
    "sorghum",
    "urban",
    "forest",
    "shrub",
    "tidal",
    "cotton",
    "water",
    "fallow_barren",
    "forest_shrubland",
    "millet",
    "large_building",
    "water_body",
]
drop = [
    "Don't know",
    "Other (later, specify in optional notes)",
    "could be maize.",
    "no",
    "don_t_know",
]

# apply keep/drop
lc.drop(lc[lc["lc_name"].isin(drop)].index, inplace=True)
lc.loc[lc["lc_name"].isin(keep) == False, "lc_name"] = "Other"
lc.reset_index(drop=True, inplace=True)

lc.replace(
    {"water_body": "water", "large_building": "urban", "Other": "other"}, inplace=True
)
set(lc.lc_name)
# %%

lc = lc.clip(bbox)
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder
lc["lc_code"] = le().fit_transform(lc.lc_name)
lc.explore()
# %%
lc.to_file(
    "/home/mmann1123/Dropbox/Presentations/YouthMappers_Thailand_2024/Tanzania/lc_classes.geojson",
    driver="GeoJSON",
)

# %%
