from stack import Stack

def stack_test():
    names = Stack()
    names.push("Jack")
    names.push("Jim")
    names.push("Joe")
    names.push("James")
    names.pop()
    print(str(names))
