import os
import csv

# Create path into csv file budget data
csvpath = os.path.join("..",'Resources', 'budget_data.csv')

# Set variables for calculation  
month_count = 0
total_revenue = 0 
current_revenue = 0
previouse_revenue = 0
revenue_change = 0

# Make append columns to contain list data
revenue_changes = []
month = []

# Open CSV Budget_data file 
with open(csvpath) as csvpybank:
    csvreader = csv.reader(csvpybank, delimiter=',')
    # skip headers
    csv_header = next(csvreader)
    
    # loop through data file as csvreader to get a define value
    for row in csvreader:

    # Calculate month count and total revenue
        month_count += 1
        month.append(row[0])
        current_revenue = float(row[1])
        total_revenue += current_revenue
    
    # print(month_count)
    # print(total_revenue)

     # Calculate revenue change to find average revenue change
        if month_count > 1:
            revenue_change = current_revenue - previouse_revenue
            revenue_changes.append(revenue_change)
            previouse_revenue = current_revenue

    # Analyze the average revenue change, max and min of revenue change following by month
    total_revenue_change = sum(revenue_changes)
    average_revenue_change = int(total_revenue_change/month_count)
    max_change = max(revenue_changes)
    min_change = min(revenue_changes)
    max_month_index = revenue_changes.index(max_change)
    min_month_index = revenue_changes.index(min_change)
    max_month = month[max_month_index]
    min_month = month[min_month_index]

    # print analysis
    print(f" Financial Analysis: ")

    print("------------------------------------------------------------")

    print(f"Total Months: {month_count}")
    print(f"Total Revenue: $ {total_revenue} ")
    print(f"Average Change: $ {average_revenue_change} ")    
    print(f"Greatest Increase in Profit: {max_month} {max_change} USD")
    print(f"Greatest Decrease in Profit: {min_month} {min_change} USD")

  
    # name white file
    output_file = csvpath[0:-4]
    write_csvpath = f"{output_file}_pybank_results.text"

    # open write file
    filewriter = open(write_csvpath, mode = 'w')

    # print to writer file
    filewriter.write(f"Financial Analysis:\n")
    filewriter.write("--------------------------------------------------------\n")
    filewriter.write(f"Total Months: {month_count}\n")
    filewriter.write(f"Total Revenue: $ {total_revenue} \n")
    filewriter.write(f"Average Change: $ {average_revenue_change}\n ")    
    filewriter.write(f"Greatest Increase in Profit: {max_month} {max_change} USD\n")
    filewriter.write(f"Greatest Decrease in Profit: {min_month} {min_change} USD\n")

    filewriter.write("")
    filewriter.close()

