import sys

sys.path.append('../LPTP')
from timesheet_prep import *

export_list_both = []
export_list_westerville = []
export_list_woburn = []
export_list_both_modified = []

import_list_westerville = []
import_list_woburn = []


def test_create_import_lists():
    pass


"""
Tests for the create_import_lists function:

1. Provide export file in expected format with entries from both Westerville and 
Woburn and confirm Westerville and Woburn import lists have all import data.

2. Provide export file in expected format with entries from just Westerville full time and 
confirm Westerville import list has all import data and Woburn list is empty.

3. Repeat test 2 but with entries from just Westerville interns.

4. Repeat test 2 but with entries from just Woburn full time.

5. Repeat test 2 but with entries from just Woburn interns.

6. Repeat test 1, but rearrange entries in export file and confirm import data is
still correct.

5. Add error handling that confirms the export file contains all required fields.
Write test with missing fields to ensure error handling catches error.

"""



"""
Git notes
Branching:
	• Create new branch: git branch <branch name>
	• Checkout branch: git checkout <branch name>
	• After changes are made in new branch, add and commit changed files and the branches will now be different.
	• Merge branch to main: git merge <branch name>
	• Merge conflicts can be resolved in PyCharm by going to Git -> Remote -> Resolve Conflicts. Click on Merge for guidance on changes.

Working with branches on remote repositories:
	• To show if local is out of date: git remote show origin
	• Get data I don't have yet (but not merge): git fetch origin
		○ After running fetch, differences can be seen by running: git status
	• Merge changes after running fetch: git pull
	• Show all branches on origin: git branch -a
	• Get a remote branch on local:
		○ git checkout origin/<branch name>
		○ git checkout <branch name>

Typical workflow with branches and a remote repository:
	1. Create branch
	2. Checkout branch and make changes
	3. Add and commit changes
	4. Push branch to remote repo: git push origin <branch>
	5. When ready to merge changes into main: In remote repository, create a pull request to merge the branch into main
	6. Merge pull request
	7. Delete branch at remote repository
	8. Delete local branch: git branch -D <branch name>
	9. To get updated main branch on another local computer/user:
		○ git checkout main
		○ git remote show origin (optional, to verify local is behind origin)
		○ git fetch origin
		○ git status (optional, to view differences)
		○ git pull
Use PyCharm to resolve merge conflicts if needed

"""
