class Animal:
    def __init__(self, fur: bool) -> None:
        self.__fur: bool = fur
    
    @property
    def has_fur(self) -> bool:
        return self.__fur

class Dog(Animal):
    def __init__(self, name: str, fur: bool) -> None:
        super().__init__(fur)
        self._name: str = name
    
    @staticmethod
    def has_e_in_name(name):
        return ("u" in name.lower())

    @classmethod
    def unknown_dog_name(cls, fur: bool):
        return cls("Unknown Name", fur)

d: Dog = Dog("Jed", True)
e: Dog = Dog.unknown_dog_name(fur=True)

print(d._name)
print(d.has_fur)
print(d.has_e_in_name(d._name))

print(e._name)
print(e.has_fur)
print(e.has_e_in_name(e._name))
