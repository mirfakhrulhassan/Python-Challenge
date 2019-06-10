import os
import csv

month_count = 0
total_amount = 0.00
average_change = 0
profit_loss = []
average_chnge = []
dateList=[]

flpth = os.path.join("D:\\UOFT DATA ANALYTICS\\Homeworks\\3 Python Homework\\Big Data Analysis using Python\\python-challenge\\PyBank\\budget_data.csv")

with open (flpth,newline="",encoding="UTF-8") as csvFile:
    csvReader = csv.reader(csvFile,delimiter=",")

    header  = next(csvReader)
    
    for row in csvReader:
        month_count = month_count + 1
        total_amount = total_amount + int(row[1])
        profit_loss.append(float(row[1]))
        dateList.append(row[0])

    for x in range(1,len(profit_loss)):
        average_chnge.append(profit_loss[x]-profit_loss[x-1])
    
    average_change= sum(average_chnge)/len(average_chnge)

print("Financial Analysis")
print("-----------------------------------------------------------")
print(f"Total Months:  {month_count}")
print(f"Total: $ {total_amount}")
print(f"Average  Change: $ {round(average_change,2)}")
print(f"Greatest Increase in Profits:  {dateList[(average_chnge.index(max(average_chnge)))+1]} (${max(average_chnge)})")
print(f"Greatest Decrease in Profits:  {dateList[(average_chnge.index(min(average_chnge)))+1]} (${min(average_chnge)})")

outflpth = "PyBank.txt"

with open(outflpth,"w") as textFile:
    textFile.write("Financial Analysis \n")
    textFile.write("----------------------------------------------------------- \n")
    textFile.write(f"Total Months:  {month_count}\n")
    textFile.write(f"Total: $ {total_amount}\n")
    textFile.write(f"Average  Change: $ {round(average_change,2)}\n")
    textFile.write(f"Greatest Increase in Profits:  {dateList[(average_chnge.index(max(average_chnge)))+1]} (${max(average_chnge)})\n")
    textFile.write(f"Greatest Decrease in Profits:  {dateList[(average_chnge.index(min(average_chnge)))+1]} (${min(average_chnge)})\n")