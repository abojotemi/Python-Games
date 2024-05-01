def summation(lst):
    if len(lst) == 1:
        return lst[0]
    lst[1] = lst[0] + lst[1]
    return summation(lst[1:])

lst = [1,2,3]
print(summation(lst))