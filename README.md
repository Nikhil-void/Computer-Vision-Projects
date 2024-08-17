# Computer Vision Projects

This repository contains a collection of computer vision projects demonstrating various techniques and applications in the field. Each project is implemented in Python and leverages popular libraries like OpenCV, numpy, and scipy. Below is a brief overview of each project.

## Projects Overview

### 1. 3D Surface Estimate Using Visual Hull Technique

In this project, a still image of a dancer is captured using multiple cameras placed at various locations. The objective is to create a 3D surface estimate using voxel grids and the visual hull technique, followed by ray tracing to develop a textured 3D model.

- **Tech Stack:** Python, OpenCV, numpy, pandas, multiprocessing
- **Input:** Silhouette and colored images, camera calibration matrix
- **Output:** 3D textured model
- **Example:**
  - Input images:
    ![Input colored](https://github.com/Nikhil-void/Computer-Vision-Projects/blob/main/Visual%20Hull%203D%20Surface%20Estimation/input_data/actual_images/cam00_00023_0000008550.png)
    ![Input colored](https://github.com/Nikhil-void/Computer-Vision-Projects/blob/main/Visual%20Hull%203D%20Surface%20Estimation/input_data/actual_images/cam02_00023_0000008550.png)
  - Output:
    ![3D Textured model](https://github.com/Nikhil-void/Computer-Vision-Projects/blob/main/Visual%20Hull%203D%20Surface%20Estimation/Output_data/Textured_3d_model.gif)

### 2. Document Scanner Using Homography

This project implements a document scanner that uses homography to convert an image into a properly scanned copy.

- **Tech Stack:** Python, OpenCV

### 3. Depth Map Estimation from Stereo Images

This project involves calculating the disparity map using the rank transformation technique for two stereo-matched point clouds.

- **Tech Stack:** Python, OpenCV, scipy, math
- **Input:** Stereo images
- **Output:** Depth map
- **Example:**
  - Input stereo images:
    ![Stereo Image Left](https://github.com/Nikhil-void/Computer-Vision-Projects/blob/main/DepthMap%20Estimation%20from%20Sterio/Output_Images/Sterio_Image_1.jpg)
    ![Stereo Image Right](https://github.com/Nikhil-void/Computer-Vision-Projects/blob/main/DepthMap%20Estimation%20from%20Sterio/Output_Images/Sterio_Image_0.jpg)
  - Output:
    ![Depth Map](https://github.com/Nikhil-void/Computer-Vision-Projects/blob/main/DepthMap%20Estimation%20from%20Sterio/Output_Images/Sterio_Disparity_Amplified.jpeg)

### 4. Color-Based Object Tracking

This project creates an object tracker based on a color mask, which draws tracking lines marking the motion of the object.

- **Tech Stack:** Python, OpenCV
- **Example:**
  ![Example](https://github.com/Nikhil-void/Computer-Vision-Projects/blob/main/Color%20Based%20Object%20Tracker/screen_recorder.gif)

### 5. Camera Motion and Point-Cloud Manipulation

This project manipulates the camera's extrinsic matrix to create a half-circle motion around a foreground object, using separate point clouds for the foreground and background objects.

- **Tech Stack:** Python, OpenCV, scipy, math
- **Input:** Point clouds, camera intrinsic matrix
- **Output:** Motion visualization
- **Example:**
  ![Output](https://github.com/Nikhil-void/Computer-Vision-Projects/blob/main/Camera%20motion%20and%20point%20cloud%20manipulation/output.gif)

### 6. Bubble Test AutoGrader

This project creates an auto grader for multiple-choice question (MCQ) tests where students fill in answers. Contour detection techniques are used to identify answer options, which are then compared with an answer key to calculate the student's score.

- **Tech Stack:** Python, OpenCV, ImUtils, matplotlib
- **Example:**
  ![Graded Test](https://github.com/Nikhil-void/Computer-Vision-Projects/blob/main/Bubble%20Test%20Auto%20Grader/example.JPG)

### 7. Sobel Edge Detection with Direction

This project demonstrates Sobel edge detection along with direction visualization.

- **Tech Stack:** Python, OpenCV

## Getting Started

To run any of these projects, clone the repository and follow the installation steps provided in each project's individual README.

```sh
git clone https://github.com/yourusername/Computer-Vision-Projects.git
cd Computer-Vision-Projects
```



