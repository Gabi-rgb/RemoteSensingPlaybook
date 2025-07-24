# Chapter V : Analysis & Feature Extraction

Once the data has been downloaded and preprocessed, the next step is to extract meaningful information from it. This phase is crucial in any remote sensing project, as it transforms raw pixel values into interpretable features for analysis or modeling.

This section introduces common techniques used to extract features from satellite imagery and geospatial data.
🔎 Covered Topics

Each topic below is accompanied by a Python notebook or script to illustrate its use:

    Spectral Indices
    Compute vegetation or water-related indices such as NDVI, NDWI, NDBI, SAVI, etc.
    ➤ ndvi_ndwi_indices.ipynb

    Band Math & Arithmetic
    Perform operations between bands (e.g., band ratios, differences, custom formulas).
    ➤ band_math.ipynb

    Zonal Statistics
    Extract statistics (mean, min, max, std) within polygons (like land parcels or administrative zones).
    ➤ zonal_statistics.ipynb

    Texture Analysis
    Calculate textural features using methods like GLCM (Grey-Level Co-occurrence Matrix), entropy, etc.
    ➤ texture_analysis.ipynb

    Change Detection
    Identify changes across multiple dates (e.g., vegetation loss, urban expansion) using image differencing or ratios.
    ➤ change_detection.ipynb

    Feature Engineering for ML/DL
    Prepare features for machine learning or deep learning pipelines: normalization, selection, extraction.
    ➤ feature_engineering.ipynb
