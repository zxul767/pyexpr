class Expression:
    @property
    def is_number(self):
        return False

    @property
    def is_variable(self):
        return False

    @property
    def is_product(self):
        return False

    @property
    def is_sum(self):
        return False


class Number(Expression):
    def __init__(self, value):
        self.value = value

    def is_number(self):
        return True

    def __eq__(self, rhs):
        rhs = implicit_cast(rhs)
        if not rhs.is_number:
            return False
        return self.value == rhs.value

    def __add__(self, rhs):
        if self.value == 0:
            return rhs
        rhs = implicit_cast(rhs)
        if rhs.is_number:
            return Number(self.value + rhs.value)
        return Sum(self, rhs)

    def __radd__(self, lhs):
        return self + lhs

    def __mul__(self, rhs):
        if self.value == 0:
            return self
        if self.value == 1:
            return rhs
        rhs = implicit_cast(rhs)
        if rhs.is_number:
            return Number(self.value * rhs.value)
        return Product(self, rhs)

    def __rmul__(self, lhs):
        return self * lhs

    def __repr__(self):
        return f"@{self.value}"


class Variable(Expression):
    def __init__(self, symbol):
        self.symbol = symbol

    @property
    def is_variable(self):
        return True

    def __eq__(self, rhs):
        rhs = implicit_cast(rhs)
        if not rhs.is_variable:
            return False
        return self.symbol == rhs.symbol

    def __add__(self, rhs):
        rhs = implicit_cast(rhs)
        if rhs.is_number:
            return rhs + self
        return Sum(self, rhs)

    def __radd__(self, lhs):
        return self + lhs

    def __mul__(self, rhs):
        rhs = implicit_cast(rhs)
        if rhs.is_number:
            return rhs * self
        return Product(self, rhs)

    def __rmul__(self, lhs):
        return self * lhs

    def __repr__(self):
        return f"{self.symbol}"


class Sum(Expression):
    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend

    @property
    def is_sum(self):
        return True

    def __eq__(self, rhs):
        if not rhs.is_sum:
            return False
        return (self.augend == rhs.augend and self.addend == rhs.addend) or (
            self.augend == rhs.addend and self.addend == rhs.augend
        )

    def __add__(self, rhs):
        rhs = implicit_cast(rhs)
        if rhs.is_number:
            return self.fold_constants(rhs)
        return Sum(self, rhs)

    def __mul__(self, rhs):
        rhs = implicit_cast(rhs)
        if rhs.is_number:
            return rhs * self
        return Product(self, rhs)

    def __rmul__(self, lhs):
        return self * lhs

    def fold_constants(self, addend):
        if self.augend.is_number:
            return Sum(self.augend + addend, self.addend)
        if self.addend.is_number:
            return Sum(self.augend, self.addend + addend)
        return Sum(Number(addend), self)

    def __repr__(self):
        return f"({self.augend} + {self.addend})"


class Product(Expression):
    def __init__(self, multiplicand, multiplier):
        self.multiplicand = multiplicand
        self.multiplier = multiplier

    @property
    def is_product(self):
        return True

    def __add__(self, rhs):
        rhs = implicit_cast(rhs)
        return Sum(self, rhs)

    def __mul__(self, rhs):
        rhs = implicit_cast(rhs)
        if rhs.is_number:
            return self.fold_constants(rhs)
        return Product(self, rhs)

    def __rmul__(self, lhs):
        return self * lhs

    def fold_constants(self, scale):
        if scale.value == 0:
            return scale
        if self.multiplicand.is_number:
            return Product(scale * self.multiplicand, self.multiplier)
        if self.multiplier.is_number:
            return Product(self.multiplicand, scale * self.multiplier)
        return Product(Number(scale), self)

    def __eq__(self, rhs):
        if not rhs.is_product:
            return False
        return (
            self.multiplicand == rhs.multiplicand and self.multiplier == rhs.multiplier
        ) or (
            self.multiplicand == rhs.multiplier and self.multiplier == rhs.multiplicand
        )

    def __repr__(self):
        return f"({self.multiplicand} * {self.multiplier})"


def differentiate(expression, variable):
    expression = implicit_cast(expression)
    variable = implicit_variable_cast(variable)
    if expression.is_number:
        return Number(0)
    if expression.is_variable:
        if expression == variable:
            return Number(1)
        return Number(0)
    if expression.is_sum:
        return differentiate(expression.augend, variable) + differentiate(
            expression.addend, variable
        )
    if expression.is_product:
        return (
            expression.multiplier * differentiate(expression.multiplicand, variable)
            + differentiate(expression.multiplier, variable) * expression.multiplicand
        )
    raise ValueError(f"{expression} is not a supported expression!")


def implicit_cast(expression):
    return implicit_variable_cast(implicit_numeric_cast(expression))


def implicit_numeric_cast(expression):
    return Number(expression) if isinstance(expression, (int, float)) else expression


def implicit_variable_cast(expression):
    return Variable(expression) if isinstance(expression, (str)) else expression
