class Tamagochi:
    def __init__(self, name):
        self.name = name
        self.hunger = 100
        self.happiness = 100
        self.energy = 100
        self.bathroom = 0
        self.alive = True

    def status(self):
        print(
            f"{self.name}:\n "
            f"Сытость: {self.hunger}\n "
            f"Радость: {self.happiness}\n "
            f"Бодрость: {self.energy}\n "
            f"Нужда: {self.bathroom}")

    def death(self):
        if self.hunger <= 0 or self.energy <= 0 or self.happiness < 0 or self.bathroom >= 100:
            self.alive = False
        return not self.alive

    def feed(self):
        if self.death():
            print(f"{self.name} мертв(а)")

        elif self.death == False and self.hunger < 100:
            self.hunger = min(100, self.hunger + 30)
            self.bathroom += 20
            self.energy += 5
            self.happiness = min(100, self.happiness + 5)
            self.status()
        else:
            print(f"{self.name} не голод(ен/на)")

    def play(self):
        if self.death():
            print(f"{self.name} мертв(а)")
        elif self.energy > 20:
            self.happiness = min(100, self.happiness + 20)
            self.energy -= 20
            self.bathroom += 10
            self.hunger -= 10
            self.status()
        else:
            print(f"{self.name} устал(а)")

    def sleep(self):
        if self.death():
            print(f"{self.name} мертв(а)")
        elif self.energy < 100:
            self.energy = min(100, self.energy + 30)
            self.hunger -= 30
            self.happiness = min(100, self.happiness + 5)
            self.bathroom += 10
            self.status()
        else:
            print(f"{self.name} не хочет спать")

    def need(self):
        if self.death():
            print(f"{self.name} мертв(а)")
        elif self.bathroom > 0:
            self.bathroom = min(100, self.bathroom - self.bathroom)
            self.status()
        else:
            print(f"{self.name} не испытывает нужду")

    def work(self):
        if self.death():
            print(f"{self.name} мертв(а)")
        elif self.alive:
            self.happiness = min(100, self.happiness - 50)
            self.energy = min(100, self.energy - 50)
            print(f"{self.name} поработал(а) в Осетинских пирогах. Устал и несчастен")
