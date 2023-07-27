import csv
from datetime import date

# Read LiquidPlanner export file into a list
def read_export_file(export_file):
    lp_export_list = []
    with open(export_file, encoding='utf-8-sig') as lp_export_file:
        time_entries_dict = csv.DictReader(lp_export_file)
        for row in time_entries_dict:
            lp_export_list.append(dict(row))
    return lp_export_list


def verify_export_fields(export_list):
    """Verify all required fields are present in the export list"""
    export_fields = ['team', 'person_reference', 'Company', 'LaborTypePseudo', 'hours', 'timesheet_entry_note', 'date',
                     'ProjectID', 'PhaseID', 'PhaseID-WN', 'activity', 'TimeStatus', 'OpComplete',
                     'OkToChangeResourceGrpID']

    for field in export_fields:
        try:
            _ = export_list[0][field]
        except KeyError:
            print(f"The LiquidPlanner export file is missing the {field} field!")


# Define import fields
import_fields = ['Company', 'EmployeeNum', 'LaborTypePseudo', 'IndirectCode', 'LaborHrs', 'BurdenHrs', 'LaborNote',
          'PayrollDate', 'ProjectID', 'PhaseID', 'ClockInDate', 'PhaseOprSeq', 'TimeStatus', 'OpComplete',
          'ResourceID', 'OkToChangeResourceGrpID']


def create_import_lists(export_list):
    """Build the Epicor import list(s) from the LiquidPlanner export list"""
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
        new_dict[import_fields[0]] = entry.get('Company')
        new_dict[import_fields[1]] = employee_num
        new_dict[import_fields[2]] = entry.get('LaborTypePseudo')
        new_dict[import_fields[3]] = indirect_code
        new_dict[import_fields[4]] = entry.get('hours')

        # Report BurdenHrs only if entry contains Direct hours
        if entry.get('LaborTypePseudo') == 'J':
            new_dict[import_fields[5]] = entry.get('hours')
        else:
            new_dict[import_fields[5]] = '0'

        new_dict[import_fields[6]] = entry.get('timesheet_entry_note')
        new_dict[import_fields[7]] = entry.get('date')
        new_dict[import_fields[8]] = entry.get('ProjectID')

        # Select either Westerville or Woburn PhaseID
        if westerville:
            new_dict[import_fields[9]] = entry.get('PhaseID')
        elif woburn:
            new_dict[import_fields[9]] = entry.get('PhaseID-WN')

        new_dict[import_fields[10]] = entry.get('date')

        # Report the PhaseOprSeq only if entry contains Direct hours
        if entry.get('LaborTypePseudo') == 'J':
            new_dict[import_fields[11]] = entry.get('activity')
        else:
            new_dict[import_fields[11]] = ""

        new_dict[import_fields[12]] = entry.get('TimeStatus')
        new_dict[import_fields[13]] = entry.get('OpComplete')
        new_dict[import_fields[14]] = employee_num
        new_dict[import_fields[15]] = entry.get('OkToChangeResourceGrpID')

        # If entry is for Westerville, append to Westerville import list. Else, append to Woburn.
        if westerville:
            westerville_import.append(new_dict)
        elif woburn:
            woburn_import.append(new_dict)

    return westerville_import, woburn_import


today = date.today()


def write_westerville_file():
    wv_filename = f"LiquidPlannerTimesheetReadyForUpload{today.year}-{today.month}-{today.day}-WE.csv"
    if len(westerville_import_list) > 0:
        with open(wv_filename, 'w', newline='') as westerville_import_csv:
            log_writer = csv.DictWriter(westerville_import_csv, fieldnames=import_fields)

            log_writer.writeheader()
            for entry in westerville_import_list:
                log_writer.writerow(entry)


# Write Woburn import file
def write_woburn_file():
    wn_filename = f"LiquidPlannerTimesheetReadyForUpload{today.year}-{today.month}-{today.day}-WN.csv"
    if len(woburn_import_list) > 0:
        with open(wn_filename, 'w', newline='') as woburn_import_csv:
            log_writer = csv.DictWriter(woburn_import_csv, fieldnames=import_fields)

            log_writer.writeheader()
            for entry in woburn_import_list:
                log_writer.writerow(entry)


if __name__ == '__main__':
    # Read and verify the LP export file
    export_list = read_export_file('Sample LP export.csv')
    verify_export_fields(export_list)

    # Create the import lists
    import_lists = create_import_lists(export_list)
    westerville_import_list = import_lists[0]
    woburn_import_list = import_lists[1]

    # Create the Epicor import files
    write_westerville_file()
    write_woburn_file()

    # Test prints, to be deleted
    # print(f"\nThis is the Westerville import list. The length is {len(westerville_import_list)} entries:")
    # for row in westerville_import_list:
    #     print(row)
    #
    # print(f"\nThis is the Woburn import list: The length is {len(woburn_import_list)} entries:")
    # for row in woburn_import_list:
    #     print(row)
