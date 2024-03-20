import pytest
import input
def test_read_csv_is_list():
    result = input.read_csv()
    assert isinstance(result,list), "Error this isn't a LIST"
    
def test_read_csv_no_duplicates():
    result = input.read_csv()
    assert len(result) == len(set([x[0] for x in result])), "List has duplicate elements"

def test_read_csv_removes_blank_line():
    result = input.read_csv()
    assert all(all(x) for x in result), "List has BLANKS"

def test_user_name_is_capitalised():
    result = input.read_csv()
    assert all(x[1] == x[1].capitalize() for x in result), "Did not capitalise first name"
    assert all(x[2] == x[2].capitalize() for x in result), "Did not capitalise second name"

def test_read_csv_excludes_invalid_last_answer():
    result = input.read_csv()
    assert all(int(x[5]) >= 1 and int(x[5]) <= 10 for x in result), "Result contains invalid third answers"