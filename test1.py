import numpy as np
import pandas as pd
df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
columns=['a', 'b', 'c'])
print(df)

import pandas as pd
data = pd.read_csv("Data.csv", sep=";")
print(data)

# Membaca data dari file dengan format text (delimeter)
print("\n read text data with tab delimiter")
with open ('Data.txt') as data:
    print(data.read())


# Membaca data dari URL
import pandas as pd
f = pd.read_csv('http://www.exploredata.net/ftp/Spellman.csv')
print(f)

import numpy as sp
traffic = sp.genfromtxt("web_traffic.tsv",delimiter='\t')
print(traffic[:10])
print(traffic.shape)

x = traffic[:,0]
y = traffic[:,1]

x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]

import matplotlib.pyplot as plt
plt.scatter(x,y)
plt.title("Web traffic last month")
plt.xlabel("Time")
plt.ylabel("Hits/hour")

plt.xticks([w*7*24 for w in range(10)],['week %i' %w for w in range(10)])
plt.autoscale(tight=True)
plt.show()

# pilihan load image (contoh logo ipb)
import matplotlib.pyplot as plt
import cv2
import numpy as np

print("read images using opencv")
five = cv2.imread("5.png")
print(five.shape)
print(five.size)
plt.imshow(five)
cv2.waitKey(0)
plt.show()

babon = cv2.imread("5.png")
babon_gray = cv2.cvtColor(babon, cv2.COLOR_BGR2GRAY)

#plt.imshow(babon) 
#plt.imshow(babon_gray)
#plt.show()

f, arr = plt.subplots(2)
arr[0].imshow(babon)
arr[1].imshow(babon_gray)
plt.show()


# mengambil nilai matriksnya

# acces pixel of images per postion 
pixels = five[100,100]
print(pixels)



