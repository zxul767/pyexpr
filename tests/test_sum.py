from src.expression import Number, Variable, Sum


def test__can_sum_numbers_and_variables(x):
    assert Number(1) + x == Sum(Number(1), Variable("x"))
    assert x + Number(1) == Sum(Variable("x"), Number(1))


def test__can_do_implicit_numeric_cast_in_sum_expressions(x):
    assert 1 + x == Sum(Number(1), Variable("x"))
    assert x + 1 == Sum(Variable("x"), Number(1))


def test__order_of_terms_should_not_matter_in_sum_comparison(x):
    assert 1 + x == x + 1


def test_can_fold_numbers_in_sum_regardless_of_position(x):
    assert 2 + x + 3 == Sum(Number(5), Variable("x"))


def test__adding_zero_is_no_op(x):
    assert 0 + x == Variable("x")
    assert x + 0 == Variable("x")
