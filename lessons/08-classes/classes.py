class Car:
    brand: str
    model: str
    is_driving: bool

    def __init__(self, brand: str, model: str) -> None:
        self.brand = brand
        self.model = model
        self.is_driving = False

    def drive(self):
        print('Printed from instance: ', self)
        # print(f'{self.brand}, model {self.model} is DRIVING!')

    def stop_driving(self):
        self.is_driving = False
        print(f'{self.brand}, model {self.model} is STOPPED!')

    @classmethod
    def new_ford(cls, model: str) -> "Car":
        print('Printed from classmethod: ', cls)
        return Car('Ford', model)


class Dog:
    species: str = 'German shepperd'

    def __init__(self, species: str = '') -> None:
        if species:
            self.species = species


class Animal:
    _name: str

    def __init__(self, name: str) -> None:
        self._name = name

    def speak(self) -> str:
        return f'Animal named {self._name} made a sound'
    
    def calc_weight(self):
        ...
    

class Elephant(Animal):
    def speak(self) -> str:
        return f'Elephant {self._name} made a sound'
    

class AfricanElephant(Elephant):
   ...


class Cat(Animal):
    ...
