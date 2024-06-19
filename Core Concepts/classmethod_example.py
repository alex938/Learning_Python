class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients
    
    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])
    
    @classmethod
    def pepperoni(cls):
        return cls(['mozzarella', 'tomatoes', 'pepperoni'])

margherita_pizza = Pizza.margherita()
pepperoni_pizza = Pizza.pepperoni()

print(margherita_pizza.ingredients)  # ['mozzarella', 'tomatoes']
print(pepperoni_pizza.ingredients)  # ['mozzarella', 'tomatoes', 'pepperoni']





class MyClass:
    class_variable = 'I am a class variable'
    
    def __init__(self, value):
        self.instance_variable = value
    
    @classmethod
    def class_method(cls):
        return f'Class method called. class_variable: {cls.class_variable}'

print(MyClass.class_method())  # Class method called. class_variable: I am a class variable

instance = MyClass('some value')
print(instance.class_method())  # Class method called. class_variable: I am a class variable
