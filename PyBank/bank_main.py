import os
import csv

bank_file = os.path.join("Resources", "budget_data.csv")
output_path = os.path.join("Resources", "output")

profit = 0
losses = 0
tot_profit = 0
num_months = 0
row_values = []
running_avg = []
avg_change = 0
i = 0

with open(bank_file, newline ='', encoding = "UTF-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_reader)
    #print(f"Header:{csv_header}")

    for row in csv_reader:
        num_months += 1
        row_values = row_values + [float(row[1])]
        if (float(row[1]) >= 0):
            profit = profit + float(row[1])
            
        elif (float(row[1])<0):
            losses = losses + float(row[1])

    for i in range(1, len(row_values)-1):
        avg_change = float((row_values[i] - row_values[i+1]))
        running_avg = running_avg + [avg_change]
        avg_change = 0

#AVG chnage is actually the running change!!!
#print(str(profit)) ##for reference
#print(str(losses)) ##for reference

tot_profit = profit + losses
print("Financial Analysis:")
print("---------------------")
print("Total Months: " + str(num_months))
print("Total " + str(tot_profit))

#print(row_values) ##for reference
#print(running_avg) ##for reference
A = str(float(sum(running_avg)/len(running_avg)))
print("Average Change: " + A)
print("Greatest Increase in Profits: (" + str(max(running_avg)) + ")")
print("Greatest Decrease in Profits: (" + str(min(running_avg)) + ")")

with open(output_path, 'w', newline ='') as csv_file:
    csv_writer csv.writer(csv_file, delimiter = ',')
    csv_writer.writer(['Financial Analysis'])
    csv_writer.writer(['Total Months ', str(num_months)])
    csv_writer.writer(['Total ', str(tot_profit)])
    csv_writer.writer(['Average Change', A])
    csv_writer.writer(['Greatest Increase in Profits', str(max(running_avg))])
    csv_writer.writer(['Greatest Decrease in Profits', str(min(running_avg))])