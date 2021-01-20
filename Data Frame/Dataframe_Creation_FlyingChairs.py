import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib.image import imread

images = os.listdir('')
flow =os.listdir('')


data_1 = []
for i in range (0,22873):
    curr = []
    if(i<10):
        curr_file_1 = '0000'+str(i)+"_img1.ppm"
        curr_file_2 = '0000' + str(i) + "_img2.ppm"
        flo1 = '0000'+str(i)+"_flow.flo"
    elif(i<100):
        curr_file_1 = '000' + str(i) + "_img1.ppm"
        curr_file_2 = '000' + str(i) + "_img2.ppm"
        flo1 = '000' + str(i) + "_flow.flo"
    elif(i<1000):
        curr_file_1 = '00' + str(i) + "_img1.ppm"
        curr_file_2 = '00' + str(i) + "_img2.ppm"
        flo1 = '00' + str(i) + "_flow.flo"
    elif(i<10000):
        curr_file_1 = '0' +str(i) + "_img1.ppm"
        curr_file_2 = '0' + str(i) + "_img2.ppm"
        flo1 = '0' + str(i) + "_flow.flo"
    else:
        curr_file_1 =   str(i) + "_img1.ppm"
        curr_file_2 =  str(i) + "_img2.ppm"
        flo1 =  str(i) + "_flow.flo"

    curr.append(curr_file_1)
    curr.append(curr_file_2)
    curr.append(flo1)

    data_1.append(curr)


df1 = pd.DataFrame(data_1,columns=["img1","img2","flow"])

df1.to_csv("FlyingChairs_dataframes.csv")
