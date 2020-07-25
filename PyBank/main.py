#pybank

import os

# current_working_directory = os.getcwd()
# print(current_working_directory)

# Module for reading CSV files
import csv

#define file path to open
csvpath = os.path.join("..", "..", "Desktop", "Bootcamp", "Repos", "python-challenge", "PyBank", 'Resources', "budget_data.csv")

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)