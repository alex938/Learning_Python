class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def divide(a, b):
        if b == 0:
            return 'Error: Division by zero'
        return a / b

# Usage
print(MathUtils.add(5, 3))        # 8
print(MathUtils.subtract(5, 3))   # 2
print(MathUtils.multiply(5, 3))   # 15
print(MathUtils.divide(5, 3))     # 1.6666666666666667
print(MathUtils.divide(5, 0))     # Error: Division by zero




class Example:
    def __init__(self, value):
        self.value = value

    def instance_method(self):
        return f'Instance method called. Value: {self.value}'

    @classmethod
    def class_method(cls):
        return f'Class method called. Class: {cls.__name__}'

    @staticmethod
    def static_method(param):
        return f'Static method called with parameter: {param}'

# Usage
instance = Example(42)

# Instance method
print(instance.instance_method())  # Instance method called. Value: 42

# Class method
print(Example.class_method())  # Class method called. Class: Example
print(instance.class_method())  # Class method called. Class: Example

# Static method
print(Example.static_method('test'))  # Static method called with parameter: test
print(instance.static_method('test'))  # Static method called with parameter: test
