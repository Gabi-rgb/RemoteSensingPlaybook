# Chapter III : Downloading Remote Sensing Data

Remote sensing data is freely available from several platforms, but understanding where to get it and how to retrieve it efficiently is a key skill.

---
## 1. Public Portals for Manual Download

Several well-known websites allow you to manually search and download satellite imagery:

- [USGS Earth Explorer](https://earthexplorer.usgs.gov/) – Landsat, MODIS, and more

- [Copernicus Browser](https://browser.dataspace.copernicus.eu) – Sentinel-1, Sentinel-2, etc.

- [ESA Data Portal](https://earth.esa.int/eogateway/catalog) – Various European Earth Observation missions

- [NASA Earthdata](https://www.earthdata.nasa.gov/) – MODIS, VIIRS, and other global datasets

These portals let you search by date, location, satellite, and cloud cover, and preview scenes before downloading.

However, this manual method can quickly become time-consuming when dealing with large datasets or long time series.

---
## 2. Automating Downloads with APIs

To streamline the process, many platforms provide APIs or command-line tools. These allow you to automate and batch-download scenes, directly from your Python scripts or terminal.
Benefits of using APIs:

- Automate bulk downloads (e.g., dozens or hundreds of scenes)

- Filter by precise parameters (date, cloud cover, tile ID, etc.)

- Integrate downloads directly into your processing pipeline

---
## 3. Access Conditions

While much of the data is free and open, some restrictions may apply:

- You often need to create an account and authenticate via API tokens or credentials.

- Some APIs or datasets may require authorization or project approval (e.g., high-resolution commercial imagery).

- For very large requests, providers may throttle the download speed or limit the number of queries.

Be sure to read the terms of use and understand the access policy of each platform.

---
## What's Next?
You can continue to:
- Go to Chapter [IV – Downloading Remote Sensing Data](../III-Data_download/)
- Or return to the [Project Overview](../)
