#   Capstone EVA5 - Object Detection and Depth Estimation using a Encooder and Multi Decoder Architecture

**Contents:** 
1. Architecture
2. Training
3. Learnings
4. Code base

## Project Summary: 
Agenda of the project was to use existing state of the art architecture and utilize transfer learning technique to merge into a Single encoder --> Multi decoder achitecure. This model would take a input and give outs for both Object Detection and Depth Estimation. Here are the base models on which the architecture is inspired from: 
1. [Yolov3](https://github.com/theschoolofai/YoloV3)
2. [MiDaS](https://github.com/intel-isl/MiDaS) 

### Architecture:
Here is the Overall Architecture at higlevel look like: 

![image](https://github.com/realpranav93/EVA5-JEDI/blob/master/Captsone_EVA5/images/fork_model.PNG "Fork model")

**Encoder:** 
Though YoloV3 had darknet a form of densenet as its encoder, it is replaced by pre-trained resnext101 as encoder. It takes a image(img_size) and gives the following output: 
resolution of ouputs:
1. EC1: img_size/4
2. EC2: img_size/8
3. EC3: img_size/16
4. EC_out: img_size/32

![image](https://github.com/realpranav93/EVA5-JEDI/blob/master/Captsone_EVA5/images/resnext101_encoder.PNG "Encoder")

**Depth Decoder:**
As showcased in the below diagram outputs EC1, EC2, EC3, EC_out are passed into the decoder where they are connected to the respective upsampled blocks called feature fusion blocks through scratch layer. Feature fusion blocks are used to bring the resolution of the ouputs to the input resolution. 
ouput: [batch_size, img_size, img_size]
![image](https://github.com/realpranav93/EVA5-JEDI/blob/master/Captsone_EVA5/images/depth_decoder.PNG "Depth decoder")

**Yolo Decoder:**
Yolo decoder has three ouputs which are of the resolution of img_size/32, img_size/16, img_size/8 and are predicted at an anchor box and channel level which in this case is 9, 3 respectively. Inputs from Encoder are connected to yolo_decoder through 1 bottleneck convolution layer.

Inputs of yolo_decoder: EC2, EC3, EC_out 
ouputs of yolo_decoder: [batch_size, 3, img_size/32,img_size/32, 9], [batch_size, 3, img_size/16,img_size/16, 9], [batch_size, 3, img_size/8,img_size/8, 9]
![image](https://github.com/realpranav93/EVA5-JEDI/blob/master/Captsone_EVA5/images/yolo_decoder.PNG "Depth decoder")

Below figure showcases the internals of a individual(img_size/32) which in bottom to top order is a bottle neck followed by a path section(to be passed into a img_size/16 after upsampling) and tail section(which would be passed into a yolo_layer)
![image](https://github.com/realpranav93/EVA5-JEDI/blob/master/Captsone_EVA5/images/yolo_path_tail.PNG "Depth decoder")

### Training: 

Following is the code to be run to train the code: 

```
!python fork_train.py --cfg /content/EVA5-JEDI/Captsone_EVA5/cfg_yolo/yolov3-custom.cfg  --data '/content/drive/My Drive/EVA/EVA5/YoloV3_S13/YoloV3/data/customdata/custom.data' --batch 10 --cache --epochs 15 --train_decoder=yolo
```

Following are the parameters are to be passed for training: 
arguments| description |
---|---|
--cfg| Text file to generate base yolo model based on which fork model is built on|
--data|location of config file with information of labels and images for both train and test data|
train_decoder| argument to specify which part of fork to train `all - train both yolo and depth, depth - train depth decoder, yolo - train yolo decoder`|

Train Decoder argument: 
During back propagation of training, all the parameters in the modules of encoder are always frozen by making `require_grad = False`. And yolo and depth decoder are frozen as per the argument. And example of the output during the model initiation of training yolo decoder is as follows: 
```
resnet_layer 0 was frozen
resnet_layer 1 was frozen
resnet_layer 2 was frozen
resnet_layer 3 was frozen
depth_layer 0 was frozen
```
In this [notebook](https://github.com/realpranav93/EVA5-JEDI/blob/master/Captsone_EVA5/Capstone_eva5_pranav.ipynb) I have trained yolo and showcased that yolo_loss could be decreased and also showcased that all the decoders can also be trained simultaneoulsy. For yolo we have used the loss function used in stock yolov3 for depth a SSIM(structural similarity index measure) and MSE as loss. 

We have used tensorboard to log the training and here is the yolo_loss for the above training: 
![image](https://github.com/realpranav93/EVA5-JEDI/blob/master/Captsone_EVA5/images/yolo_loss.svg "yolo_training")

fork_loss for the same training instance: 
![image](https://github.com/realpranav93/EVA5-JEDI/blob/master/Captsone_EVA5/images/fork_loss%20_final.svg "yolo_training")

## Learnings: 

1. Given a chance again to do the assignmnet I would spend time in writing the training function from scractch to effectively test different loss functions. Currrently lot of time was spent in integrating 2 different code bases that starkly different.
2. I would also try training with different image sizes. 

## Code structure

Script| description |
---|---|
model.py| Script where fork model is defined. Fork model consists of encoder, depth_decoder, yolo_decoder, fork class|
model_yolo.py| Base model of yolo v3 on which yolo_decoder modules are taken and a network is built|
train_fork.py and test.py|Train and evaluaton of the model during Training|
utils_yolo| All the util functions like parsing and loading data e.t.c to run DarknetV3(yolov3) model|
blocks.py| utility functions for building Depth decoder|
depth_loss|SSIM function for evaluation for depth loss|
