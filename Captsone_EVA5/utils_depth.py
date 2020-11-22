import sys
import re
import numpy as np
import cv2
import torch

#write code to get targets fot depth
import zipfile
import numpy as np
from PIL import Image
import cv2
import io
import os

#name = '1.png'
#loc = 'D:/ML/EVA/JEDI/S14/midas_out_colormap-20201031T155204Z-001'
def get_depth_map(name, loc, img_size = 512):
    if '.zip' in loc:
        archive = zipfile.ZipFile(loc, 'r')
        required_list = [x for x in archive.namelist()
                        if str.split(x,'/')[1] in name]
        data = io.BytesIO(archive.read(required_list[0]))
        img = Image.open(data).convert('L')

    else:
        required_list = [os.path.join(loc,'midas_out_colormap',x) for x in os.listdir(os.path.join(loc,'midas_out_colormap'))
                     if x in name]
        img = Image.open(required_list[0]).convert('L')

    img = np.array(img)/255
    img = cv2.resize(img,  (img_size,img_size), interpolation=cv2.INTER_AREA)
    img = torch.from_numpy(np.expand_dims(img, axis=0)).contiguous().float()
    return(img)

def _get_depth_targets(paths,loc, img_size = 512):
    targets = []
    for x in paths:
      name = str.split(str.split(x,'images\\')[1],'.jpg')[0] + '.png'
      #print(name)
      targets.append(get_depth_map(name = name, loc = loc, img_size = img_size))
    return(torch.cat(targets))
