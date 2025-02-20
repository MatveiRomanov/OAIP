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
            print(f"{self.name} поел. Сытость = {self.hunger}\nНужда = {self.bathroom}")
        else:
            print(f"{self.name} не голоден")

    def play(self):
        if self.energy > 20:
            self.happiness = min(100, self.happiness + 20)
            self.energy -= 20
            self.bathroom += 10
            print(f"")