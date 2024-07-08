# Efficient Image Segmentation using K-Means Clustering

## Overview

This project implements image segmentation using the K-Means clustering algorithm. The goal is to compress an image by reducing the number of colors while preserving the essential visual content. This is achieved by clustering the pixels of the image into a predefined number of clusters and replacing each pixel with the centroid of its cluster.

## Files

- `image_compression.py`: The main script that performs image segmentation using K-Means clustering.
- `Input_pic.PNG`: The input image used for the segmentation.
- `Figure_1_clusters_16.png`: Sample output image with 16 clusters.
- `Figure_1_clusters_3.png`: Sample output image with 3 clusters.

## How It Works

1. **Load Image**: The input image is loaded and normalized.
2. **Initialize Centroids**: Random centroids are selected from the image pixels.
3. **K-Means Clustering**: The algorithm iteratively assigns pixels to the nearest centroid and updates the centroids.
4. **Save Compressed Image**: The segmented image is saved with reduced colors based on the number of clusters.

## Dependencies

- `numpy`
- `matplotlib`
- `imageio`

Install the dependencies using:
```bash
pip install numpy matplotlib imageio
