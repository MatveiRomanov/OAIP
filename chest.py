import random


class Chest:
    def __init__(self, filling, locked=False):
        self.filling = filling
        self. locked = locked

    def open(self):
        if self.locked:
            print("Сундук заперт")
        else:
            if self.filling:
                item = random.choice(self.filling)
                print(f"Ты нашел {item} в сундуке")
            else:
                print("Сундук пуст")

    def close(self):
        print("Сундук закрыт.")

    def lock_up(self):
        self.locked = True
        print("Сундук заперт")

    def lock_out(self):
        self.locked = False
        print("Замок открыт")

