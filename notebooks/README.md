# Exploratory Data Analysis (EDA) on Solar Radiation Measurement Data

## Overview of the dataset
The data for this week's challenge is extracted and aggregated from Solar Radiation Measurement Data. Each row in the data contains the values for solar radiation, air temperature, relative humidity, barometric pressure, precipitation, wind speed, and wind direction, cleaned and soiled radiance sensor (soiling measurement) and cleaning events.

The structure of the data is as follows
- Timestamp (yyyy-mm-dd hh:mm): Date and time of each observation.
- GHI (W/m²): Global Horizontal Irradiance, the total solar radiation received per square meter on a horizontal surface.
- DNI (W/m²): Direct Normal Irradiance, the amount of solar radiation received per square meter on a surface perpendicular to the rays of the sun.
- DHI (W/m²): Diffuse Horizontal Irradiance, solar radiation received per square meter on a horizontal surface that does not arrive on a direct path from the sun.
- ModA (W/m²): Measurements from a module or sensor (A), similar to irradiance.
- ModB (W/m²): Measurements from a module or sensor (B), similar to irradiance.
- Tamb (°C): Ambient Temperature in degrees Celsius.
- RH (%): Relative Humidity as a percentage of moisture in the air.
- WS (m/s): Wind Speed in meters per second.
- WSgust (m/s): Maximum Wind Gust Speed in meters per second.
- WSstdev (m/s): Standard Deviation of Wind Speed, indicating variability.
- WD (°N (to east)): Wind Direction in degrees from north.
- WDstdev: Standard Deviation of Wind Direction, showing directional variability.
- BP (hPa): Barometric Pressure in hectopascals.
- Cleaning (1 or 0): Signifying whether cleaning (possibly of the modules or sensors) occurred.
- Precipitation (mm/min): Precipitation rate measured in millimeters per minute.
- TModA (°C): Temperature of Module A in degrees Celsius.
- TModB (°C): Temperature of Module B in degrees Celsius.
- Comments: This column is designed for any additional notes.

# Notebooks
This folder contains Jupyter notebooks for Exploratory Data Analysis (EDA).

`EDA.ipynb`: This notebook focuses on exploring and analyzing your data. It contains code for:
- Loading and cleaning the data
- Performing data analysis tasks (descriptive statistics, visualizations)
- Identifying patterns and relationships within the data

## Running the Notebooks

1. Install Dependencies: Ensure you have the required Python libraries installed for the notebooks to run. You can usually find the list of dependencies within the notebooks themselves or in a separate `requirements.txt` file.
2. Open in Jupyter Notebook: Launch Jupyter Notebook and navigate to the directory containing this README.md file. From here, you can open and run the notebooks (e.g., `EDA.ipynb`).