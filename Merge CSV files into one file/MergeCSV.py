import numpy
import pandas as pd
import os


os.chdir(r'C:\Users\jjenn\Google Drive\Jie Jenn (YouTube)\Python\How to merge multiple CSV files into one file' + '\\')

# now we need to get all the files
fileList = [file for file in os.listdir() if file.endswith('.xlsx')]

# empty dataframe to store all the data from each file
masterList = pd.DataFrame()

for file in fileList:
    df = pd.read_excel(file, sheet_name=0)
    masterList = masterList.append(df, ignore_index=True)
    

writer = pd.ExcelWriter('Boston Public School List.xlsx')
masterList.to_excel(writer, 'School List', index=False)
writer.save()
