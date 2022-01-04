import os
import csv
csvpath = os.path.join("Resources", "budget_data.csv")
# List to store data
totalMonths = 0
totalRevenue = 0
monthly_change = []
month_count = []
previous_revenue = 0
greatest_increase = 0
greatest_decrease = 0
greatest_month_increase = 0
greatest_month_decrease = 0

with open (csvpath, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = next(csv_reader)

#Find total number of months
    for row in csv_reader:
                
        #Calculate total months
        totalMonths += 1
        
        #Calculate Net Profit & Loss
        totalRevenue += int(row[1])
        
        # Monthly Change Calculation
        revenue_change = int(row[1]) - previous_revenue
        monthly_change.append(revenue_change)
        previous_row = int(row[1])
        month_count.append(row[0])
        
        #Greatest Increase Calculation
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_month_increase = row[0]
        
        #Greatest Decrease Calculation
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_month_decrease = (row[0])
            
        #Average Change Calculation
        average_change = sum(monthly_change)/ len(monthly_change)
        
        #Max and Min Calculation 
        Max = max(monthly_change)
        Min = min(monthly_change)
        
Financial_Analysis = (
f"Financial Analysis\n"
f"-----------------------------------------------------\n"
f"Total Months: {totalMonths}\n"
f"Total: ${totalRevenue}\n"
f"Average Change: ${average_change:.2f}\n"
f"Greatest Increase in Profits: {greatest_month_increase} (${Max})\n"
f"Greatest Decrease in Profits: {greatest_month_decrease} (${Min})\n")

print(Financial_Analysis)

#Export results to text file
output = os.path.join("Analysis", "financial_analysis.txt")
with open(output, "w") as txt_file:
    txt_file.write(Financial_Analysis)