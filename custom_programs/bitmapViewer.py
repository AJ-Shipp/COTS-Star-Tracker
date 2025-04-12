import os
import scipy as sci
import matplotlib.pyplot as plt
import numpy as np
import PIL 
from PIL import Image

file = r"G:\My Drive\Terminus\2-22-25_Trip\310ms_24d1g_v2_10.tiff"
# file = r"C:\Users\antho\InfraTracker\2-1-25 Trip\image_series_set5-_15.tiff"
# file = r"C:\Users\antho\InfraTracker\2-1-25 Trip\testimages_set7_8.bmp"
fSize = [int(2592),int(1944)]
imgSubbed = np.zeros((fSize[1],fSize[0]))
imChosen = 2

darkFile = r"C:\Users\antho\InfraTracker\2-13-25_Tests\test_images-_11.tiff"
darkImg = Image.open(darkFile)
darkImgReshaped = np.reshape(list(darkImg.getdata()),(fSize[1],fSize[0]))
avg = np.average(darkImgReshaped)


img = Image.open(file)
imgReshaped = np.reshape(list(img.getdata()),(fSize[1],fSize[0]))
# avg = np.average(imgReshaped)

for i in range(fSize[0]):
    for j in range(fSize[1]):
        imgSubbed[j][i] = imgReshaped[j][i] - avg
        if i < fSize[0] or j < fSize[1]:
            if imgSubbed[j][i] < 0.05*imgSubbed[j-1][i-1]:
                imgSubbed[j-1][i-1] = 0

# for n in range(fSize[0]):
#     for m in range(fSize[1]):
#         if imgSubbed[m][n] < 1.2*avg:
#             imgSubbed[m][n] = 0

print(avg)

imgSubbed2 = np.zeros((fSize[1],fSize[0]))
avgDarkVal = np.average(imgReshaped[810:840,1150:1190])
for i in range(fSize[0]):
    for j in range(fSize[1]):
        imgSubbed2[j][i] = imgReshaped[j][i] - avgDarkVal
        if imgSubbed2[j][i] < 1.2*avgDarkVal:
            imgSubbed2[j][i] = 0
        if i < fSize[0] or j < fSize[1]:
            if imgSubbed2[j][i] < 0.05*imgSubbed2[j-1][i-1]:
                imgSubbed2[j-1][i-1] = 0

avgDarkVal = np.average(imgReshaped[810:840,1150:1190])
print(avgDarkVal)
#imgReshaped[810:840,1150:1190]

plt0 = plt.subplot(221)
plt0 = plt.imshow(imgReshaped,'jet')
plt0 = plt.title('1: Avg%.0f Sum%.2f'%((imgReshaped.shape[0]*imgReshaped.shape[1])/np.sum(imgReshaped),np.sum(imgReshaped)))
plt0 = plt.subplot(222)
plt0 = plt.imshow(darkImgReshaped,'jet')
plt0 = plt.title('2: Avg%.0f Sum%.2f'%((darkImgReshaped.shape[0]*darkImgReshaped.shape[1])/np.sum(darkImgReshaped),np.sum(darkImgReshaped)))
plt0 = plt.subplot(223)
plt0 = plt.imshow(imgSubbed,'jet')
plt0 = plt.title('3: Avg%.0f Sum%.2f'%((imgSubbed.shape[0]*imgSubbed.shape[1])/np.sum(imgSubbed),np.sum(imgSubbed)))
plt0 = plt.subplot(224)
plt0 = plt.imshow(imgSubbed2,'jet')
plt0 = plt.title('4: Avg%.0f Sum%.2f'%((imgSubbed2.shape[0]*imgSubbed2.shape[1])/np.sum(imgSubbed2),np.sum(imgSubbed2)))
# plt0 = plt.subplot(224)
# plt0 = plt.imshow(img,'jet')

plt.show()

"""
from astropy.io import fits

file = r"C:\Users\antho\InfraTracker\Testing_3-29\70ms_10g_50ict_0bl_0d50gam_1.tiff"
img = Image.open(file)
imgReshaped = np.reshape(list(img.getdata()),(1944,2592))

file2 = r"C:\Users\antho\InfraTracker\Testing_3-29\100ms_10g_50ict_0bl_0d50gam_1.tiff"
img2 = Image.open(file2)
imgReshaped2 = np.reshape(list(img2.getdata()),(1944,2592))

file3 = r"C:\Users\antho\InfraTracker\Testing_3-29\70ms_0g_50ict_0bl_0d50gam_1.tiff"
img3 = Image.open(file3)
imgReshaped3 = np.reshape(list(img3.getdata()),(1944,2592))

file4 = r"C:\Users\antho\Videos\NG\Testing_3-21\img_0-0.fits"
with fits.open(file4) as hdul:
    img4 = hdul[1].data
for i in range(0,img4.shape[1]):
    for j in range(0,img4.shape[0]):
        if img4[j][i] < 0:
            img4[j][i] = 0

file5 = r"C:\Users\antho\InfraTracker\Testing_3-29\Brights\dk-70ms_0g_50ict_0bl_0d50gam_1.tiff"
img5 = Image.open(file5)
imgReshaped5 = np.reshape(list(img5.getdata()),(1944,2592))

file6 = r"C:\Users\antho\InfraTracker\Testing_3-29\Brights\dk-100ms_0g_50ict_0bl_0d50gam_1.tiff"
img6 = Image.open(file6)
imgReshaped6 = np.reshape(list(img6.getdata()),(1944,2592))


plt.subplot(321)
plt.imshow(imgReshaped)
plt.colorbar()
plt.title(file[41:]+"\nDark Avg:"+str(np.average(imgReshaped[0:250,2250:2500])))

plt.subplot(322)
plt.imshow(imgReshaped2)
plt.colorbar()
plt.title(file2[41:]+"\nDark Avg:"+str(np.average(imgReshaped2[0:250,2250:2500])))

plt.subplot(323)
plt.imshow(imgReshaped3)
plt.colorbar()
plt.title(file3[41:]+"\nDark Avg:"+str(np.average(imgReshaped3[0:250,2250:2500])))

plt.subplot(324)
plt.imshow(img4)
plt.colorbar()
plt.title(file4[38:]+"\nDark Avg:"+str(np.average(img4[0:250,2250:2500])))

plt.subplot(325)
plt.imshow(imgReshaped5)
plt.colorbar()
plt.title(file5[49:]+"\nDark Avg:"+str(np.average(imgReshaped5[0:250,2250:2500])))

plt.subplot(326)
plt.imshow(imgReshaped6)
plt.colorbar()
plt.title(file6[49:]+"\nDark Avg:"+str(np.average(imgReshaped6[0:250,2250:2500])))


plt.show()
"""