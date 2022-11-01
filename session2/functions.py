
### defining functions with no arguments

def say_hello():
    print("hello")
    print("bye")
    
#say_hello()


### defining functions with one arguments

def print_info(info):
    print("first name -> " + info["first name"])
    print("last name  -> " + info["last name"])


user1_info = {
    "first name": "Jack",
    "last name": "Black"
}

user2_info = {
    "first name": "Joe",
    "last name": "Brown"
}


# print_info(user1_info)
# print_info(user2_info)


### defining functions with multiple arguments 

def greet_people(first, second, third):
    print("hi " + str(first))
    print("hi " + str(second))
    print("hi " + str(third))

def greet_people_using_arrays(people):
    print("hi " + str(people))


# greet_people("Jack", "Jim", "Joe")
# greet_people_using_arrays(["Jack", "Jim", "Joe"])


### calling functions with parameter names

#greet_people(second="Jack", first="Jim", third="Joe")


### functions with default values

def calculate(int1, int2 = 1):
    print("result: " + str(int1 * int2))

# calculate(int1 = 10)







