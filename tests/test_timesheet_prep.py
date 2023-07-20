import sys

import pytest

sys.path.append('..')
from timesheet_prep import *


def read_import_compare_file(compare_file):
    import_compare = []
    with open(compare_file, encoding='utf-8-sig') as compare_csv_file:
        time_entries_dict = csv.DictReader(compare_csv_file)
        for row in time_entries_dict:
            import_compare.append(dict(row))
    return import_compare


def test_create_import_lists_all():
    """Provide an export list that contains full time and intern employees from both Westerville and
    Woburn. Verify both import lists are created and correct"""
    export_list_all = read_export_file('LP_Export_Test_All.csv')
    import_lists = create_import_lists(export_list_all)

    import_compare_list_wv_all = read_import_compare_file('LP_Import_Test_WV_All.csv')
    import_compare_list_wn_all = read_import_compare_file('LP_Import_Test_WN_All.csv')

    assert import_lists[0] == import_compare_list_wv_all
    assert import_lists[1] == import_compare_list_wn_all


def test_create_import_lists_wv_ft():
    """Provide an export list that contains full time employees from Westerville only. Verify WV
    import list is created and correct. Verify WB import list is empty"""
    export_list_wv_ft = read_export_file('LP_Export_Test_WV_FT.csv')
    import_lists = create_import_lists(export_list_wv_ft)

    import_compare_list_wv_ft = read_import_compare_file('LP_Import_Test_WV_FT.csv')

    assert import_lists[0] == import_compare_list_wv_ft
    assert import_lists[1] == []


def test_create_import_lists_wv_intern():
    """Provide an export list that contains intern employees from Westerville only. Verify WV import
    list is created and correct. Verify WB import list is empty"""
    export_list_wv_intern = read_export_file('LP_Export_Test_WV_Intern.csv')
    import_lists = create_import_lists(export_list_wv_intern)

    import_compare_list_wv_intern = read_import_compare_file('LP_Import_Test_WV_Intern.csv')

    assert import_lists[0] == import_compare_list_wv_intern
    assert import_lists[1] == []


def test_create_import_lists_wn_ft():
    """Provide an export list that contains full time employees from Woburn only. Verify WN import
     list is created and correct. Verify WV import list is empty"""
    export_list_wn_ft = read_export_file('LP_Export_Test_WN_FT.csv')
    import_lists = create_import_lists(export_list_wn_ft)

    import_compare_list_wn_ft = read_import_compare_file('LP_Import_Test_WN_FT.csv')

    assert import_lists[0] == []
    assert import_lists[1] == import_compare_list_wn_ft


def test_create_import_lists_wn_intern():
    """Provide an export list that contains intern employees from Woburn only. Verify WN import
    list is created and correct. Verify WV import list is empty"""
    export_list_wn_intern = read_export_file('LP_Export_Test_WN_Intern.csv')
    import_lists = create_import_lists(export_list_wn_intern)

    import_compare_list_wn_intern = read_import_compare_file('LP_Import_Test_WN_Intern.csv')

    assert import_lists[0] == []
    assert import_lists[1] == import_compare_list_wn_intern


def test_create_import_lists_all_rearranged():
    """Same as test_create_import_lists_all, except the LP export list is rearranged to move columns
     and remove/add various columns that are not included in the import. This simulates custom project
      fields being added in LP and included as part of the export"""
    export_list_all = read_export_file('LP_Export_Test_All_Rearranged.csv')
    import_lists = create_import_lists(export_list_all)

    import_compare_list_wv_all = read_import_compare_file('LP_Import_Test_WV_All.csv')
    import_compare_list_wn_all = read_import_compare_file('LP_Import_Test_WN_All.csv')

    assert import_lists[0] == import_compare_list_wv_all
    assert import_lists[1] == import_compare_list_wn_all


def test_export_field_verification():
    """Test to confirm the verify_export_fields function raises an exception if required fields are missing"""
    export_list_missing_fields = read_export_file('LP_Export_Test_Missing_Fields.csv')  # need to create this file
    with pytest.raises(KeyError) as exc_info:
        verify_export_fields(export_list_missing_fields)
    expected = 'The LiquidPlanner export file is missing the Company field!'
    assert expected in str(exc_info.value)



