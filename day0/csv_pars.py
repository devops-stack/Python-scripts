import csv
f = open("file.csv")
#instance of CSV reader class
csv_f = csv.reader(f)

for row in csv_f:
    name, phone, role = row
    print("Name {}, Phone {}, Role {}".format(name, phone, role))
f.close()
