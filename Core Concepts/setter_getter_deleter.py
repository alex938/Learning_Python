class Animal():
    def __init__(self, name: str, age: int):
        self.__name: str = name
        self.__age: int = age

    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, value: str) -> str:
        self.__name = value

    @name.deleter
    def name(self) -> None:
        print("Deleting name...")
        self.__name = None  

class Dog(Animal):
    def __init__(self, name: str, age: int, colour: str):
        super().__init__(name, age)
        self.__colour: str = colour

def main() -> None:
    first_dog: Dog = Dog("Ted", 34, "Brown")
    print(first_dog.name)
    first_dog.name = "Roger"
    print(first_dog.name)
    del first_dog.name

if __name__ == '__main__':
    main()
