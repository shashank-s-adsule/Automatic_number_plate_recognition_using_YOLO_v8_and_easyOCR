# Automatic number plate recognition using YOLO v8 and easyOCR
This project implements Automatic Number Plate Recognition using YOLOv8 for license plate detection and EasyOCR for text extraction.
It processes images or videos, detects number plates in real time, and recognizes alphanumeric text efficiently.
Ideal for smart parking, traffic monitoring, and security applications.
<!-- no need sort.py but check once -->

 
## Dataset
- images
    - [Indian licence plate (small set)](https://www.kaggle.com/datasets/saisirishan/indian-vehicle-dataset?select=State-wise_OLX)
    - [Indian licence plate (large set)](https://www.kaggle.com/datasets/gauravsanwal/indian-licence-plate)          
    <!--downloaded in Dataset folder in D drive-->
- Videos
    - [sample european car showcase](./dataset/video/demo.mp4) 
    - [sample Indian number plate (augmented)](./dataset/video/IND_demo.mp4) 
    <!-- - [traffic video](https://www.youtube.com/watch?v=MNn9qKG2UFI&list=PLcQZGj9lFR7y5WikozDSrdk6UCtAnM9mB) -->

## Train YOLO V8
- to train YOLO models we have to prepare the dataset set in a specfic format like .yaml or dataloader. here I'm using [`IN_NP_large_set.yaml`](./dataset/IN_NP_large_set.yaml) 
- to start training create a instance of model and use `model.train(**args)` to begin training. [train.ipynb](./Model/train.ipynb) for training refrence
- adjust the epochs, batchs, num workers, devices to Fine Tune the model. default parameter which i have used are listed below

|parameters|value|
|:-:|:-:|
|Dataset|Indian licence plate (large set)|
|epochs|50|
|Device|CUDA (GPU)|
|image size|640 x 640|

## Inference On YOLO V8
after performing infernce on image and video sample set it showed average accuracy about 89%-96% for images and 76%-89% for videos
### Infernece on Image

|![Sample test image](./dataset/images/test1.jpg)|![infernced test image](./assests/images/image_inference.png)|
|:-:|:-:|
|Orignal Test Image|Image after Infernece|

### Infernce on Video
|![Sample test Video](./assests/video/demo.gif)|![infernced test Video](./assests/video/demo_inference.gif)|
|:-:|:-:|
|Orignal Test Video|Video after Infernece|


## Future work
- intigrate object tracking using SORT (simple online and realtime tracking algorithm) [refernce:  [https://github.com/abewley/sort](https://github.com/abewley/sort)]