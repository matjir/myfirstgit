
import csv

csv_file = open('tree.csv')
csv_reader = csv.reader(csv_file, delimiter=',')

# Skip first row if it only contains the column headers
next(csv_reader)
max_height = 0

for row in csv_reader:
    Index, Girth, Height, Volume = row
    if float(Volume) > max_height:
        max_height = float(Volume)

print("Heighest tree was {} meters high.".format(max_height))

csv_file.close()