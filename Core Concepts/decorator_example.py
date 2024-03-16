def star(func):
    def add_stars(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return add_stars

@star
def printer(msg):
    print(msg)

printer("Hello Frank")