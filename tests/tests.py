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

