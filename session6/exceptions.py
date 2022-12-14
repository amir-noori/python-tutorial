
def fn1():
    print("in fn1")
    result = fn2()
    if result is None:
        print("some error down the line!")
    else:
        print(f"result {result}")

def fn2():
    print("in fn2")
    try:
        return fn3()
    except KeyError as e:
        print(f"error: {repr(e)}")
        return None

def fn3():
    print("in fn3")
    return fn4()

def fn4():
    print("in fn4")
    data = {}
    return data["not_exists"]


fn1()

