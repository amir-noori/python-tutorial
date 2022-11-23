
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
    if d == 0:
        return 0
    # print("r -> " + str(d % 10) + " v -> " + str(d // 10))
    print(f"r -> {d % 10} v -> {d // 10}")
    return d % 10 + sum_digit_using_math(d // 10)

print(sum_digit_using_math(365))

def sum_digit1(n):
    result = 0
    i = n
    while i != 0:
        m = i % 10
        result += m
        i = (i - m)/10
    return result

def sum_digit2(n):
    mk = len(str(n))
    i=0
    jam = 0
    while i < mk:
        taghsim = n // 10
        baghimandeh = n % 10
        i= i+1
        jam = jam + baghimandeh    
        n = taghsim

    return jam


# print(sum_digit_using_math(555))



