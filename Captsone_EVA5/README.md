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
Though YoloV3 had darknet a form of densenet as its encoder, it is replaced by pre-trained resnext101 as encoder. 

![image](https://github.com/realpranav93/EVA5-JEDI/blob/master/Captsone_EVA5/images/resnext101_encoder.PNG "Encoder")
