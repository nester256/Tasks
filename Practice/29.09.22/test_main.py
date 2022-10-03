import pytest

# from main import add_two, calc_two
from task_for_seminar import *

#
# tests = [(2, 4), (0, 2), (10, 12), (100, 102), (-10, -8)]
#
#
# @pytest.mark.parametrize('test_inp, result', tests)
# def test_addition(test_inp, result):
#     assert add_two(test_inp) == result
#
#
# test_calc = [('2 * 2', 4), ("2 + 2", 4), ("9 / 3", 3), ("9 + 7", 16)]
#
#
# @pytest.mark.parametrize('test_inp, result', test_calc)
# def test_calc(test_inp, result):
#     assert calc_two(test_inp) == result

#
# test_hash = [("привет пока", "#ПриветПока")]
#
#
# @pytest.mark.parametrize('test_inp, result', test_hash)
# def test_hashtag(test_inp, result):
#     assert does_hashtag(test_inp) == result
#
#
# test_remove = [([0, 1, 1, 0], "отчислен"), ([1, 1, 1, 1], "пока живи")]
#
#
# @pytest.mark.parametrize('test_inp, result', test_remove)
# def test_hashtag(test_inp, result):
#     assert removed(test_inp) == result
#
#
# test_NSWE = [(['W', 'E', 'S', 'N'], ['W', 'E', 'S', 'N']), (['W', 'E', 'S'], ['S'])]
#
#
# @pytest.mark.parametrize('test_inp, result', test_NSWE)
# def test_hashtag(test_inp, result):
#     assert go_to_NSWE(test_inp) == result

#Проверка на ошибки! Именно отлов ошибок


@pytest.mark.xfail(ValueError) #Добавляет проверку ошибок
def test_mult_10():
    with pytest.raises(ValueError) as error:
        assert mult_10("hello") == 100