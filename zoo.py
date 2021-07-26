class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_lion(self, name):
        self.animals.append( Lion(name) )
    def add_tiger(self, name):
        self.animals.append( Tiger(name) )
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()


class Animal:
    def __init__(self, animal_name, animal_age=0, level_health=0, level_happy=0):
        self.name   = animal_name
        self.age    = animal_age
        self.health = level_health
        self.happy  = level_happy

    def add_animal(self, name):
        self.animals.append(name)
    
    def display_info(self):
        print("Nombre animal:", self.name)
        print("Nivel salud:", self.health)
        print("Nivel felicidad", self.happy)
    
    def up_happy(self):
        self.happy = self.happy + 10
    
    def up_health(self):
        self.health = self.health + 10

class Lion(Animal):
    def __init__(self, animal_name, animal_age=1, level_health=5, level_happy=6):
        super().__init__(animal_name, animal_age, level_health, level_happy)

class Oso(Animal):
    def __init__(self, animal_name, animal_age, level_health, level_happy):
        super().__init__(animal_name, animal_age, level_health, level_happy)

    def up_happy(self):
        self.happy = self.happy + 20
    
    def up_health(self):
        self.health = self.health + 20


class Tiger(Animal):
    def __init__(self, animal_name, animal_age=0, level_health=15, level_happy=15):
        super().__init__(animal_name, animal_age, level_health, level_happy)
    def up_happy(self):
        self.happy = self.happy + 15
    
    def up_health(self):
        self.health = self.health + 15

"""
leon1 = Lion("juanito", 29,100,100)
oso1 = Oso("pepito",10,100,100)
leon1.display_info()
leon1.up_happy()
leon1.display_info()
print("########################################3")
oso1.display_info()
oso1.up_happy()
oso1.display_info()

print("-------------------------------------------------")
tigre1 = Tiger("tontin")
tigre1.display_info()

"""
zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala")
zoo1.add_lion("Simba")
zoo1.add_tiger("Rajah")
zoo1.add_tiger("Shere Khan")
zoo1.print_all_info()



    

