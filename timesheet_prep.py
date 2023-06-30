import csv

lp_export = []

with open('Sample LP export.csv', encoding='utf-8-sig') as lp_export_file:
    time_entries_dict = csv.DictReader(lp_export_file)
    for row in time_entries_dict:
        lp_export.append(row)

new_dict = {}

print(lp_export[0])

new_dict['Company'] = lp_export[0].get('Company')
emp_num = lp_export[0].get('person_reference')
new_dict['EmployeeNum'] = emp_num.split("-")[0]

print(new_dict)

# for k, v in lp_export[0].items():
#     print(f"{k}: {v}")


# Add a line to test git push from home account
