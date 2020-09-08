from src.expression import Variable, Sum, Product


def test__can_compare_for_equality():
    assert Variable("x") == Variable("x")


def test__can_compare_for_inequality():
    assert Variable("x") != Variable("y")


def test__can_do_implicit_cast_in_equality_comparison():
    assert "x" == Variable("x")
    assert Variable("x") == "x"


def test__can_do_implicit_cast_in_inequality_comparison():
    assert "x" != Variable("y")
    assert Variable("y") != "x"


def test__can_sum_two_variables():
    assert Variable("x") + Variable("x") == Sum(Variable("x"), Variable("x"))


def test__can_sum_two_distinct_variables():
    assert Variable("x") + Variable("y") == Sum(Variable("x"), Variable("y"))


def test__can_sum_two_variables_with_implicit_cast():
    assert Variable("x") + "x" == Sum(Variable("x"), Variable("x"))
    assert "x" + Variable("x") == Sum(Variable("x"), Variable("x"))


def test__can_multiply_two_variables():
    assert Variable("x") * Variable("x") == Product(Variable("x"), Variable("x"))


def test__can_multiply_two_distinct_variables():
    assert Variable("x") * Variable("y") == Product(Variable("x"), Variable("y"))


def test__can_multiply_two_variables_with_implicit_cast():
    assert "x" * Variable("x") == Product(Variable("x"), Variable("x"))
    assert Variable("x") * "x" == Product(Variable("x"), Variable("x"))
