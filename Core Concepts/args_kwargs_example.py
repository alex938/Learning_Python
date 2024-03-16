#*args = tuple
#**kwargs = dictionary

def func3(*args):
    print(args)

func3(1)
func3(1,2)
func3(1,2,3)

def func4(**kwargs):
    print(kwargs)

func4(name="frank", age=19, hungry="yes")

def func5(*args, **kwargs):
    print(args)
    print(kwargs)
    
func5(1, "frank", True, name="john", asleep="yes")