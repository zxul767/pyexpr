from src.expression import Number


def test__can_compare_numbers_for_equality():
    assert Number(1) == Number(1)


def test__can_compare_numbers_for_inequality():
    assert Number(1) != Number(-1)


def test__can_do_implicit_cast_in_equality_comparison():
    assert 1 == Number(1)
    assert Number(1) == 1


def test__can_do_implicit_cast_in_inequality_comparison():
    assert Number(1) != -1
    assert 1 != Number(-1)


def test__can_sum_two_numbers():
    assert Number(1) + Number(2) == Number(3)


def test__sum_should_be_commutative():
    assert Number(1) + Number(2) == Number(2) + Number(1)


def test__can_sum_multiple_numbers():
    assert Number(1) + Number(2) + Number(3) == Number(6)


def test__can_do_implicit_cast_in_simple_sums():
    assert 1 + Number(2) == Number(3)
    assert Number(1) + 2 == Number(3)


def test__can_multiply_two_numbers():
    assert Number(2) * Number(3) == Number(6)


def test__product_of_opposite_signs_should_be_positive():
    assert Number(-1) * Number(-2) == Number(2)


def test__product_of_different_signs_should_be_negative():
    assert Number(-1) * Number(2) == Number(-2)


def test__product_should_be_commutative():
    assert Number(2) * Number(3) == Number(3) * Number(2)


def test__can_multiply_multiple_numbers():
    assert Number(2) * Number(3) * Number(4) == Number(24)


def test__can_do_implicit_cast_in_simple_products():
    assert 2 * Number(2) == Number(4)
    assert Number(2) * 2 == Number(4)
