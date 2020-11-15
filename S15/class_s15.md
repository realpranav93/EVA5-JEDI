- regression with DNN is possible and good explore this
- kitti data set - germans are good at depth estimation
- 


#Questions: 

#### What is the metric and loss function for plane-segmentation model?
**metric:**

we can use dice coefficient = 2 * area of overall lap / total number pixels in both ground truth and prediction above is calculated for all classes of the image and averaged to get the dice coefficient of an image. [reference](https://towardsdatascience.com/metrics-to-evaluate-your-semantic-segmentation-model-6bcb99639aa2)

loss: 

BCEDiceLoss

[Segmentation in PyTorch using convenient tools](https://www.kaggle.com/artgor/segmentation-in-pytorch-using-convenient-tools)

#### What is the metric and loss function metric for depth model? 

#### Do you understand how to implement encoder and decoder implementation? 


#Steps to be done: 

1. Consolidate data: 
    - Create one single folder in google drive with zip files and not actual images to save space 
    - Create a dataset with small resolution images and also save as a zip - `probably downscale and crop to required size`
    - If you really want background data pic from EVA4 assignment: [satyajitghana drive](https://drive.google.com/drive/folders/10MBvlf6pMB78o-bWNe7tVlqNaIP3DtKQ)
    
2. 