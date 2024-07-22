"""
Purpose: To create a script that counts the number of reported street flooding incidents that occurred
within 10 meters of a sewer catch basin for each month since January 2022. The script will output the
results to an Excel file.
"""

# Import necessary libraries
import arcpy
import pandas as pd
from datetime import datetime, timedelta

# Define input shapefiles
sewer_catch_basin = r"G:\............\sewer-catch-basins.shp"
service_requests = r"G:\............\Street_flooding.shp"

# Create feature layers for the input shapefiles
arcpy.MakeFeatureLayer_management(sewer_catch_basin, "sewer_catch_basin_layer")
arcpy.MakeFeatureLayer_management(service_requests, "service_requests_layer")

# Define the start and end dates
start_date = datetime(2022, 1, 1)
end_date = datetime.now()

# Create a DataFrame to store the results. Initialize an empty DataFrame with columns for Month and Flood Count
df = pd.DataFrame(columns=['Month', 'Flood Count'])

# Iterate over each month since the start date
current_date = start_date
while current_date < end_date:
    # Define the date range for the current month
    next_month_date = current_date + timedelta(days=31)
    next_month_date = next_month_date.replace(day=1)
    date_query = f"Service__1 >= '{current_date.strftime('%Y-%m-%d %H:%M:%S')}' And Service__1 < '{next_month_date.strftime('%Y-%m-%d %H:%M:%S')}'"

    # Apply the date filter to the service requests layer
    arcpy.SelectLayerByAttribute_management("service_requests_layer", "NEW_SELECTION", date_query)

    # Apply spatial selection to select service requests within 10 meters of a sewer catch basin
    # The selection is based on the previous selection of service requests in November 2023 thus the use of "SUBSET_SELECTION"
    arcpy.management.SelectLayerByLocation("service_requests_layer", "WITHIN_A_DISTANCE_GEODESIC", 
                                           "sewer_catch_basin_layer", "10 Meters", 
                                           "SUBSET_SELECTION")

    # Get count of selected service requests
    flood_count = int(arcpy.management.GetCount("service_requests_layer")[0])

    # Clear the selection on the service requests layer
    arcpy.management.SelectLayerByAttribute("service_requests_layer", "CLEAR_SELECTION")

    # Add/Append the result to the DataFrame
    df = df._append({'Month': current_date.strftime('%B %Y'), 'Flood Count': flood_count}, ignore_index=True)

    # Print the result
    print(f"Number of reported floods within 10 meters of a sewer drain in {current_date.strftime('%B %Y')}: {flood_count}")

    # Move to the next month
    current_date = next_month_date

# Export the DataFrame to an Excel file
df.to_excel('G:/............/Monthly_reported_flooding.xlsx', index=False)
