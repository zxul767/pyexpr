from src.expression import Number, differentiate


def test__derivative_of_constant_is_zero(x):
    assert differentiate(1, "x") == Number(0)
    assert differentiate("x", "y") == Number(0)


def test__derivative_of_x_is_one(x):
    assert differentiate(x, x) == Number(1)


def test__derivative_of_constant_product_is_constant(x, y):
    assert differentiate(2 * x, x) == Number(2)
    assert differentiate(x * y, x) == y


def test__derivative_of_sum_is_sum_of_derivatives(x):
    assert differentiate(2 + x + 2 * x, x) == Number(3)


def test__can_differentiate_sums_and_products_recursively(x):
    result = differentiate((2 * x * x) + x * (x + 1), x)

    # TODO: implement simple simplification of expressions (e.g., to collect together same-order terms)
    assert result == (2 * x + 2 * x) + (1 + x + x)
