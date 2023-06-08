import csv

lp_export = []

with open('Sample LP export.csv') as time_entries_file:
    time_entries_dict = csv.DictReader(time_entries_file)
    for row in time_entries_dict:
        lp_export.append(row)

print(lp_export)
