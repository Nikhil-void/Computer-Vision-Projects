
# 3D Surface Estimate Using Visual Hull Technique

In this project, a still image of a dancer has been captured using multiple cameras placed in various locations of the room. We are provided with camera calibration matrix and the silhouette of the dancer as seen by each camera. We are also provided with the colored images so we can create textured model.

Our task is:
1. To create 3D surface estimate using voxel grids and visual hull technique
2. Use ray tracing to determine which portion of the silhouette is visible from which camera and we feed in the colors to make textured 3D model

## Tech Stack

**Language:** Python

**Modules:** OpenCV, numpy, pandas, multiprocessing, 


## Input Data
1. Input images silhouette and coloured
 Some examples
![Input colored]( https://github.com/Nikhil-void/Computer-Vision-Projects/blob/main/Visual%20Hull%203D%20Surface%20Estimation/input_data/actual_images/cam00_00023_0000008550.png)

![Input colored]( https://github.com/Nikhil-void/Computer-Vision-Projects/blob/main/Visual%20Hull%203D%20Surface%20Estimation/input_data/actual_images/cam02_00023_0000008550.png)

2. Camera calibration matrix
           
## Output
1. 3D Textured model
 ![3D Texured model]( https://github.com/Nikhil-void/Computer-Vision-Projects/blob/main/Visual%20Hull%203D%20Surface%20Estimation/Output_data/Textured_3d_model.gif)
