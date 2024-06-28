def decor_func(func):

    def inner():
        print("I got decorated")
        func()
    return inner


@decor_func
def test_func():
    print("a test function")


test_func()
# decorated_function = decor_func(test_func)
# decorated_function()
