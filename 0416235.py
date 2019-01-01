#!/usr/bin/env python
# coding: utf-8

# # DIP Mini Project
# * 0416235 劉昱劭

# In[1]:


import cv2
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


# In[2]:


img = cv2.imread('cover.PNG')
plt.figure(figsize=(28,20))
plt.subplot(1, 2, 1)
plt.title('Origin', fontsize=45)
plt.grid(True, linewidth=2)
plt.imshow(img)

size = int(img.shape[0]/10)

# generating the kernel
kernel_motion_blur = np.zeros((size, size))
for i in range(size//2, size):
    kernel_motion_blur[i][i] = 1
kernel_motion_blur = kernel_motion_blur / (size//2)

# applying the kernel to the input image
output = cv2.filter2D(img, -1, kernel_motion_blur)


plt.subplot(1, 2, 2)
plt.imshow(output)
plt.title('Blurred', fontsize=45)
plt.grid(True, linewidth=2)

plt.show()


# ## Visualize the filter
# * The shape of the window will be size/10 (about 68)
# * Only show the 5x5 window in the center.

# In[3]:


center = size//2
pd.DataFrame(kernel_motion_blur).iloc[center-2:center+3, center-2:center+3]


# In[ ]:





# ## Other testcase

# In[4]:


testcase = ['Q1.tif', 'Q2.tif', 'Q3.tif', 'Q4.tif']


# In[5]:


for idx, imgName in enumerate(testcase):

    img = cv2.imread(imgName)
    plt.figure(figsize=(28, 20*len(testcase)))
    plt.subplot(idx+1, 2, 1)
    plt.title('Origin', fontsize=45)
    #plt.grid(True, linewidth=2)
    plt.ylabel(imgName, fontsize=45, labelpad=70, rotation=0)
    plt.imshow(img)

    size = int(img.shape[0]/10)

    # generating the kernel
    kernel_motion_blur = np.zeros((size, size))
    for i in range(size//2, size):
        kernel_motion_blur[i][i] = 1
    kernel_motion_blur = kernel_motion_blur / (size//2)

    # applying the kernel to the input image
    output = cv2.filter2D(img, -1, kernel_motion_blur)


    plt.subplot(idx+1, 2, 2)
    plt.imshow(output)
    plt.title('Blurred', fontsize=45)
    #plt.grid(True, linewidth=2)

plt.show()


