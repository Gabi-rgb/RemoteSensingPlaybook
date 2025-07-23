# Chapter IV : Preprocessing

Preprocessing is a crucial step in any remote sensing workflow. It transforms raw satellite data into clean, analysis-ready information. In this section, we’ll walk through several essential operations needed before starting classification, analysis, or visualization.

Each subsection below links to a dedicated script or notebook illustrating the operation.

Note: Most of the tasks here are based on GDAL, rasterio, and other geospatial libraries.

---
## 1. Reprojection, Alignment & Cliping
Ensure all input rasters share the same coordinate system, spatial resolution, and pixel grid. This step uses tools like gdalwarp.
[*Reprojection_Alignment_Cliping*](../IV-Preprocessing/Reprojection_Alignment_Cliping.ipynb)

---
## 2. Merge, cloudmasking & Normalization
Merge multiple scenes into one, apply cloud filtering (e.g. with QA bands or masks), and normalize reflectance values for better consistency across images.
[*Merging_cloudmasking_normalization*](../IV-Preprocessing/Merging_cloudmasking_normalization.ipynb)

---
## 3. Resampling & Pan-Sharpening
Adapt rasters to a target resolution using various resampling techniques, and apply pan-sharpening to enhance spatial resolution using panchromatic bands.
[*Resampling_Pansharpening*](../IV-Preprocessing/Resampling_Pansharpening.ipynb)

---
## 4. Stacking Multiband Rasters
Combine several single-band rasters (e.g. different dates or spectral bands) into a multi-band stack for machine learning or time-series analysis.
[*Stack*](../IV-Preprocessing/Stacking.ipynb)

---
## What's Next?
You can continue to:
- Go to Chapter [V – Downloading Remote Sensing Data](../V-Data_download/)
- Or return to the [Project Overview](../)
