class Tamagochi:
    def __init__(self, name):
        self.name = name
        self.hunger = 100
        self.happiness = 100
        self.energy = 100
        self.cleanliness = 100
        self.bathroom = 0

    def status(self):
        print(f"{self.name}:\n Сытость: {self.hunger}\n Радость: {self.happiness}\n Бодрость: {self.energy}\n Чистота: {self.cleanliness}\n Нужда: {self.bathroom}")

    def feed(self):
        if self.hunger < 100:
            self.hunger = min(100, self.hunger + 30)
            self.bathroom += 20
            self.energy += 5
            self.happiness += 10
            print(f"{self.name} поел(а).\n Сытость = {self.hunger}\n Нужда = {self.bathroom}\n Бодрость = {self.energy}\n Счастье = {self.happiness}")
        else:
            print(f"{self.name} не голод(ен/на)")

    def play(self):
        if self.energy > 20:
            self.happiness = min(100, self.happiness + 20)
            self.energy -= 20
            self.bathroom += 10
            self.hunger -= 10
            print(f"{self.name} поиграл(а)\n Счастье = {self.happiness}\n Бодрость = {self.energy}\n Нужда = {self.bathroom}\n Сытость =  {self.hunger}")
        else:
            print(f"{self.name} устал(а)")


    def sleep(self):
        if self.energy < 100:
            self.energy = min(100, self.energy + 30)
