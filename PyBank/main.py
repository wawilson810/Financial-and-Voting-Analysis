import os
import csv

#Writing the paths for reading in the csv file as well as writing the txt file with the results respectively

path = "C:\\Users\\wawil\\python-challenge\\PyBank\\"
budget_csv = os.path.join(path, 'Resources','budget_data.csv')
writepath = path + "analysis\\results.txt"

#Opening the csv file to read in the data
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Storing the header row and moving past it to get to the data
    csv_header = next(csvreader)

    #Initializing lists to store the months and profits as well as the net profit as 0
    months = []
    net_prof = 0
    prof = []

    #Reading in each row of data
    for row in csvreader:
        #Adding each month to the proper list as well as adding the profit from that month to the total
        months.append(row[0])
        net_prof+= float(row[1])

        #Testing if we are reading in the first row. If true, we store the profit as the previous month's profit.
        #If it is a row after the first, we subtract the previous month's profit from the current month's to get the change and then store that month's as the previous for the next loop
        if len(months) == 1:
            prev_prof = float(row[1])
        else:
            prof.append(float(row[1])-prev_prof)
            prev_prof = float(row[1])

    #Calculating the average change in profit, the maximum change and the minimum.
    avg_prof = sum(prof)/len(prof)
    max_prof = max(prof)
    min_prof = min(prof)

    #Looping through the list of changes in profit to determine the index of the maximum and minimum to store the values to display which month they occured in
    for i in range(len(prof)):
        if prof[i] == max_prof:
            max_ind = i+1
        elif prof[i] == min_prof:
            min_ind = i+1

    #Printing the results to the terminal
    print("Financial Analysis")
    print("--------------------------")
    print(f"Total Months: {len(months)}")
    print(f"Total: ${net_prof}")
    #Formatting the changes in profit in a way that matches the desired output
    print(f"Average Change: ${round(avg_prof, 2)}")
    print(f"Greatest Increase in Profits: {months[max_ind]} (${int(max_prof)})")
    print(f"Greatest Decrease in Profits: {months[min_ind]} (${int(min_prof)})")

#Exporting what was displayed in the terminal to a txt file in the analysis folder
with open(writepath, "w") as file:
    lines = ["Financial Analysis", "--------------------------", f"Total Months: {len(months)}", f"Total: ${net_prof}",
    f"Average Change: ${round(avg_prof, 2)}", f"Greatest Increase in Profits: {months[max_ind]} (${int(max_prof)})",
    f"Greatest Decrease in Profits: {months[min_ind]} (${int(min_prof)})"]
    file.write('\n'.join(lines))

