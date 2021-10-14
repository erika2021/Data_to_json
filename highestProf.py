#!/usr/bin/env python
# coding: utf-8

# In[1328]:


import pandas as pd
import json
import numpy



def main():
    csv = pd.read_csv(r'sadaData.csv')
    csv = scanCSV(csv)
    jsonD = JSONFormat(csv)
    with open('data2.json', 'w') as f:
        f.write(str(jsonD))




# Part 1
# Download the data file at https://gist.github.com/bobbae/b4eec5b5cb0263e7e3e63a6806d045f2 as "raw" and read the file into a program memory.

# The data file is in CSV format, the comma separated values format.

# Once the data is read into memory in your program, print out how many rows of the data is in the CSV data. This is your first printed answer.

# For each row, there are columns. One of the columns is the "profit". 
# The data in this profit column are not always valid. Sometimes the data is non-numeric. 
# Remove all rows with 'profit' that is not numerical value. Then print out how many rows of data are left, 
# after removing all the rows with invalid non-numeric profit column data. This is your second printed answer.




#counts number of rows, and removes rows where profit is not float type
#prints original number of rows, and prints number of rows after removal
# returns csv object with rwmoved rows
def scanCSV(csv):
    count = 0;
    countF = 0;
    skip = []
    for i in csv:
        count = 0;
        if "Profit" in i:
            for x in range(len(csv[i])):
                count= count+1;
                try: 
                    float(csv[i][x])
                    countF = countF+1;
                except:
                    csv = csv.drop(x)
                    
     
    csv = csv.reset_index(drop=True)
    print("Total number of rows: ", count)
    print("Number of rows that are left after removing N.A.: ", countF)
    return csv




# You can now convert the content your read into memory in your program in Part 1 into JSON format 
# and write it out to another file called data2.json which should only contain rows of data that have 
# the valid numeric profit values. Each row in the Array should contain data 
# columns like year, rank, company, revenue, and profit.

# Order the data based on the profit value. Print the top 20 rows with the highest profit values.
# This is your third printed answer.




# method that takes the CSV and returns the CSV into JSON format in order of highest to lowest profit
def JSONFormat(csv1):
    # casts the column to a float
    csv1["Profit (in millions)"] = csv1["Profit (in millions)"].astype(float)
    # Sorts the df based on the column"Profit in millions
    csv = csv1.sort_values('Profit (in millions)', ascending=False)
    csv = csv.reset_index(drop=True)
    data2 = []
    rows = len(csv["Profit (in millions)"])
    numPrint = 20
    printB = True
    print("Top 20: ")
    for x in range(rows):
        if len(csv["Profit (in millions)"]) == 0:
            break;
        dataRow = {}
        num = x
        for i in csv:
                dataRow[i] = csv[i][x]
        data2.append(dataRow)
        if printB:
            print(dataRow)
            numPrint = numPrint- 1
            if numPrint == 0:
                printB = False
    return data2




main()







