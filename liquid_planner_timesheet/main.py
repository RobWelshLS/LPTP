import csv
from datetime import date
from pathlib import Path
from tkinter import filedialog
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
    if len(westerville_import_list) > 0:
        wv_file = filedialog.asksaveasfilename(
            initialdir=r"\\chewie\lakeshore\Product Development\1_Post\LiquidPlanner Timesheet Export\Accounting",
            initialfile=f"LiquidPlannerTimesheetReadyForUpload{today.year}-"
                        f"{today.month}-{today.day}-WE",
            title='Write Westerville import file',
            filetypes=(('csv files', '*.csv'), ('all files', '*.*')),
            defaultextension='csv')
        if wv_file:
            with open(wv_file, 'w', newline='') as westerville_import_csv:
                log_writer = csv.DictWriter(westerville_import_csv, fieldnames=import_fields)

                log_writer.writeheader()
                for entry in westerville_import_list:
                    log_writer.writerow(entry)


def write_woburn_file():
    """Write the Woburn import file if the woburn_import_list contains entries"""
    if len(woburn_import_list) > 0:
        wn_file = filedialog.asksaveasfilename(
            initialdir=r"\\chewie\lakeshore\Product Development\1_Post\LiquidPlanner Timesheet Export\Accounting",
            initialfile=f"LiquidPlannerTimesheetReadyForUpload{today.year}-"
                        f"{today.month}-{today.day}-WN",
            title='Write Woburn import file',
            filetypes=(('csv files', '*.csv'), ('all files', '*.*')),
            defaultextension='csv')
        if wn_file:
            with open(wn_file, 'w', newline='') as woburn_import_csv:
                log_writer = csv.DictWriter(woburn_import_csv, fieldnames=import_fields)

                log_writer.writeheader()
                for entry in woburn_import_list:
                    log_writer.writerow(entry)


if __name__ == '__main__':
    # Open file dialog, read and verify the LP export file
    lp_export_file = filedialog.askopenfilename(initialdir=Path.home() / 'Downloads',
                                                title='Select LiquidPlanner timesheet export file',
                                                filetypes=(('csv files', '*.csv'), ('all files', '*.*')))
    if lp_export_file:
        export_list = read_export_file(lp_export_file)
        export_list_error = verify_export_fields(export_list)
    else:
        export_list_error = True

    if not export_list_error:
        # Create the import lists
        import_lists = create_import_lists(export_list)
        westerville_import_list = import_lists[0]
        woburn_import_list = import_lists[1]

        # Create the import files
        write_westerville_file()
        write_woburn_file()
