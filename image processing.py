#!/usr/bin/env python
# coding: utf-8

# In[1]:


# pip install opencv-python


# In[3]:


import cv2


# In[4]:


img=cv2.imread(r"F:\ASHU\PICTURES\462321853.jpg")  # give image path/ image= collection of pixels
print(img)


# In[5]:


cv2.imshow('Frame',img) # display ka name rakha Frame
cv2.waitKey(0) # wait infinite time until key pressed
cv2.destroyAllWindows()


# In[ ]:




