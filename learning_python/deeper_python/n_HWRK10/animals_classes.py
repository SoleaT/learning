
class Animal:

    def __init__(self, species: str, age: float, voice: str = None, name=None):
        self.species = species
        self.age = age
        self.name = name
        self.voice = voice if voice else 'This species is voiceless'

    def make_sound(self):
        print(self.voice)

    def __str__(self, add_str: str = ''):
        return f"""{"-" * 3}Info: exemplar of {self.__class__.__name__}{"-" * 6}
{self.species} {self.name} {self.age} years old
{add_str}
{'_'.rjust(40, '_')}\n"""


class Bird(Animal):

    def __init__(self, species, weight: int, age, voice, name=None):  # а надо ли тип переменных у подкласса указывать?
        super().__init__(species, age, voice, name)
        self.weight = weight

    def check_weight(self):
        return f'This bird weights {self.weight}g'

    def __str__(self, **kwargs):
        return super().__str__(self.check_weight())


class Lizard(Animal):

    def __init__(self, species, color: str, age, name):
        super().__init__(species, age, None, name)
        self.color = color

    def __str__(self, **kwargs):
        return super().__str__(f"It's colored with {self.color} color")


class Dog(Animal):

    def __init__(self, species, breed: str, age, voice, name):
        super().__init__(species, age, voice, name)
        self.breed = breed

    def __str__(self, **kwargs):
        return super().__str__(f"Breed: {self.breed}")


class AnimalExemplar:

    def __new__(cls, animal_type, *args, **kwargs) -> [Lizard, Dog, Bird]:  # клепаем только 3 вида
        try:
            animal = super().__new__(animal_type)
            animal.__init__(*args, **kwargs)
            return animal
        except Exception as e:
            print(f'{e.__class__.__name__} {e}')


firebird = AnimalExemplar(Bird, species='Phoenix', weight=300, age=10, voice="arrr", name="Al'ar")
dragon = AnimalExemplar(Lizard, species='Dragon', color='Black', age=3100, name='Deathswing')
hound = AnimalExemplar(Dog, species='Cerberus', age=12, breed='Corehound', name='', voice='Woof')
wow_bestiary = [firebird, dragon, hound]
print(*wow_bestiary)
firebird.make_sound()
