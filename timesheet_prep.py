import csv

lp_export = []

# Read LiquidPlanner export file into a list
with open('Sample LP export.csv', encoding='utf-8-sig') as lp_export_file:
    time_entries_dict = csv.DictReader(lp_export_file)
    for row in time_entries_dict:
        lp_export.append(dict(row))

# Define import fields
fields = ['Company', 'EmployeeNum', 'LaborTypePseudo', 'IndirectCode', 'LaborHrs', 'BurdenHrs', 'LaborNote',
          'PayrollDate', 'ProjectID', 'PhaseID', 'ClockInDate', 'PhaseOprSeq', 'TimeStatus', 'OpComplete',
          'ResourceID', 'OkToChangeResourceGrpID']


# Build the Epicor import list(s) from the LiquidPlanner export list
def create_import_lists(export_list):
    westerville_import = []
    woburn_import = []

    for entry in export_list:
        # Create a new dictionary for the entry and initialize variables
        new_dict = {}
        westerville = False
        woburn = False

        # Determine if the entry is for Westerville or Woburn
        if entry.get('team') == 'Westerville Team' or entry.get('team') == 'Westerville Intern Team':
            westerville = True
        elif entry.get('team') == 'Woburn Team' or entry.get('team') == 'Woburn Intern Team':
            woburn = True

        # Split the person_reference field into the employee number and indirect code
        employee_num = entry.get('person_reference').split("-")[0]
        indirect_code = entry.get('person_reference').split("-")[1]

        # Build the import list by setting the appropriate dictionary keys/values
        new_dict[fields[0]] = entry.get('Company')
        new_dict[fields[1]] = employee_num
        new_dict[fields[2]] = entry.get('LaborTypePseudo')
        new_dict[fields[3]] = indirect_code
        new_dict[fields[4]] = entry.get('hours')

        # Report BurdenHrs only if Direct
        if entry.get('LaborTypePseudo') == 'J':
            new_dict[fields[5]] = entry.get('hours')
        else:
            new_dict[fields[5]] = '0'

        new_dict[fields[6]] = entry.get('timesheet_entry_note')
        new_dict[fields[7]] = entry.get('date')
        new_dict[fields[8]] = entry.get('ProjectID')

        # Select either Westerville or Woburn PhaseID
        if westerville:
            new_dict[fields[9]] = entry.get('PhaseID')
        elif woburn:
            new_dict[fields[9]] = entry.get('PhaseID-WN')

        new_dict[fields[10]] = entry.get('date')
        new_dict[fields[11]] = entry.get('activity')
        new_dict[fields[12]] = entry.get('TimeStatus')
        new_dict[fields[13]] = entry.get('OpComplete')
        new_dict[fields[14]] = employee_num
        new_dict[fields[15]] = entry.get('OkToChangeResourceGrpID')

        # If entry is for Westerville, append to Westerville import list. Else, append to Woburn.
        if westerville:
            westerville_import.append(new_dict)
        elif woburn:
            woburn_import.append(new_dict)

    return westerville_import, woburn_import


import_lists = create_import_lists(lp_export)

westerville_import_list = import_lists[0]
woburn_import_list = import_lists[1]

# Test prints, to be deleted
# print(f"\nThis is the Westerville import list. The length is {len(westerville_import_list)} entries:")
# for row in westerville_import_list:
#     print(row)
#
# print(f"\nThis is the Woburn import list: The length is {len(woburn_import_list)} entries:")
# for row in woburn_import_list:
#     print(row)

# Write Westerville import file
if len(westerville_import_list) > 0:
    with open('westerville_import.csv', 'w', newline='') as westerville_import_csv:
        log_writer = csv.DictWriter(westerville_import_csv, fieldnames=fields)

        log_writer.writeheader()
        for entry in westerville_import_list:
            log_writer.writerow(entry)

# Write Woburn import file
if len(woburn_import_list) > 0:
    with open('woburn_import.csv', 'w', newline='') as woburn_import_csv:
        log_writer = csv.DictWriter(woburn_import_csv, fieldnames=fields)

        log_writer.writeheader()
        for entry in woburn_import_list:
            log_writer.writerow(entry)
