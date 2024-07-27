# الفئة الأساسية
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# الفئة الفرعية ترث من الفئة الأساسية
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# إنشاء كائن من الفئة الفرعية
dog = Dog("Buddy")
print(dog.speak())  # يطبع: Buddy says Woof!

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# إنشاء كائنات من فئات مختلفة
animals = [Dog("Buddy"), Cat("Whiskers")]

for animal in animals:
    print(animal.speak())
# يطبع:
# Buddy says Woof!
# Whiskers says Meow!


class Person :
    def __init__(self , name , age ):
        self._name = name 
        self._age = age 
    def get_info(self):
        return f"Name : {self._name} , Age :{self._age}"

person = Person("MaHmoud shaker " , 24 )

print(person.get_info())

