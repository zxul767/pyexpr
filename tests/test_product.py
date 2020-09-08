from src.expression import Number, Variable, Product, Sum
from pytest import fixture


def test__can_multiply_numbers_and_variables(x):
    assert Number(2) * x == Product(Number(2), Variable("x"))
    assert x * Number(2) == Product(Variable("x"), Number(2))


def test__can_do_implicit_numeric_cast_in_product_expressions(x):
    assert 2 * x == Product(Number(2), Variable("x"))
    assert x * 2 == Product(Variable("x"), Number(2))


def test__order_of_terms_should_not_matter_in_product_comparison(x):
    assert 2 * x == x * 2


def test__can_fold_numbers_in_product_regardless_of_position(x):
    assert 2 * x * 3 == Product(Number(6), Variable("x"))


def test__multiplying_by_one_is_no_op(x):
    assert 1 * x == Variable("x")
    assert x * 1 == Variable("x")


def test__multiplying_by_zero_is_zero(x):
    assert 0 * x == Number(0)
    assert x * 0 == Number(0)

    assert 0 * (Number(1) * Number(2)) == Number(0)
    assert (Number(1) * Number(2)) * 0 == Number(0)

    assert 0 * (Number(1) + Number(2)) == Number(0)
    assert (Number(1) + Number(2)) * 0 == Number(0)


def test__can_multiply_numbers_and_products(x):
    assert 2 * (x * 1) == Product(Variable("x"), Number(2))
    assert (x * 1) * 2 == Product(Variable("x"), Number(2))


def test__can_multiply_numbers_and_sums(x):
    assert 2 * (x + 1) == Product(Number(2), Sum(Variable("x"), Number(1)))
    assert (x + 1) * 2 == Product(Number(2), Sum(Variable("x"), Number(1)))


def test__can_multiply_products_and_sums(x):
    assert (x + 1) * (2 + x) == Product(
        Sum(Number(1), Variable("x")), Sum(Number(2), Variable("x"))
    )
