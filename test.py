import csv

Class = ['Pop','Punk']
ID = ['0','1']

with open('employee_file.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            line_count += 1

print(line_count)

with open('employee_file.csv', mode='a') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)


    for i in range(len(Class)):
        employee_writer.writerow([ID[i],Class[i]])