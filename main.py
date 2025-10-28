from classes import *


def demo_task1():
    print("=== Задача 1: Веб-приложение ===")

    label = Label("username_label", "Имя пользователя:", "18px Arial")
    line_edit = LineEdit("username_input", "Введите имя...")
    button = Button("submit_btn", "Отправить", "primary")
    checkbox = CheckBox("agree_checkbox", "Согласен с условиями", False)

    print(label.render())
    print(line_edit.render())
    print(button.render())
    print(checkbox.render())
    print()


def demo_task2():
    print("=== Задача 2: Иерархия оружия ===")

    sword = ColdWeapon("Меч возмездия", 25, 1.2, "одноручный")
    pistol = Firearm("Пистолет 'Ворон'", 15, 12, 6)
    shotgun = Shotgun("Дробовик 'Гром'", 40, 2, 8)

    weapons = [sword, pistol, shotgun]

    for weapon in weapons:
        print(weapon.info())
        print(f"Урон: {weapon.calculate_damage()}")
        print()


def demo_task3():
    print("=== Задача 3: Тетрис ===")

    game = TetrisGame()
    i_piece = IPiece()
    l_piece = LPiece()

    print("Игра Тетрис инициализирована")
    print(f"Текущий уровень: {game.level}")
    print(f"Фигура I: {i_piece.shape}")
    print(f"Фигура L: {l_piece.shape}")
    print()


def demo_task4():
    print("=== Задача 4: RPG Персонажи ===")

    warrior = Warrior("Боромир", 150, 25)
    mage = Mage("Гэндальф", 80, 15, 100)
    archer = Archer("Леголас", 100, 20, 30)

    characters = [warrior, mage, archer]

    for char in characters:
        char.info()
        char.attack()
        if hasattr(char, 'special_ability'):
            char.special_ability()
        print()


if __name__ == "__main__":
    demo_task1()
    demo_task2()
    demo_task3()
    demo_task4()