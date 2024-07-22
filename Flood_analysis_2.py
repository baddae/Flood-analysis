"""
Name: Bright Addae
Date: 2023-6-24
Purpose: To determine the number of reported street flooding incidents that occurred within 10 meters
of a sewer catch basin in November 2023.
"""
# Import necessary libraries
import arcpy

# Define input shapefiles
sewer_catch_basin = r"G:\Bright\City_of_Vancouver\sewer-catch-basins.shp"
service_requests = r"G:\Bright\City_of_Vancouver\Street_flooding.shp"

# Create feature layers for the input shapefiles
arcpy.MakeFeatureLayer_management(sewer_catch_basin, "sewer_catch_basin_layer")
arcpy.MakeFeatureLayer_management(service_requests, "service_requests_layer")

# Define the date range for November 2023. Would be used to filter the service requests layer
date_query = "Service__1 > '2023-11-01 00:00:00' And Service__1 < '2023-12-01 00:00:00'"

# Apply the date filter to the service requests layer
arcpy.SelectLayerByAttribute_management("service_requests_layer", "NEW_SELECTION", date_query)

# Apply spatial selection to select service requests within 10 meters of a sewer catch basin.
# The selection is based on the previous selection of service requests in November 2023 thus the use of "SUBSET_SELECTION"
arcpy.management.SelectLayerByLocation("service_requests_layer", "WITHIN_A_DISTANCE_GEODESIC", 
                                       "sewer_catch_basin_layer", "10 Meters", 
                                       "SUBSET_SELECTION")

# Get count of selected service requests
flood_count = int(arcpy.management.GetCount("service_requests_layer")[0])

# Clear the selection on the service requests layer
arcpy.management.SelectLayerByAttribute("service_requests_layer", "CLEAR_SELECTION")

# Print the result
print(f"Number of reported floods within 10 meters of a sewer drain in November 2023: {flood_count}")