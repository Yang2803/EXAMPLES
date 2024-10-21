class Animal:
    def sound(self):
        return "sound"
class Dog(Animal):
    def sound(self):
        return "Gau"
    
animal = Animal()
dog=Dog()

print(animal.sound())
print(dog.sound())

