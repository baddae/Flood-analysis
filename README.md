# Flood-analysis

This repository contains three Python scripts created to analyze street flooding incidents in the City of Vancouver. Each script is designed to perform a specific analysis related to street flooding based on spatial data and service requests.

## Usage
To use these scripts, you need to have ArcGIS Pro installed on your machine, as the scripts use the ArcPy library, which is part of ArcGIS Pro. You also need to have the input data for public streets, sewer catchment basin and service requests.

To run the scripts, simply open them in a Python environment (such as PyCharm, VS Code) and execute them. Make sure to update the file paths for the input shapefiles to match their location on your machine.

## Data
The data used in these scripts is not included in this repository due to its size. However, they can be obtained from the City of Vancouver's open data portal.


### 1. Flood_analysis_1.py
**Purpose:** Analyze the number of streets intersecting with service requests for street flooding in November 2023 within different search distances.

### 2. Flood_analysis_2.py
**Purpose:** To determine the number of reported street flooding incidents that occurred within 10 meters of a sewer catch basin in November 2023.

### 3. Flood_analysis_3.py
To create a script that counts the number of reported street flooding incidents that occurred within 10 meters of a sewer catch basin for each month since January 2022. The script will also output the results to an Excel file for additional analysis and visualization in other systems.


