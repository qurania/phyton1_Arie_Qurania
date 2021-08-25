# Operasi image pada Python 
# pilihan load image (contoh logo ipb)
import matplotlib.pyplot as plt
import cv2
import numpy as np

print("read images using opencv")
five = cv2.imread("ipb.png")
print(five.shape)
print(five.size)
plt.imshow(five)
cv2.waitKey(0)
plt.show()

# konversi image
import cv2
babon = cv2.imread("babon.jpg")
babon_gray = cv2.cvtColor(babon, cv2.COLOR_BGR2GRAY)

#plt.imshow(babon) 
#plt.imshow(babon_gray)

f, arr = plt.subplots(2)

arr[0].imshow(babon)
arr[1].imshow(babon_gray)

plt.show()
# mengambil nilai matriksnya

# acces pixel of images per postion 
pixels = five[100,100]
print(pixels)


