import operator
import csv

def take_second(elem):
    return elem[1]

sample = open("myfile.csv", "r")
csv_file = csv.reader(sample, delimiter=",")
sort = sorted(csv_file, key=take_second)
print(sort)



