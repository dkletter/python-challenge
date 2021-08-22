import os
import csv

total = 0
months = []
p_and_l = []

# Path to collect data from the resources folder
budget_csv = os.path.join('resources','budget_data.csv')

with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

for row in csv_reader:
    months.append(row[0])
    p_and_l.append(row[1])
    total = total + int(row[1])