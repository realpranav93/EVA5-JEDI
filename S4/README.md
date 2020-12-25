## **Objective:**
To build a Model to acheive a validation accuracy >=99.4% with less than 20k parameters for [MNIST](https://en.wikipedia.org/wiki/MNIST_database) dataset.
 
## **Code block by block:**

**Block1:** Is to load all the necessary libraries to build and train our model. 

**Block2:** Is to define the architecture of our model. Following are the key tools used while designing this architecture: 
- It's a expand and squeeze model. Number of kernels(also translates to number of parameters in a particular layer of a deep numeral network) are increased using 3x3 convolutions and decreased using 1x1 convolutions respectively 
- We have used Batch normalization to standardise activations and dropouts to decrease the overfit of the model(Basically decrease the gap between train accuracy and test accuracy)

**Block3:** Is to just visually understand the architecture and the total number of parameters utlised in the same. We can observe `16,138 parameters`. 
 
**Block4:** Is to download MNIST into train and test/validation data set. These are downloaded as packets of images called batches. Here we have a `batch size of 128`. We are also transforming the images by standardizing them and control of variation in unnnecessary aspects of the image. 

**Block5:** Is to define a functions for training(train function) and Evaluation(test function) that needs to be run on train and test data from block4 respectively. 
- **Train function** basically would do a forward pass to calculate model loss and adjust weights of the parameter in backward pass so that it can decrease the loss value to least possible value it can. Here loss function is [nll(negative log liklihood)](https://medium.com/deeplearningmadeeasy/negative-log-likelihood-6bd79b55d8b6)
- **Test function** takes the current version of trained model and predicts the outcome evaluates it against actual label to give you the accuracy that your model can acheive in the current iteration.

**Block6:** Is to Intialize the model instance from block2 and run the train and test from block5 for 20 iterations called epochs. In every epoch the train function goes through all the images in training once and updates the weights for every batch of 128 images. So given that there 60000 images in training in 1 epoch weights are updates ~ 468 times(60k/128).

## **Output and conclusion**
- We are able to observe epoch number, Train and test loss and accuracy in the output of block6
- `An validation accuracy of 99.44% is observed in 15 epoch` and we have used `16,138 paramerters` to acheive it.
