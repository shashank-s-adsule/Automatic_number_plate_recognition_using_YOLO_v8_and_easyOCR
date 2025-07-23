# ANPR
<!-- no need sort.py but check once -->
 
## Dataset
- images
    - [Indian licence plate (small set)](https://www.kaggle.com/datasets/saisirishan/indian-vehicle-dataset?select=State-wise_OLX)
    - [Indian licence plate (large set)](https://www.kaggle.com/datasets/gauravsanwal/indian-licence-plate)             
    <!--downloaded in Dataset folder in D drive-->
- Videos
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