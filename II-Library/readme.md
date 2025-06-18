# Chapter II: Python Libraries for Remote Sensing

---

## 1. Setting Up a Virtual Environment

Before diving into libraries, it's important to understand virtual environments.  
Creating a virtual environment offers several important benefits when working with Python projects:
- It isolates your project dependencies, meaning each project can have its own versions of libraries without interfering with others.
- It prevents version conflicts, especially when you work on multiple projects requiring different versions of the same package.
- It makes your work reproducible, as you can easily share your environment setup with others or re-create it on a different machine using a requirements.txt or environment.yml file

In this example, I’ll show you how to create a virtual environment using **VSCode** and set it up as a **Jupyter kernel**.  
Warning : This example assumes you're using **Windows**, and that you have **Python installed**.  
If not, [Download Python here](https://www.python.org/)

### *First step :*
  Open the terminal in VSCode and type the following command. remote_sensing_env will be the name of your virtual environments. You can also specify a Python version if multiple versions are installed on your system.
       
    python -m venv remote_sensing_env
  
  Then activated with:
  
    remote_sensing_env\Scripts\activate
 
  If you see  *(remote_sensing_env) PS C:\Users\example\project\env\kernel>* everything is ok.
  
### *Second step :*

  Once the environment is activated, we are going to install Jupyter and ipykernel.
  
      pip install jupyter ipykernel
      
  Then link this environment to Jupyter with.   --name is the internal identifier used by Jupyter.  --display-name is what you will see in the Jupyter interface
     
      python -m ipykernel install --user --name=remote_sensing_env --display-name "Python (Remote Sensing)"
      
### *How to pip in the environment :*

  To pip a new libraries, you need to be in the environment. If you don't see *(remote_sensing_env) PS C:\Users\example\project\env\kernel>* in the terminal, you are not in. So type this :
  
      remote_sensing_env\Scripts\activate
      
  Then you can pip whatever you want. Like numpy for example.

      pip install numpy
      
### *Share or Reuse your environment :*

  When you have created your environment and installed some libraries, you can save their name and version on a requirement.txt. This txt will be usefull when you are on a new pc or when you need to share a project.
  To do so, go in your first environment and write :
  
      pip freeze > requirements.txt
      
  Create a new environment (see step 1) and write :

      pip install -r requirements.txt

---

## 2. Core Python Tools: NumPy and Matplotlib

At the heart of Python's data science ecosystem are [**NumPy**](https://numpy.org/) and [**Matplotlib**](https://matplotlib.org/).

- **NumPy** provides support for **multidimensional arrays (ndarrays)**, which are essential when working with raster data like satellite images. It allows fast, efficient operations on pixel values (mathematical, logical, etc.).

- **Matplotlib** is a plotting library that lets you visualize data, histograms, raster bands, or classification results.

These libraries are **powerful and lightweight**, making them ideal for remote sensing workflows.

---

## 3. Installing GDAL (Geospatial Data Abstraction Library)

[**GDAL**](https://gdal.org/en/stable/) is one of the most important libraries in remote sensing. It allows you to:
- Read and write geospatial raster and vector formats (GeoTIFF, Shapefile, etc.)
- Handle metadata and coordinate systems
- Perform raster calculations and reprojections

**Note**: GDAL can be tricky to install due to dependencies. I will explain how to do it below.

### *First step*
You need to download a .whl. You can find this files [here](https://github.com/cgohlke/geospatial-wheels/releases).

Look into the asset and find the correct .whl. We are searching for a file looking like this : *gdal-3.10.2-cp312-cp312-win_amd64.whl*.

3.10.2 is gdal version, cp312 is the python version(3.12 here), and finally win_amd64 is your systems (windows 64 bit here).

Choose the .whl who satisfy your profile and your need.

### *Second step*
  Next enter your virtual environment (see How to pip in the environment) and type :

    pip install C:\path\to\file\gdal-3.10.2-cp312-cp312-win_amd64.whl


---

## 4. Other Python Libraries for Geoprocessing

Beyond GDAL, many Python libraries help handle spatial data more efficiently:

- `rasterio`: Simplifies raster access using a Pythonic interface to GDAL
- `geopandas`: Extends pandas to support geospatial vector data (shapefiles, GeoJSON)
- `shapely`: Handles geometric operations (intersection, union, buffer, etc.)
- `pyproj`: Works with map projections and transformations
- `fiona`: Reads and writes vector data

These tools allow easier and more flexible handling of geospatial data.

---

## 5. Libraries for Machine Learning and Deep Learning

Machine learning is often used in remote sensing for classification, regression, and clustering.

Common libraries include:
- `scikit-learn`: Standard ML models (SVM, Random Forest, PCA, etc.)
- `xgboost`: Powerful gradient boosting for tabular and spatial data
- `tensorflow`, `keras`, `pytorch`: Deep learning libraries used for image classification, segmentation, and time series prediction

You will also find combinations of these tools with remote sensing data formats in advanced workflows.

---

- [Go to Chapter III – Downloading Remote Sensing Data](../III_data_download/readme.md)
- Or return to the [Project Overview](../README.md)

 
