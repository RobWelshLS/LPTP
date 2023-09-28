# LiquidPlanner Timesheet

The purpose of this app is to convert the timesheet exported from LiquidPlanner into the format required to import the timesheet into Epicor via the Data Management Tool (DMT).

LiquidPlanner exports all time entries in a csv file. The file contains all data needed to import the entries into Epicor. However, the data needs to be modified before it can be imported for the following reasons:
* Most fields need to be renamed and reordered.
* Some fields need to be duplicated.
* Many fields included in the export are not needed and must be deleted.
* The export file contains entries for both Westerville and Woburn users. These need to be separated into two files as they are imported into Epicor separately.

### Features
* The LiquidPlanner export file is verified to contain all required fields.
* The fields in the export file may be in any order. The program will sort them appropriately in the export file(s).
* Any unneeded field in the export file is ignored. This means that custom fields may be added or deleted in LiquidPlanner as needed and they will not affect the conversion operation.
* Separate import files are generated for Westerville and Woburn.
* An import file is not generated if there are no entries for a location. This means the program may be used to generate import files that are as small as a single entry. This is often needed when subsequent imports are required due to corrections or entries made after the initial import.

### Executable creation and installation
Pyinstaller is used to create the executable from the script. To install the Pyinstaller package, run the following command:

```
pip install pyinstaller
```

To create the executable, navigate to \UtilitiesLiquidPlannerTimesheet\liquid_planner_timesheet and run the following command:

```
pyinstaller --onefile --name LPTimesheet main.py
```
This will create the build and dist folders and related files. The LPTimesheet.exe file is found in the dist folder.

To install the executable, simply copy the LPTimesheet.exe file to the desired location on the target computer.
