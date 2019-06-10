import os
import csv

month_count = 0
total_amount = 0.00

flpth = os.path.join("D:\\UOFT DATA ANALYTICS\\Homeworks\\3 Python Homework\\Big Data Analysis using Python\\python-challenge\\PyBank\\budget_data.csv")

with open (flpth,newline="",encoding="UTF-8") as csvFile:
    csvReader = csv.reader(csvFile,delimiter=",")

    header  = next(csvReader)
    
    for row in csvReader:
        month_count = month_count + 1
        total_amount = total_amount + int(row[1])
        
print("Financial Analysis")
print("-----------------------------------------------------------")
print(f"Total Months:  {month_count}")
print(f"Total:  {total_amount}")