"""def select_operation(choice):
    if choice == 1:
        return lambda a, b: a + b
    elif choice == 2:
        return lambda a, b: a - b
    else:
        return lambda a, b: a * b


operation = select_operation(1)  # operation = sum
#print(select_operation(1))
print(operation(10, 6))  # 16

operation = select_operation(2)  # operation = subtract
print(operation(10, 6))  # 4

operation = select_operation(3)  # operation = multiply
print(operation(10, 6))  # 60
"""


def select_case(choice):
    if choice <= 1:
        return lambda a, b: a * b
    if 1 < choice <= 10:
        return lambda a, b, c: a + b**c
    if choice > 10:
        return lambda a: a**a


case1 = select_case(-12)
print(case1(34, 12))
case2 = select_case(14)
print(case2(4))

