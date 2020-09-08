from src.expression import Number, Variable, Sum


def test__can_sum_numbers_and_variables():
    assert Number(1) + Variable("x") == Sum(Number(1), Variable("x"))
    assert Variable("x") + Number(1) == Sum(Variable("x"), Number(1))


def test__can_do_implicit_numeric_cast_in_sum_expressions():
    assert 1 + Variable("x") == Sum(Number(1), Variable("x"))
    assert Variable("x") + 1 == Sum(Variable("x"), Number(1))


def test__order_of_terms_should_not_matter_in_sum_comparison():
    assert Number(1) + Variable("x") == Variable("x") + Number(1)


def test_can_fold_numbers_in_sum_regardless_of_position():
    assert Number(2) + Variable("x") + Number(3) == Sum(Number(5), Variable("x"))
    assert 2 + Variable("x") + 3 == Sum(Number(5), Variable("x"))


def test__adding_zero_is_no_op():
    assert 0 + Variable("x") == Variable("x")
    assert Variable("x") + 0 == Variable("x")
