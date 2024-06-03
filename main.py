def decor(func):
    def wraps(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("Finish")
        return result
    return wraps


@decor
def say_hi(name):
    print(f"Hello, {name}!")
    return name


result = say_hi("Michael")
print(result)
