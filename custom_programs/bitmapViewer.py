import os
import scipy as sci
import matplotlib.pyplot as plt
import numpy as np
import PIL 
from PIL import Image

# file = r"C:\Users\antho\InfraTracker\2-1-25 Trip\image_series_set4-_3.bmp"
# file = r"C:\Users\antho\InfraTracker\2-1-25 Trip\image_series_set5-_15.tiff"
file = r"C:\Users\antho\InfraTracker\2-1-25 Trip\testimages_set7_8.bmp"
fSize = [int(2592),int(1944)]
imgSubbed = np.zeros((fSize[1],fSize[0]))
imChosen = 2


img = Image.open(file)
imgReshaped = np.reshape(list(img.getdata()),(fSize[1],fSize[0]))
avg = np.average(imgReshaped)

for i in range(fSize[0]):
    for j in range(fSize[1]):
        imgSubbed[j][i] = imgReshaped[j][i] #- avg
        if imgSubbed[j][i] < 1.2*avg:
            imgSubbed[j][i] = 0
        if i < fSize[0] or j < fSize[1]:
            if imgSubbed[j][i] < 0.05*imgSubbed[j-1][i-1]:
                imgSubbed[j-1][i-1] = 0

print(np.sum(imgSubbed))

if imChosen == 1:
    plt1 = plt.imshow(img,'jet')
elif imChosen == 2:
    plt2 = plt.imshow(imgSubbed,'jet') 

plt.show()