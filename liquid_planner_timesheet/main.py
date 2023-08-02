import csv
from datetime import date
from pathlib import Path
from timesheet_lists import *

today = date.today()


def read_export_file(export_file):
    """Read LiquidPlanner export file into a list"""
    lp_export_list = []
    with open(export_file, encoding='utf-8-sig') as lp_export_file:
        time_entries_dict = csv.DictReader(lp_export_file)
        for row in time_entries_dict:
            lp_export_list.append(dict(row))
    return lp_export_list


def write_westerville_file():
    """Write the Westerville import file if the westerville_import_list contains entries"""
    wv_filename = f"LiquidPlannerTimesheetReadyForUpload{today.year}-{today.month}-{today.day}-WE.csv"
    wv_file = Path.home()/'Downloads'/wv_filename
    if len(westerville_import_list) > 0:
        with open(wv_file, 'w', newline='') as westerville_import_csv:
            log_writer = csv.DictWriter(westerville_import_csv, fieldnames=import_fields)

            log_writer.writeheader()
            for entry in westerville_import_list:
                log_writer.writerow(entry)


def write_woburn_file():
    """Write the Woburn import file if the woburn_import_list contains entries"""
    wn_filename = f"LiquidPlannerTimesheetReadyForUpload{today.year}-{today.month}-{today.day}-WN.csv"
    wn_file = Path.home()/'Downloads'/wn_filename
    if len(woburn_import_list) > 0:
        with open(wn_file, 'w', newline='') as woburn_import_csv:
            log_writer = csv.DictWriter(woburn_import_csv, fieldnames=import_fields)

            log_writer.writeheader()
            for entry in woburn_import_list:
                log_writer.writerow(entry)


if __name__ == '__main__':
    # Read and verify the LP export file
    export_file_name = input('Enter the LiquidPlanner export file name: ')
    export_file = Path.home()/'Downloads'/export_file_name

    export_list = read_export_file(export_file)
    export_list_error = verify_export_fields(export_list)

    if not export_list_error:
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
