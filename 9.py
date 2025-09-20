# Create a system where an animal can be both a Mammal and a Bird. Each class defines a method for making a sound, and the animal should inherit both sounds.

class Mammal:
    def sound1(self):
        print("mammal sound")

class Bird:
    def sound2(self):
        print("bird sound")

class animal(Mammal,Bird):
    def sound3(self):
        print("animal is sounding");

a=animal()
a.sound1()
a.sound2()
a.sound3()