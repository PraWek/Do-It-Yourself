# ДЗ 4: функции <, >, <=, >=, =

def less_than(pair):
    head, tail = pair
    arg2 = tail[0]
    if head < arg2:
        return 1
    return ()

def greater_than(pair):
    head, tail = pair
    arg2 = tail[0]
    if head > arg2:
        return 1
    return ()

def less_or_equal(pair):
    head, tail = pair
    arg2 = tail[0]
    if head <= arg2:
        return 1
    return ()

def greater_or_equal(pair):
    head, tail = pair
    arg2 = tail[0]
    if head >= arg2:
        return 1
    return ()

def equal(pair):
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
