from classes import Animal
from classes import Elephant
from classes import Cat


elephant = Elephant('Benjamin')
cat = Cat('Behemoth')


def make_sound(animal: Animal):
    print(animal.speak())


make_sound(elephant)
make_sound(cat)