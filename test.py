import os
import os.path
import PIL.Image
import matplotlib
import matplotlib.pyplot as plt


test_array = [5,6,7,4,5,8,9,21,4,7,56,9,8,7,5,236,9,8,74,1,2]
plt.hist(test_array, bins = 500,range = (0,499))
plt.show()