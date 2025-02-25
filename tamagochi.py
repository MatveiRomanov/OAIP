class Tamagochi:
    def __init__(self, name):
        self.name = name
        self.hunger = 100
        self.happiness = 100
        self.energy = 100
        self.bathroom = 0

    def status(self):
        print(
            f"{self.name}:\n "
            f"Сытость: {self.hunger}\n "
            f"Радость: {self.happiness}\n "
            f"Бодрость: {self.energy}\n "
            f"Нужда: {self.bathroom}")

    def feed(self):
        if self.hunger < 100:
            self.hunger = min(100, self.hunger + 30)
            self.bathroom += 20
            self.energy += 5
            self.happiness = min(100, self.happiness + 5)
            print(
                f"{self.name} поел(а).\n "
                f"Сытость = {self.hunger}\n "
                f"Нужда = {self.bathroom}\n "
                f"Бодрость = {self.energy}\n "
                f"Счастье = {self.happiness}")
        else:
            print(f"{self.name} не голод(ен/на)")

    def play(self):
        if self.energy > 20:
            self.happiness = min(100, self.happiness + 20)
            self.energy -= 20
            self.bathroom += 10
            self.hunger -= 10
            print(
                f"{self.name} поиграл(а)\n "
                f"Счастье = {self.happiness}\n "
                f"Бодрость = {self.energy}\n "
                f"Нужда = {self.bathroom}\n "
                f"Сытость =  {self.hunger}")
        else:
            print(f"{self.name} устал(а)")

    def sleep(self):
        if self.energy < 100:
            self.energy = min(100, self.energy + 30)
            self.hunger -= 30
            self.happiness = min(100, self.happiness + 5)
            self.bathroom += 10
            print(
                f"{self.name} поспал(а)\n "
                f"Бодрость = {self.energy}\n "
                f"Счастье = {self.happiness}\n "
                f"Нужда = {self.bathroom}\n "
                f"Сытость =  {self.hunger}")
        else:
            print(f"{self.name} не хочет спать")

    def nuzhda(self):
        if self.bathroom > 0:
            self.bathroom = min(100, self.bathroom - self.bathroom)
            print(f"{self.name} сходил(а) в туалет\n"
                  f"Нужда = {self.bathroom}")

        else:
            print(f"{self.name} не испытывает нужду")

    def work(self):
        self.happiness -= self.happiness
        self.energy -= self.energy
        print(f"{self.name} поработал(а) в Осетинских пирогах. Устал и несчастен")
        


    def sleep(self):
        if self.energy < 100:
            self.energy = min(100, self.energy + 30)
