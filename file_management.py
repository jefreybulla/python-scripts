# File management

import os
import csv

#curent dir
print(os.getcwd())

# list files
os.listdir()


with open('people.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


# Write to file
'''
with open('protagonist.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Movie", "Protagonist"])
    writer.writerow([1, "Lord of the Rings", "Frodo Baggins"])
    writer.writerow([2, "Harry Potter", "Harry Potter"])
'''

# more examples: https://www.programiz.com/python-programming/csv