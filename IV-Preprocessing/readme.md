🧪 Part IV - Preprocessing

Preprocessing is a crucial step in any remote sensing workflow. It transforms raw satellite data into clean, analysis-ready information. In this section, we’ll walk through several essential operations needed before starting classification, analysis, or visualization.

Each subsection below links to a dedicated script or notebook illustrating the operation.

    ⚠️ Note: Most of the tasks here are based on GDAL, rasterio, and other geospatial libraries.

📌 Overview of Preprocessing Tasks
1. 📐 Reprojection, Alignment & Resizing

Ensure all rasters share the same projection, pixel alignment, and resolution.
👉 See script
2. ✂️ Clipping, Cloud Masking, Merging

Cut rasters to your area of interest, remove cloud-covered areas, and merge adjacent scenes.
👉 See script
3. 🧱 Stacking Multiple Rasters

Combine multiple bands or dates into a single multi-layer GeoTIFF.
👉 See script
🔧 Additional Preprocessing Options
4. 🌍 CRS Harmonization

Reproject all datasets into a common CRS (e.g., EPSG:4326 or UTM).
👉 See script
5. 🔁 Resampling

Unify spatial resolutions (e.g., Sentinel-2 20m → 10m) using bilinear, cubic, or nearest methods.
👉 See script
6. 🧼 Raster Normalization

Normalize pixel values (e.g., min-max scaling) for machine learning or statistics.
👉 See script
7. 🗺️ Vector Mask Clipping

Clip rasters using vector files like shapefiles or GeoJSON.
👉 See script
8. 🚫 NoData Handling

Fix missing values or nodata pixels to avoid errors in downstream processing.
👉 See script
9. 🌓 Creating Masks

Generate binary masks for clouds, water, vegetation, etc. using band thresholds or QA layers.
👉 See script
📦 Bonus (Optional)

    🔄 Compression & optimization of GeoTIFFs (gdal_translate)

    🧩 Tiling large rasters for batch processing

    📆 Time filtering based on cloud cover or acquisition dates
