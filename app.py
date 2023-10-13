# app.py

"""
Це модуль для виконання деякої функціональності.
"""

# Решта коду вашого модуля

def add_numbers(a, b):
    """
    Додає два числа і повертає результат.

    :param a: Перше число.
    :param b: Друге число.
    :return: Сума чисел a і b.
    """
    return a + b

if __name__ == "__main__":
    A = 5
    B = 3
    RESULT = add_numbers(A, B)
    print(f"The sum of {A} and {B} is {RESULT}")
