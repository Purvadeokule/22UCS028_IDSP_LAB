
import csv
from dataclasses import fields
from fileinput import filename
from stat import filemode

file = open('C:\\Honours\\IDSP\\file.csv')
print(file)
csvreader = csv.reader(file)
print(csvreader)

fields = ['name','age','CGPA']

rows = [['Purva','20','8.8'],
        ['Sakshi','19','8.3'],
        ['Revati','20','8.5']]
filename = "file.csv"

# writing to csv file
with open(filename,'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

