# session1 assignment 

**1. What are Channels and Kernels (according to EVA)?** 

A simple black and white image can be looked as a matrix where every element from matrix is a pixel in image with values ranging from 0-255 where 255 being absolute white and 0 being pitch black. Now coloured image can be broken into similar matrix of colours(eg: Red,green,blue) which when stacked on top of each other would result in the original picture. 
 
 **Channel:** 
 A group/layer of similar characteristics of an image can be considered as a channel. Below figure you can observe that same peacock is divide into 3 layers of characterics that is a pixel value for colour green, red and blue. An image can be broken into any number of channels.
 
  ![Image](https://drive.google.com/uc?id=1quPLiZewo9yxQEsJohcOkwC_mmehAp0j)

  **Kernel:** 
  In Image processing to extract features we use small matrices (3x3,5x5 e.t.c.). This matrix helps us extract mutiple feature channels like edge detectors, horizontal detectors etc. A kernel can also be viewed as a `filter or feauture extractor` that can help us in manipulating and extracting parts of image for further analysis. Some of the examples can be blur kernel, sharpen kernel which are manually created kernels. Below you can see a vertical edge detector.
  
  ![Image](https://drive.google.com/uc?id=10jbReSFLy4Sm_2CKWRzKVvq1bhQRRwvw)
  
 --------------------------------------------------------------------------
 
 **2. Why should we (nearly) always use 3x3 kernels?**
 
 The process of extract of features using kernels from an image is called **convolution**. Convolution is simply a element wise multiplication of 2 matrices followed by a sum of all those multiplications. Here 2 matrices being kernel(green matrix) and part of image (blue matrix). A simple 3x3 convolution can be observed below
 
 ![Image](https://drive.google.com/uc?id=1yZqs8uhBJPzF9K3daMv8VyECJLPiZIMD)
 
 Convolution is a way to extract the information of pixel based on neighbouring pixels, kernel and pass it on to the next layers of information/channel. In generally the kerenl's center is placed on each and every element of input image and convolved using neighbouring pixels. `So, its imperative that the convolved information passed on to next layer is symmetric to the current pixel which is only possible in case odd numbers kernels`. As seen in the figure below even number kernels lack a centre and may cause bias in the information that would be passed to further layers. If we donot consider padding at image ends we generally end up n-k+1 matrix where input image is a nxn matrix and kernel is a kxk matrix. Which mean there is loss of information. So, bigger the kernel size more is the loss of information. Hence 3x3 kernel is the way to go!!!!!! 

![Image](https://drive.google.com/uc?id=1zeB0kygvwoaeYV_zPOD_544b4w40Zew9)

--------------

**3. How many times to we need to perform 3x3 convolutions operations to reach close to 1x1 from 199x199 (type each layer output like 199x199 > 197x197...)**

Number of iterations required:**99**

```
[199x199]*[3x3]-->[197x197]
[197x197]*[3x3]-->[195x195]
[195x195]*[3x3]-->[193x193]
[193x193]*[3x3]-->[191x191]
[191x191]*[3x3]-->[189x189]
[189x189]*[3x3]-->[187x187]
[187x187]*[3x3]-->[185x185]
[185x185]*[3x3]-->[183x183]
[183x183]*[3x3]-->[181x181]
[181x181]*[3x3]-->[179x179]
[179x179]*[3x3]-->[177x177]
[177x177]*[3x3]-->[175x175]
[175x175]*[3x3]-->[173x173]
[173x173]*[3x3]-->[171x171]
[171x171]*[3x3]-->[169x169]
[169x169]*[3x3]-->[167x167]
[167x167]*[3x3]-->[165x165]
[165x165]*[3x3]-->[163x163]
[163x163]*[3x3]-->[161x161]
[161x161]*[3x3]-->[159x159]
[159x159]*[3x3]-->[157x157]
[157x157]*[3x3]-->[155x155]
[155x155]*[3x3]-->[153x153]
[153x153]*[3x3]-->[151x151]
[151x151]*[3x3]-->[149x149]
[149x149]*[3x3]-->[147x147]
[147x147]*[3x3]-->[145x145]
[145x145]*[3x3]-->[143x143]
[143x143]*[3x3]-->[141x141]
[141x141]*[3x3]-->[139x139]
[139x139]*[3x3]-->[137x137]
[137x137]*[3x3]-->[135x135]
[135x135]*[3x3]-->[133x133]
[133x133]*[3x3]-->[131x131]
[131x131]*[3x3]-->[129x129]
[129x129]*[3x3]-->[127x127]
[127x127]*[3x3]-->[125x125]
[125x125]*[3x3]-->[123x123]
[123x123]*[3x3]-->[121x121]
[121x121]*[3x3]-->[119x119]
[119x119]*[3x3]-->[117x117]
[117x117]*[3x3]-->[115x115]
[115x115]*[3x3]-->[113x113]
[113x113]*[3x3]-->[111x111]
[111x111]*[3x3]-->[109x109]
[109x109]*[3x3]-->[107x107]
[107x107]*[3x3]-->[105x105]
[105x105]*[3x3]-->[103x103]
[103x103]*[3x3]-->[101x101]
[101x101]*[3x3]-->[99x99]
[99x99]*[3x3]-->[97x97]
[97x97]*[3x3]-->[95x95]
[95x95]*[3x3]-->[93x93]
[93x93]*[3x3]-->[91x91]
[91x91]*[3x3]-->[89x89]
[89x89]*[3x3]-->[87x87]
[87x87]*[3x3]-->[85x85]
[85x85]*[3x3]-->[83x83]
[83x83]*[3x3]-->[81x81]
[81x81]*[3x3]-->[79x79]
[79x79]*[3x3]-->[77x77]
[77x77]*[3x3]-->[75x75]
[75x75]*[3x3]-->[73x73]
[73x73]*[3x3]-->[71x71]
[71x71]*[3x3]-->[69x69]
[69x69]*[3x3]-->[67x67]
[67x67]*[3x3]-->[65x65]
[65x65]*[3x3]-->[63x63]
[63x63]*[3x3]-->[61x61]
[61x61]*[3x3]-->[59x59]
[59x59]*[3x3]-->[57x57]
[57x57]*[3x3]-->[55x55]
[55x55]*[3x3]-->[53x53]
[53x53]*[3x3]-->[51x51]
[51x51]*[3x3]-->[49x49]
[49x49]*[3x3]-->[47x47]
[47x47]*[3x3]-->[45x45]
[45x45]*[3x3]-->[43x43]
[43x43]*[3x3]-->[41x41]
[41x41]*[3x3]-->[39x39]
[39x39]*[3x3]-->[37x37]
[37x37]*[3x3]-->[35x35]
[35x35]*[3x3]-->[33x33]
[33x33]*[3x3]-->[31x31]
[31x31]*[3x3]-->[29x29]
[29x29]*[3x3]-->[27x27]
[27x27]*[3x3]-->[25x25]
[25x25]*[3x3]-->[23x23]
[23x23]*[3x3]-->[21x21]
[21x21]*[3x3]-->[19x19]
[19x19]*[3x3]-->[17x17]
[17x17]*[3x3]-->[15x15]
[15x15]*[3x3]-->[13x13]
[13x13]*[3x3]-->[11x11]
[11x11]*[3x3]-->[9x9]
[9x9]*[3x3]-->[7x7]
[7x7]*[3x3]-->[5x5]
[5x5]*[3x3]-->[3x3]
[3x3]*[3x3]-->[1x1]

```
-----------------------------------------------------------------------------------------------------

**4. How are kernels initialized?**
The weights of Kernels must be initialized to small random numbers preferably in between close to zero and less than 1. This along with Pixel value(generally range between 0-255) when normalized will help us eliminate exploding gradient problem that arrise during back propagation.

--------------------------------------------------------------------------------------------------
**5. What happens during the training of a DNN?**
Consider a example model as shown below which has 2 layers, each layer consisting of a convolution layer + a pooling layer. A convolution layer would have a kernels(whose purpose is to extract features from the image) with weights that are initiated with random values in between 0 to 1. 

![Image](https://drive.google.com/uc?id=1trz__XhwABeGgxzjXP0gvdz9ZXCVAZtL)

There are primarily 2 stages in training of a DNN or a CNN. 

**- Forward Pass:**
At every layer convolution operation happens with image pixels and kernels which are intiated with random values between 0 and 1. Then this information oftern reffered as channels are passed on to the next layer where the same operation happens.
` 
let X be the input image 
f() be the convolution at first layer 
Y1 = f(X) 
assuming g() as convolution at second layer 
Y1 = g(Y1) = g(f(X)) 
`

**- Backward Pass:** 
A cost function is defined which accounts for the error in our predictions. And backpropagation is done in which the kernels values(which were initiated at random during forward pass) are calculated by trial basis(also known as epochs) for every layer such the cost function is minimised. 













