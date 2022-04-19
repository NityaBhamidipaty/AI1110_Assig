#Ncert class 9 statistics 14.2 Q5
#Name: Nitya Seshagiri Bhamidipaty
#Roll no. cs21btech11041

import numpy as np
import pandas as pd

#read raw data from excel sheet
df = pd.read_excel(r'raw_data.xlsx')
raw_data = np.array(df)

#creating the grouped frequency table
bin = [0.04*i for i in range(7)] 
h = np.histogram(raw_data,bins = bin)

#creating class intervals 
class_intervals = ["{}-{}".format(bin[i],bin[i+1]) for i in range(6)]
class_intervals.append("Total")

#adding the total at the end of frequency column
new = np.append(h[0],raw_data.size)

#creating dataframe of the grouped frequency table and writing to excel
dict = {"Conc. of sulphur dioxide (ppm)":class_intervals,"Frequency":new}
gtable = pd.DataFrame(dict) 
gtable.to_excel('f_d.xlsx',index = False)

#counting how many days concentration is more than 0.11 ppm
raw_data = raw_data.flatten()
count = 0
for i in raw_data:
    if i > 0.11:
        count+=1
#printing the no. of days conc > 0.11 ppm
print(count)
