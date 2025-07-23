# Base class
class Person:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation

    def learn(self):
        print(f"{self.name} is learning.")

    def walk(self):
        print(f"{self.name} is walking.")

    def eat(self):
        print(f"{self.name} is eating.")

# Subclass: Programmer
class Programmer(Person):
    def __init__(self, name, designation, companyName):
        super().__init__(name, designation)
        self.companyName = companyName

    def coding(self):
        print(f"{self.name} is coding at {self.companyName}.")

# Subclass: Dancer
class Dancer(Person):
    def __init__(self, name, designation, groupName):
        super().__init__(name, designation)
        self.groupName = groupName

    def dancing(self):
        print(f"{self.name} is dancing in {self.groupName}.")

# Subclass: Singer
class Singer(Person):
    def __init__(self, name, designation, bandName):
        super().__init__(name, designation)
        self.bandName = bandName

    def singing(self):
        print(f"{self.name} is singing in {self.bandName}.")

    def playGuitar(self):
        print(f"{self.name} is playing guitar in {self.bandName}.")

# Creating instances
p = Programmer("Ravi", "Software Engineer", "TCS")
d = Dancer("Neha", "Lead Dancer", "Bollywood Troupe")
s = Singer("Amit", "Vocalist", "RockOn Band")

# Calling their methods
p.learn()
p.coding()

d.walk()
d.dancing()

s.eat()
s.singing()
s.playGuitar()
