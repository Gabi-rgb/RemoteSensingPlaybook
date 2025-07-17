from osgeo import gdal
gdal.UseExceptions()
import numpy as np
import matplotlib.pyplot as plt

def read_and_stretch(path, vmin=None, vmax=None, pmin=2, pmax=98):
    """
    Reads a raster file and applies contrast stretching.
    Returns the stretched array (scaled 0-1), its extent, and the min/max used.
    """
    ds = gdal.Open(path)
    band = ds.GetRasterBand(1)
    array = band.ReadAsArray()
    gt = ds.GetGeoTransform()
    cols, rows = ds.RasterXSize, ds.RasterYSize
    extent = (gt[0], gt[0] + cols * gt[1], gt[3], gt[3] + rows * gt[5])
    ds = None

    if vmin is None or vmax is None:
        vmin, vmax = np.percentile(array, (pmin, pmax))

    stretched = np.clip((array - vmin) / (vmax - vmin), 0, 1)
    return stretched, extent, vmin, vmax

def display_images(paths, titles=None, stretch='global', pmin=2, pmax=98, cmap='gray', axis_labels=("Easting (m)", "Northing (m)")):
    """
    Displays one or more raster images with consistent or individual stretching.

    Parameters:
        - paths: list of file paths to rasters
        - titles: list of titles (optional, defaults to path names)
        - stretch: 'global' or 'individual' stretch method
        - pmin/pmax: percentiles used if vmin/vmax are not given
        - cmap: matplotlib colormap
        - axis_labels: tuple (xlabel, ylabel)
    """
    if isinstance(paths, str):
        paths = [paths]

    if titles is None:
        titles = [f"Image {i+1}" for i in range(len(paths))]

    if len(titles) != len(paths):
        raise ValueError("The number of titles must match the number of images.")

    images = []
    extents = []

    # Global stretch: compute vmin/vmax from first image
    if stretch == 'global':
        _, _, global_vmin, global_vmax = read_and_stretch(paths[0], pmin=pmin, pmax=pmax)
        for path in paths:
            img, extent, *_ = read_and_stretch(path, vmin=global_vmin, vmax=global_vmax)
            images.append(img)
            extents.append(extent)

    elif stretch == 'individual':
        for path in paths:
            img, extent, *_ = read_and_stretch(path, vmin=None, vmax=None, pmin=pmin, pmax=pmax)
            images.append(img)
            extents.append(extent)

    else:
        raise ValueError("stretch must be either 'global' or 'individual'.")

    # Display
    fig, axes = plt.subplots(1, len(images), figsize=(6 * len(images), 6))
    if len(images) == 1:
        axes = [axes]

    for ax, img, extent, title in zip(axes, images, extents, titles):
        ax.imshow(img, cmap=cmap, extent=extent)
        ax.set_title(title)
        ax.set_xlabel(axis_labels[0])
        ax.set_ylabel(axis_labels[1])
        ax.grid(True, linestyle='--', alpha=0.5)

    plt.tight_layout()
    plt.show()
