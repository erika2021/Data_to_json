# Sada-Repo
## Run code:
# Dependecies:
- pandas
- numpy
- json
# Run:
- Clone this repository
- In bash, use command -> run.bat
## Input needed
- The input needed is a csv, with a column named "Prices (in millions)". You can change the input on the python script at the top and just change the name.
## Output produced
- The ouput produced is a json file named data2.json. There are also 3 print statments printed; the total number of rows there are in the csv, the total number of rows that are float numbers, and the top 20 rows, with the highest profit. 
## The code
- I split the code up into parts of the problem with the first part of my code, going through each of the rows and removing the rows where "Profit (in millions)" is not a float type. This gets rid of all the values that are "N.A.". (I could make my overall code more efficient, if I did this in the second part of the problem)
- I then used the function "sort_values()" to sort the dataframe based off of the column "Profit (in millions)" in ascending order, and then had to reset the index's for printing the rows in correct order. 
- Now that the data frame is in correct order, I traversed through each row, using a for loop, and then used another for loop to go through the column names and get each value at that (column, row) value. This is put into a dictionary (Each row had its own dictionary). After a rows dictionary was made I then appended the dictionary to the array. I also had a variable to count down from 20, to print the top 20 rows. After the for loop's are done then the csv (df) is in the correct format of a json file.
- I then cast the array of dictionaries to a string and exported it into a json file. I needed to cast the array to a string in order to keep the brackets and commas.
