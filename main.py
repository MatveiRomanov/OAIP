class Item:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def use(self):
        return f"Осмотр: {self.__name}"

    def craft(self, other, inventory):
        return None

    def disassemble(self):
        return [Item(self.__name)]

    def __repr__(self):
        return self.__name


class Tool:
    def __init__(self, name, durability, material):
        self.__name = name
        self.__durability = durability
        self.__material = material

    def get_name(self):
        return self.__name

    def use(self):
        self.__durability -= 1
        if self.__durability <= 0:
            return f"{self.__name} сломался!"
        return f"Использован {self.__name}. Прочность: {self.__durability}"

    def craft(self, other, inventory):
        if self.__name == "Diamond Sword" and other.get_name() == "Netherite Ingot":
            if inventory.count("Netherite Ingot") >= 1:
                inventory.remove("Netherite Ingot", 1)
                new_tool = Tool("Netherite Sword", 2031, "Netherite")
                return new_tool

        elif self.__name == "Diamond Pickaxe" and other.get_name() == "Netherite Ingot":
            if inventory.count("Netherite Ingot") >= 1:
                inventory.remove("Netherite Ingot", 1)
                new_tool = Tool("Netherite Pickaxe", 2031, "Netherite")
                return new_tool

        return None

    def disassemble(self):
        fragments = []
        if "Diamond" in self.__material:
            fragments.append(Item("Diamond"))
        if "Iron" in self.__material:
            fragments.append(Item("Iron Ingot"))
        if "Gold" in self.__material:
            fragments.append(Item("Gold Ingot"))
        if "Stone" in self.__material:
            fragments.append(Item("Cobblestone"))

        fragments.append(Item("Stick"))
        return fragments

    def info(self):
        return f"{self.__name} (Материал: {self.__material}, Прочность: {self.__durability})"

    def __repr__(self):
        return self.__name


class Inventory:
    def __init__(self):
        self.items = []

    def add(self, item, count=1):
        for _ in range(count):
            self.items.append(item)

    def remove(self, item_name, count):
        removed = 0
        new_items = []
        for item in self.items:
            if item.get_name() == item_name and removed < count:
                removed += 1
            else:
                new_items.append(item)
        self.items = new_items
        return removed == count

    def count(self, item_name):
        return sum(1 for item in self.items if item.get_name() == item_name)

    def show(self):
        from collections import Counter
        c = Counter([item.get_name() for item in self.items])
        return dict(c)

    def find_item(self, item_name):
        for item in self.items:
            if item.get_name() == item_name:
                return item
        return None


def disassemble_item(item, inventory):
    print(f"Разбор: {item.get_name()}")

    inventory.remove(item.get_name(), 1)

    components = item.disassemble()

    for component in components:
        inventory.add(component)
        print(f"Получен: {component.get_name()}")

    return components


def craft_items(item1, item2, inventory):
    print(f"Крафт: {item1.get_name()} + {item2.get_name()}")

    result = item1.craft(item2, inventory)
    if result is None:
        result = item2.craft(item1, inventory)

    if result:
        inventory.add(result)
        print(f"Создано: {result.info()}")
    else:
        print("Крафт невозможен")

    return result


if __name__ == "__main__":
    inv = Inventory()

    stick = Item("Stick")
    diamond = Item("Diamond")
    iron = Item("Iron Ingot")
    gold = Item("Gold Ingot")
    stone = Item("Cobblestone")
    netherite = Item("Netherite Ingot")

    inv.add(stick, 5)
    inv.add(diamond, 3)
    inv.add(iron, 3)
    inv.add(gold, 2)
    inv.add(stone, 4)
    inv.add(netherite, 2)

    print("Начало:")
    print(inv.show())
    print()

    diamond_sword = Tool("Diamond Sword", 1561, "Diamond")
    inv.add(diamond_sword)

    diamond_pickaxe = Tool("Diamond Pickaxe", 1561, "Diamond")
    inv.add(diamond_pickaxe)

    iron_pickaxe = Tool("Iron Pickaxe", 250, "Iron")
    inv.add(iron_pickaxe)

    print("С инструментами:")
    print(inv.show())
    print()

    stick_item = inv.find_item("Stick")
    diamond_item = inv.find_item("Diamond")

    if stick_item and diamond_item:
        craft_items(stick_item, diamond_item, inv)

    print("После крафта:")
    print(inv.show())
    print()

    diamond_sword = inv.find_item("Diamond Sword")
    netherite_item = inv.find_item("Netherite Ingot")

    if diamond_sword and netherite_item:
        craft_items(diamond_sword, netherite_item, inv)

    print("После улучшения:")
    print(inv.show())
    print()

    iron_pickaxe = inv.find_item("Iron Pickaxe")
    if iron_pickaxe:
        disassemble_item(iron_pickaxe, inv)

    print("После разбора:")
    print(inv.show())
    print()

    for item in [inv.find_item("Stick"), inv.find_item("Diamond Sword"), inv.find_item("Netherite Sword")]:
        if item:
            print(item.use())