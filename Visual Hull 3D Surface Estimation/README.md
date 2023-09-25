
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

![Sterio Image Left]( https://github.com/Nikhil-void/Computer-Vision-Projects/blob/main/DepthMap%20Estimation%20from%20Sterio/Output_Images/Sterio_Image_1.jpg)

![ Sterio Image Right]( https://github.com/Nikhil-void/Computer-Vision-Projects/blob/main/DepthMap%20Estimation%20from%20Sterio/Output_Images/Sterio_Image_0.jpg)
           
## Output
 ![Depth Map]( https://github.com/Nikhil-void/Computer-Vision-Projects/blob/main/DepthMap%20Estimation%20from%20Sterio/Output_Images/Sterio_Disparity_Amplified.jpeg)
