import numpy as np
import pandas as pd
import matplotlib
import os


folder = ''
flow_path = ''
data1= []
for dirname, dirs, files in os.walk(folder):
    for dir1 in dirs:
        print(dir1)

        files1 = [f for f in os.listdir(folder+"\\"+dir1)]
        files2 = [f for f in os.listdir(flow_path + "\\" + dir1)]
        for i in range(len(files1)-1):
            curr = []
            curr.append(dir1+"/"+files1[i])
            curr.append(dir1 + "/" + files1[i+1])
            curr.append(dir1+"/"+files2[i])
            data1.append(curr)


df1 = pd.DataFrame(data1, columns=["img1","img2","flow"])
df1.to_csv("sintel_dataframe.csv")