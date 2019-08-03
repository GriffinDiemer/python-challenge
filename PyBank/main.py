import os
import csv

average_pl = 0
months = 0
total_pl = 0
change_pl = []
diff = 0
previous_row = 0
greatest_inc = 0
greatest_dec = 0
count = 0
dates = []
budget_csv = os.path.join('budget_data.csv')

with open(budget_csv, newline="") as text:
    reader = csv.reader(text, delimiter =',')
    header = next(reader)


    for row in reader:
        dates.append(row[0])
        total_pl = int(row[1]) + total_pl
        months += 1

        if previous_row != 0:
            diff = int(row[1]) - previous_row
            change_pl.append(diff)
        previous_row = int(row[1])

    average_pl = sum(change_pl)/len(change_pl)

    for i in change_pl:
        if i > greatest_inc:
            greatest_inc = i

    for j in change_pl:
        if j < greatest_dec:
            greatest_dec = j

    for number in change_pl:
        count = count + 1
        if greatest_inc == number:
            date_inc = count
        if greatest_dec == number:
            date_dec = count
average_pl = round(average_pl, 2)      

result = open("results.txt","w")

output = ["Financial Analysis \n",
    "------------------------------------\n",
    (f"Total Months: {months}\n"),
    (f"Total: ${total_pl}\n"),
    (f"Average Change: ${average_pl}\n"),
    (f"Greatest Increase in Profits: {dates[date_inc]} (${greatest_inc})\n"),
    (f"Greatest Decrease in Profits: {dates[date_dec]} (${greatest_dec})")
    ]

result.writelines(output)
result.close()

result = open("results.txt","r")

print(result.read())

