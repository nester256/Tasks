import pytest
from main_program import *

test_for_division = [((2, 2), 1), ((6, 3), 2), ((10, 5), 2)]


@pytest.mark.parametrize('test_inp, result', test_for_division)
def test_division(test_inp, result):
    assert division_num(*test_inp) == result

def test_zero_division():
    with pytest.raises(ZeroDivisionError) as error:
        division_num(1, 0)
