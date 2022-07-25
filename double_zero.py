# Приклади:
# double_zero([1, 0, 2, 3, 0, 4, 5, 0]) -> [1, 0, 0, 2, 3, 0, 0, 4, 5, 0, 0]
# double_zero([1, 0, 2, 3, 0, 4, 5, 0]) -> [1, 0, 0, 2, 3, 0, 0, 4, 5, 0, 0]
# double_zero([1, 2, 3]) -> [1, 2, 3] """


def double_zero(array):
    array_new = []
    for num in array:
        array_new.append(num)
        if num == 0 in array:
            array_new.append(num)
    return array_new


print(double_zero([1, 0, 2, 3, 0, 4, 5, 0]))
print(double_zero([1, 0, 0, 2, 3, 0, 4, 5, 0]))
print(double_zero([1, 2, 3]))
