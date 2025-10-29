import random


class Widget:

    def __init__(self, widget_id, styles=None):
        self.widget_id = widget_id
        self.styles = styles or {}
        self.visible = True

    def render(self):
        pass

    def set_style(self, property, value):
        self.styles[property] = value

    def hide(self):
        self.visible = False

    def show(self):
        self.visible = True


class Label(Widget):

    def __init__(self, widget_id, text, font=None):
        super().__init__(widget_id)
        self.text = text
        self.font = font

    def render(self):
        return f"Label[id={self.widget_id}, text='{self.text}']"


class InputWidget(Widget):

    def __init__(self, widget_id, placeholder=""):
        super().__init__(widget_id)
        self.placeholder = placeholder
        self.value = ""

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value


class LineEdit(InputWidget):

    def render(self):
        return f"LineEdit[id={self.widget_id}, value='{self.value}', placeholder='{self.placeholder}']"


class TextEdit(InputWidget):

    def __init__(self, widget_id, placeholder="", rows=3):
        super().__init__(widget_id, placeholder)
        self.rows = rows

    def render(self):
        return f"TextEdit[id={self.widget_id}, rows={self.rows}, value='{self.value}']"


class Button(Widget):

    def __init__(self, widget_id, text, button_type="default"):
        super().__init__(widget_id)
        self.text = text
        self.button_type = button_type
        self.enabled = True

    def render(self):
        status = "enabled" if self.enabled else "disabled"
        return f"Button[id={self.widget_id}, text='{self.text}', type='{self.button_type}', {status}]"

    def click(self):
        if self.enabled:
            return f"Button {self.widget_id} clicked"
        return "Button is disabled"


class CheckBox(Widget):

    def __init__(self, widget_id, label, checked=False):
        super().__init__(widget_id)
        self.label = label
        self.checked = checked

    def render(self):
        status = "checked" if self.checked else "unchecked"
        return f"CheckBox[id={self.widget_id}, label='{self.label}', {status}]"

    def toggle(self):
        self.checked = not self.checked


class RadioButton(Widget):

    def __init__(self, widget_id, label, group_name, selected=False):
        super().__init__(widget_id)
        self.label = label
        self.group_name = group_name
        self.selected = selected

    def render(self):
        status = "selected" if self.selected else "unselected"
        return f"RadioButton[id={self.widget_id}, group='{self.group_name}', label='{self.label}', {status}]"

    def select(self):
        self.selected = True


class Weapon:

    def __init__(self, name, base_damage, weight):
        self.name = name
        self.base_damage = base_damage
        self.weight = weight

    def calculate_damage(self):
        return self.base_damage

    def info(self):
        return f"{self.name} (Урон: {self.base_damage}, Вес: {self.weight})"


class ColdWeapon(Weapon):

    def __init__(self, name, base_damage, weight, weapon_type):
        super().__init__(name, base_damage, weight)
        self.weapon_type = weapon_type  

    def calculate_damage(self):
        return self.base_damage * 1.1

    def info(self):
        return f"Холодное оружие: {super().info()}, Тип: {self.weapon_type}"


class Firearm(Weapon):

    def __init__(self, name, base_damage, weight, ammo_capacity):
        super().__init__(name, base_damage, weight)
        self.ammo_capacity = ammo_capacity
        self.current_ammo = ammo_capacity

    def reload(self):
        self.current_ammo = self.ammo_capacity

    def shoot(self):
        if self.current_ammo > 0:
            self.current_ammo -= 1
            return self.calculate_damage()
        return 0

    def info(self):
        return f"Огнестрельное: {super().info()}, Патроны: {self.current_ammo}/{self.ammo_capacity}"


class Shotgun(Firearm):

    def __init__(self, name, base_damage, weight, ammo_capacity):
        super().__init__(name, base_damage, weight, ammo_capacity)
        self.pellet_count = 8  # количество дробин

    def calculate_damage(self):
        return self.base_damage * 0.8 * self.pellet_count

    def info(self):
        return f"Дробовик: {super().info()}, Дробинок: {self.pellet_count}"


class TetrisGame:

    def __init__(self):
        self.score = 0
        self.level = 1
        self.board = [[0 for _ in range(10)] for _ in range(20)]
        self.current_piece = None
        self.game_over = False

    def start_game(self):
        pass

    def move_piece_left(self):
        pass

    def move_piece_right(self):
        pass

    def rotate_piece(self):
        pass

    def drop_piece(self):
        pass

    def check_lines(self):
        pass


