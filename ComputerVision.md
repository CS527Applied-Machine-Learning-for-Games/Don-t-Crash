---
layout: default
title: Computer Vision
permalink: /Computer Vision/
---

# Computer Vision

Computer Vision is an important part of the autonomous driving pipeline. By employing vision methods, our agent is able to detect and classify objects around it such as pedestrians, buildings and other vehicles.

## Mask R-CNN
Mask R-CNN is an instance segmentation technique, which locates each pixel of an object instead of a bounding box.  It classifies the image to the class it belongs to and makes dense predictions inferring labels for each pixel in the classified object of the image for the whole input. It provides not only the classes but the spatial location of the classes that are predicted. 

Mask R-CNN is a progressively improved technique, from R-CNN, Fast R-CNN, Faster R-CNN to Mask-RCNN. It uses a backbone CNN network of ResNet50 architecture or an FPN to convert the image into a feature map from (1024x1024px x 3) to (32x32x2048)

![RCNN1](images/Rcnn1.png)
![RCNN2](images/rcnn2.png)

## YOLO
In this method, we use a sliding window technique to detect and classify objects with high speed and accuracy in a single pass. For the purposes of our project, we decided to use YOLO v3 over Mask R-CNN due to its high speed and accuracy.

![YOLO1](images/cars yolo.JPG)
![YOLO2](images/pedestrian2 yolo.JPG)

Based on YOLO, we designed a closeness metric which takes into account the size of the object along with the length of the perpendicular drawn from the object to the bottom of the image. This allows the car to prioritize avoiding collision with objects closest to it.

![Closeness in City Environment](images/closeness_city.jpg)
![Closeness in Custom Environment](images/closeness_custom.png)
