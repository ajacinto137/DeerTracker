import os
import os.path
import PIL.Image
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

date = []
time = []
directory = "PICS"
for filename in os.listdir(directory):
        img = PIL.Image.open(directory + '\\' + filename)
        exif_data = img._getexif()[36867]
        # print(exif_data)
        date.append(exif_data[0:10])
        # time is in hours
        time.append(exif_data[11:13])
        # print(exif_data[11:16])


#
# print("\n")
# print("-----------Dates---------------")
# print(date)
# print(len(date))
# print("-------------------------------")
# print("\n")
# print("-----------Time---------------")
# print(time)
# print("-------------------------------")
# print(len(date))


newDict={}
def test():
        temp = 0
        for i in range(len(date)-1):
                if date[i+1] != date [i]:
                        newDict[date[i]] = time[temp:i+1]
                        # print("----------------------------------------")
                        # print("Temp is now " + str(temp))
                        # print("i is " + str(i))
                        # print(time[temp:i+1])
                        # print("----------------------------------------")
                        # temp = i+1
                        # print(newDict)
                if i == len(date)-2:
                        # print("----------------------------------------")
                        # print("Temp is now " + str(temp))
                        # print(time[temp:-1])
                        # print("----------------------------------------")
                        newDict[date[i]] = time[temp:-1]
                        # print(newDict)
                        # print("\n")
                        # print("\n")
                        # print("\n")
        print(newDict)

test()
keys_list = list(newDict)

for keys in keys_list:
        print(keys)

# print("\n")
# print("-------------------")
# print(a_key)
# print("-------------------")
# print("\n")


