#!/usr/bin/env python
# coding: utf-8

# In[22]:


from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import densenet
from tensorflow.keras.applications import vgg16
from tensorflow.keras.applications import mobilenet_v2
from tensorflow.keras.layers import AveragePooling2D
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Input
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from imutils import paths
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sn
import argparse
import cv2
import os
import os.path
from os import path
from keras.models import load_model
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np


# In[26]:


model= load_model('mod.h5')

def predict(img_path):
    img= image.load_img(img_path,target_size=(224,224))
    x= image.img_to_array(img)
    x= np.expand_dims(x, axis=0)
    imgdata=preprocess_input(x)
    classes=model.predict(imgdata)
    if(classes[0][0]*10e29 > classes[0][1]):
        return 'COVID +ve! Take Care'
    else:
        return 'COVID -ve!Still take Precautions'


# In[ ]:





# In[ ]:




