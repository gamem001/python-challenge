#pybank

import os

# Module for reading CSV files
import csv

#set lists up and counters
Total_Count = 0
Total_Months = []
Net = 0
Total_Net = []
Monthly_Change = []
Date = []
Greatest_Increase = 0
Greatest_Increase_Month = 0
Greatest_Decrease = 0
Greatest_Decrease_Month = 0


#define file path to open
csvpath = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

#use open command with csvreader to open csv file
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csv_reader)
    row = next(csv_reader)
    
    #count total and net
    previous_row = int(row[1])
    Total_Count += 1
    Net += int(row[1])

    #count total and net, add data to lists
    for row in csv_reader:
        Total_Count += 1
        Net += int(row[1])
        Date.append(row[0])
        Net_Change = int(row[1]) - previous_row
        Monthly_Change.append(Net_Change)  
        previous_row = int(row[1])
        Total_Months.append(row[0])

        #find month that matches the greatest increase using greatest increase from row 1
        if int(row[1]) > Greatest_Increase: 
            Greatest_Increase = int(row[1])
            Greatest_Increase_Month = row[0]

        #find month that matches the greatest increase using greatest increase from row 1
        if int(row[1]) < Greatest_Decrease:
            Greatest_Decrease = int(row[1])
            Greatest_Decrease_Month = row[0]

        #find the min and mac of monthly change 
        Max = max(Monthly_Change)
        Min = min(Monthly_Change)

        #find the average of the monthly change and round
        Average = round(sum(Monthly_Change)/ len(Monthly_Change), 2)

#print statements for information calculated
print("Financial Analysis")
print("----------------------------------------------------------")
print(f"Total_Months: {Total_Count}")
print(f"Total_Net: ${Net}")
print(f"Average_Change: {Average}") 
print(f"Greatest_Increase: {Greatest_Increase_Month}, ${Max}")
print(f"Greatest_Decrease: {Greatest_Decrease_Month}, ${Min}")

#create output file and print statements for the outputs file
output_file = os.path.join("..", "PyBank", "Analysis", "PyBank_Analysis.text")

with open(output_file, 'w') as txtfile:

    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------------------------------------\n")
    txtfile.write(f"Total_Months: {Total_Count}\n")
    txtfile.write(f"Total_Net: ${Net}\n")
    txtfile.write(f"Average_Change: {Average}\n") 
    txtfile.write(f"Greatest_Increase: {Greatest_Increase_Month}, (${Max})\n")
    txtfile.write(f"Greatest_Decrease: {Greatest_Decrease_Month}, (${Min})\n")
   
