"""
Purpose: Analyze the number of streets intersecting with service requests for street flooding
in November 2023 within different search distances.
"""

# Import necessary libraries
import arcpy

# Define input shapefiles
public_streets = r"G:\............\public-streets.shp"
service_requests = r"G:\............\Street_flooding.shp"

# Set search distances in meters
search_distances = [0, 1, 2.5, 5]

# Create feature layers for the input shapefiles
arcpy.MakeFeatureLayer_management(public_streets, "public_streets_layer")
arcpy.MakeFeatureLayer_management(service_requests, "service_requests_layer")

# Define the date range for November 2023. Would be used to filter the service requests layer
date_query = "Service__1 > '2023-11-01 00:00:00' And Service__1 < '2023-12-01 00:00:00'"

# Apply the date filter to the service requests layer
arcpy.SelectLayerByAttribute_management("service_requests_layer", "NEW_SELECTION", date_query)

# Function to calculate intersecting streets for a given search distance
def count_intersections(public_streets_layer, service_requests_layer, search_distance):
    # Clear any previous selection on the public streets layer
    arcpy.SelectLayerByAttribute_management(public_streets_layer, "CLEAR_SELECTION")
    
    # Select streets that are within a certain geodesic distance from the filtered service requests
    arcpy.SelectLayerByLocation_management(public_streets_layer, "WITHIN_A_DISTANCE_GEODESIC", service_requests_layer, f"{search_distance} Meters", "NEW_SELECTION")
    
    # Get count of intersecting streets
    count = int(arcpy.GetCount_management(public_streets_layer)[0])
    
    # Clear the selection on the public streets layer after getting the count
    arcpy.SelectLayerByAttribute_management(public_streets_layer, "CLEAR_SELECTION")
    
    return count

# Iterate over search distances and print the results
for distance in search_distances:
    num_intersections = count_intersections("public_streets_layer", "service_requests_layer", distance)
    print(f"Number of streets within a geodesic distance of {distance} meters: {num_intersections}")

# Clear the selection on the service requests layer
arcpy.SelectLayerByAttribute_management("service_requests_layer", "CLEAR_SELECTION")
