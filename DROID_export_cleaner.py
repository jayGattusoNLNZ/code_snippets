import csv
import os


#### make sure this filename is the same as the one on your system
input_csv_filename = r"thread0.csv"
output_csv_filename = "cleaned_csv.csv"

########### do not edit below this line #################

if not os.path.exists(input_csv_filename):
	quit("Can't find the log file '{}', please check your filename".format(input_csv_filename))

cleaned_csv_data = []

with open(input_csv_filename) as data:
	csv_reader = csv.reader(data)
	for row in csv_reader:
		if row[8] != "Folder":
			cleaned_csv_data.append(row[4:])

headers = cleaned_csv_data[0]
cleaned_csv_data.remove(headers)
cleaned_csv_data.sort()

with open(output_csv_filename, "wb") as data:
	writer = csv.writer(data, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
	writer.writerow(headers)
	for row in cleaned_csv_data:
		writer.writerow(row)