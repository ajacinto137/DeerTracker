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



print("\n")
print("-----------Dates---------------")
print(date)
print(len(date))
print("-------------------------------")
print("\n")
print("-----------Time---------------")
print(time)
print("-------------------------------")
print(len(date))


newDict={}
def test():
        temp = 0
        for i in range(len(date)-1):
                if date[i+1] != date [i]:
                        newDict[date[i]] = time[temp:i+1]
                        print("----------------------------------------")
                        print("Temp is now " + str(temp))
                        print("The Date is now" + str(date[i]))
                        print("i is " + str(i))
                        print(time[temp:i+1])
                        print("----------------------------------------")
                        temp = i+1
                        print(newDict)
                        plt.hist(newDict.get(date[i]),bins=24, range=[0,24])  # `density=False` would make counts
                        plt.ylabel('Hits')
                        plt.xlabel('Hour')
                        plt.title(date[i])
                        plt.show()
                if i == len(date)-2:
                        print("*************************************************")
                        print("----------------------------------------")
                        print("Temp is now " + str(temp))
                        print(time[temp:-1])
                        print("----------------------------------------")
                        newDict[date[i]] = time[temp:-1]
                        # print(newDict)
                        # print("\n")
                        # print("\n")
                        # print("\n")
                        plt.hist(newDict.get(date[i]),bins=24)  # `density=False` would make counts
                        plt.ylabel('Hits')
                        plt.xlabel('Hour')
                        plt.title(date[i])
                        plt.show()
        # print(newDict)

test()
keys_list = list(newDict)


# for i in range(len(newDict)):
#         # print(keys)
#         print(len(newDict))
#         print(newDict(1))
#         print("********************")
#         print(newDict.keys())
#         print("********************")
#         plt.hist(newDict.get(keys))  # `density=False` would make counts
#         plt.ylabel('Probability')
#         plt.xlabel('Data');
#         plt.show()

# print("\n")
# print("-------------------")
# print(a_key)
# print("-------------------")
# print("\n")


