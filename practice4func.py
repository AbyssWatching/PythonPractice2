def max_num(a,b,c):
    return max(a,b,c)

def mult_list(lst):

    if len(lst) == 0:
        return 0

    answer = lst[0]

    if len(lst) > 1:
        for element in lst [1:]:
            answer *= element
    return answer

def rev_string(rev):
    return rev[::-1]


print(max_num(1,2,3))
print(mult_list([]))
print(mult_list([1,5,5]))
print(rev_string("apple"))