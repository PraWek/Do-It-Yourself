# ДЗ 4: функции <, >, <=, >=, =

def check_pair(pair):
    if len(pair) != 2:
        return "Функция принимает ровно два аргумента"

def less_than(pair):
    check_pair(pair)
    head, tail = pair
    arg2 = tail[0]
    if head < arg2:
        return 1
    return ()

def greater_than(pair):
    check_pair(pair)
    head, tail = pair
    arg2 = tail[0]
    if head > arg2:
        return 1
    return ()

def less_or_equal(pair):
    check_pair(pair)
    head, tail = pair
    arg2 = tail[0]
    if head <= arg2:
        return 1
    return ()

def greater_or_equal(pair):
    check_pair(pair)
    head, tail = pair
    arg2 = tail[0]
    if head >= arg2:
        return 1
    return ()

def equal(pair):
    check_pair(pair)
    head, tail = pair
    arg2 = tail[0]
    if head == arg2:
        return 1
    return ()

# Примеры
print(less_than((1, (2, ()))))  # -> 1
print(greater_than((2, (1, ()))))  # -> 1
print(less_or_equal((2, (2, ()))))  # -> 1
print(greater_or_equal((3, (2, ()))))  # -> 1
print(equal((2, (2, ()))))  # -> 1
