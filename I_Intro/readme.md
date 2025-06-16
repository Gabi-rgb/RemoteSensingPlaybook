# Chapter I: Introduction to Remote Sensing

## 1. What is Remote Sensing?
Remote sensing is the science of acquiring information about the Earth's surface **without being in direct contact with it**. It generally uses **satellites or aircraft** to collect data by detecting the energy that is **reflected** or **emitted** from the Earth's surface.

It allows us to observe and monitor the Earth over time and at various scales.

---

## 2. Why is Remote Sensing Useful?
Remote sensing has a wide range of real-world applications:

- 🌱 **Agriculture**: crop health monitoring, drought detection
- 🏙️ **Urban planning**: land use classification, infrastructure development
- 🌳 **Environmental monitoring**: deforestation, glacier retreat
- 🌊 **Natural hazard response**: floods, wildfires, landslides
- 🌍 **Climate studies**: sea surface temperature, snow coverage

It helps scientists, governments, and communities to **analyze**, **predict**, and **respond** to environmental and societal changes.

---

## 3. Active vs Passive Remote Sensing
There are two main types of remote sensing:

| Type    | Description                                 | Example Sensors        |
|---------|---------------------------------------------|------------------------|
| Passive | Detects natural energy (usually sunlight)   | Sentinel-2, Landsat    |
| Active  | Emits energy and measures the reflection    | Sentinel-1 (SAR), LiDAR |

- **Passive sensors** rely on sunlight and work best during the day and under clear skies.
- **Active sensors** can operate day or night and through clouds or smoke.

---

## 4. Understanding Different Types of Resolution
Remote sensing data has different types of resolution that affect how it can be used:

- 🟡 **Spatial resolution**: The size of one pixel on the ground. Example: 10 m (Sentinel-2), 30 m (Landsat)
- 🔵 **Spectral resolution**: The number and width of spectral bands. Example: RGB, NIR, SWIR
- 🔴 **Temporal resolution**: How often the satellite revisits the same location. Example: Sentinel-2 = ~5 days
- ⚫ **Radiometric resolution**: The sensitivity of the sensor to detect slight differences in energy. Example: 8-bit (0–255), 16-bit (0–65535)

Understanding these helps you choose the right data for your analysis.

---

## 5. Common Earth Observation Satellites
Here are some of the most commonly used Earth observation satellites:

| Satellite     | Organization | Sensor Type | Primary Uses                      |
|---------------|--------------|-------------|-----------------------------------|
| Sentinel-2    | ESA          | Optical     | Land cover, vegetation health     |
| Sentinel-1    | ESA          | SAR (Radar) | Flood mapping, ground displacement |
| Landsat-8/9   | NASA/USGS    | Optical     | Historical analysis, land change  |
| MODIS         | NASA         | Optical     | Global monitoring, climate trends |

To learn more about each satellite, you can visit their respective official websites or data portals.

---

## 6. Why Python for Remote Sensing?
This project focuses on **Python** because:

- It is widely used in geospatial data science
- It has a strong ecosystem of scientific and geospatial libraries
- It is open-source and has a large community

Other languages like R or MATLAB are also used in remote sensing, but **this project will use Python exclusively** due to personal experience and the extensive support available.

Useful Python libraries:
- `GDAL`, `rasterio`: for reading and writing geospatial files
- `NumPy`, `Pandas`: for data handling
- `matplotlib`, `geopandas`, `folium`: for visualization and mapping
- `scikit-learn`, `xgboost`: for machine learning tasks

---

## 📚 What's Next?
You can continue to:
- [Go to Chapter II – Python Libraries for Remote Sensing](../II_libraries/remote_sensing_libraries.md) *(link to be updated)*
- Or return to the [Project Overview](../README.md)
