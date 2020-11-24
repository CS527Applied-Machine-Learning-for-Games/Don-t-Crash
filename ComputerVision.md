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
In this method, we use a sliding window technique to detect and classify objects with high speed and accuracy in a single pass. For the purposes of our project, we decided to use YOLO v3.

![YOLO1](images/cars yolo.JPG)
![YOLO2](images/pedestrian2 yolo.JPG)