class TetrisPiece:

    def __init__(self):
        self.shape = []
        self.position = [0, 0]
        self.color = None

    def rotate(self):
        pass

    def get_positions(self):
        pass


class IPiece(TetrisPiece):

    def __init__(self):
        super().__init__()
        self.shape = [
            [1, 1, 1, 1]
        ]
        self.color = "cyan"


class LPiece(TetrisPiece):

    def __init__(self):
        super().__init__()
        self.shape = [
            [1, 0],
            [1, 0],
            [1, 1]
        ]
        self.color = "orange"


class OPiece(TetrisPiece):

    def __init__(self):
        super().__init__()
        self.shape = [
            [1, 1],
            [1, 1]
        ]
        self.color = "yellow"


class TPiece(TetrisPiece):

    def __init__(self):
        super().__init__()
        self.shape = [
            [0, 1, 0],
            [1, 1, 1]
        ]
        self.color = "purple"


class Character:

    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack_power = attack_power
        self.level = 1
        self.alive = True

    def attack(self):
        print(f"{self.name} атакует!")

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            self.alive = False
            print(f"{self.name} погиб!")

    def heal(self, amount):
        if self.alive:
            self.hp = min(self.max_hp, self.hp + amount)
            print(f"{self.name} восстановил {amount} HP")

    def info(self):
        status = "жив" if self.alive else "мёртв"
        print(
            f"{self.name} (Уровень {self.level}) - HP: {self.hp}/{self.max_hp}, Атака: {self.attack_power}, Статус: {status}")


class Warrior(Character):

    def __init__(self, name, hp, attack_power):
        super().__init__(name, hp, attack_power)
        self.armor = 10
        self.rage = 0

    def attack(self):
        super().attack()
        print(f"{self.name} наносит удар мечом! Урон: {self.attack_power}")
        self.rage += 10
        return self.attack_power

    def special_ability(self):
        if self.rage >= 50:
            print(f"{self.name} использует ЯРОСТЬ! Урон удвоен!")
            self.rage = 0
            return self.attack_power * 2
        else:
            print(f"Недостаточно ярости! Текущая ярость: {self.rage}/50")
            return 0


class Mage(Character):

    def __init__(self, name, hp, attack_power, mana):
        super().__init__(name, hp, attack_power)
        self.mana = mana
        self.max_mana = mana
        self.spell_power = attack_power * 2

    def attack(self):
        super().attack()
        if self.mana >= 10:
            self.mana -= 10
            print(f"{self.name} бросает огненный шар! Урон: {self.spell_power}, Мана: {self.mana}/{self.max_mana}")
            return self.spell_power
        else:
            print(f"{self.name} атакует посохом! Урон: {self.attack_power}")
            return self.attack_power

    def special_ability(self):
        if self.mana >= 30:
            self.mana -= 30
            heal_amount = 50
            self.heal(heal_amount)
            print(f"{self.name} использует исцеление!")
            return heal_amount
        else:
            print("Недостаточно маны для исцеления!")
            return 0


class Archer(Character):

    def __init__(self, name, hp, attack_power, arrows):
        super().__init__(name, hp, attack_power)
        self.arrows = arrows
        self.critical_chance = 0.2

    def attack(self):
        super().attack()
        if self.arrows > 0:
            self.arrows -= 1
            if random.random() < self.critical_chance:
                damage = self.attack_power * 2
                print(f"{self.name} делает выстрел с дистанции! КРИТИЧЕСКИЙ УРОН: {damage}")
            else:
                damage = self.attack_power
                print(f"{self.name} делает выстрел с дистанции! Урон: {damage}")
            print(f"Стрелы: {self.arrows}")
            return damage
        else:
            print(f"{self.name} атакует кинжалом! Урон: {self.attack_power // 2}")
            return self.attack_power // 2

    def special_ability(self):
        """Особое умение - залп стрел"""
        if self.arrows >= 3:
            self.arrows -= 3
            damage = self.attack_power * 3
            print(f"{self.name} использует ЗАЛП СТРЕЛ! Урон: {damage}")
            print(f"Стрелы: {self.arrows}")
            return damage
        else:
            print("Недостаточно стрел для залпа!")

            return 0

