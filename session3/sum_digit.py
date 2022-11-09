
def sum_digit_using_str(d):
    sum = 0
    for i in str(d):
        sum += int(i)
    return sum

# print(sum_digit_using_str(555))


'''
    abc = a*100 + b*10 + c
    abc / 10 = (ab, c)
    ab / 10 = (a, b)
    a / 10 = (0, a)
'''
def sum_digit_using_math(d):
    pass

# print(sum_digit_using_math(555))



