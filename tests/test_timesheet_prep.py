import sys
sys.path.append("..")
from timesheet_prep import *


def test_add_two():
    assert add_two(3, 5) == 8
