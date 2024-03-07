import pytest
import input
def test_read_csv():
    result = input.read_csv()
    assert isinstance(result,list), "Error this isn't a LIST"
     
