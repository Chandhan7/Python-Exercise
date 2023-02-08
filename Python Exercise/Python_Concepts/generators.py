def generator_function():
    yield "yield1"
    yield "yield2"


def square_function(number):
    """ Finding the square of numbers """
    for element in range(number + 1):
        square = element * element
        yield square


variable_1 = generator_function()
print(next(variable_1))
print(next(variable_1))

variable_2 = square_function(5)
print(square_function.__doc__)
for value in variable_2:
    print(value)
