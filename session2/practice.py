
'''
    this methid will print a triangle based on input n like:

    *
    **
    ***
    ****
    *****
    ******
'''

def print_triangle(n):
    for i in range(1, n + 1):
        line = ""
        for j in range(i):
            line += "*"
        print(line)

def print_triangle_improved(n):
    for i in range(1, n + 1):
        print("*" * i)

# print_triangle(20)
print_triangle_improved(20)



'''
    this methid will print a upside down triangle 
    based on input n like:

    ******
    *****
    ****
    ***
    **
    *    
'''

def print_upside_down_triangle(n):
    pass

