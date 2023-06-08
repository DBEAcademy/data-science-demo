import csv

rows = [ ["x","y"],["z","v"]]
with open('myfile.csv', 'w', newline='') as file:
  mywriter = csv.writer(file, delimiter=',')
  mywriter.writerows(rows)
  mywriter.writerow(["ZZ", "FF"])
