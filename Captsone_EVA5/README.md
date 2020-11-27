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

## Architecture:
Here is the Overall Architecture at higlevel look like: 

![image](https://github.com/realpranav93/EVA5-JEDI/blob/master/Captsone_EVA5/images/fork_model.PNG "Fork model")

**Encoder:** 
Though YoloV3 had darknet a form of densenet as its encoder, it is replaced by pre-trained resnext101 as encoder. It takes a image(img_size) and gives the following output: 

1. EC1: img_size/4
2. EC2: img_size/8
3. EC3: img_size/16
4. out: img_size/32

![image](https://github.com/realpranav93/EVA5-JEDI/blob/master/Captsone_EVA5/images/resnext101_encoder.PNG "Encoder")

**Depth Decoder:**
![image](https://github.com/realpranav93/EVA5-JEDI/blob/master/Captsone_EVA5/images/depth_decoder.PNG "Depth decoder")

**Yolo Decoder:**

![image](https://github.com/realpranav93/EVA5-JEDI/blob/master/Captsone_EVA5/images/yolo_decoder.PNG "Depth decoder")

sdadfadf
![image](https://github.com/realpranav93/EVA5-JEDI/blob/master/Captsone_EVA5/images/yolo_path_tail.PNG "Depth decoder")
