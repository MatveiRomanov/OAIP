class Item:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class Tool:
    def __init__(self, name, durability, material):
        self.__name = name
        self.__durability = durability
        self.__material = material

    def get_name(self):
        return self.__name

    def get_durability(self):
        return self.__durability

    def get_material(self):
        return self.__material

    def info(self):
        return f"{self.__name} (Материал: {self.__material}, Прочность: {self.__durability})"


class Inventory:
    def __init__(self):
        self.items = []

    def add(self, item, count=1):
        for i in range(count):
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


class CraftingTable:
    def __init__(self):
        self.recipes = {
            "Diamond Sword": (
            [Item("Diamond"), Item("Diamond"), Item("Stick")], Tool("Diamond Sword", 1561, "Diamond")),
            "Iron Pickaxe": ([Item("Iron Ingot"), Item("Iron Ingot"), Item("Iron Ingot"), Item("Stick"), Item("Stick")],
                             Tool("Iron Pickaxe", 250, "Iron")),
            "Golden Shovel": ([Item("Gold Ingot"), Item("Stick"), Item("Stick")], Tool("Golden Shovel", 32, "Gold")),
            "Stone Axe": ([Item("Cobblestone"), Item("Cobblestone"), Item("Cobblestone"), Item("Stick"), Item("Stick")],
                          Tool("Stone Axe", 131, "Stone")),
            "Netherite Sword": ([Item("Netherite Ingot"), Tool("Diamond Sword", 1561, "Diamond")],
                                Tool("Netherite Sword", 2031, "Netherite")),
            "Diamond Hoe": (
                [Item("Diamond"), Item("Diamond"), Item("Stick"), Item("Stick")], Tool("Diamond Hoe", 1561, "Diamond")),
            "Iron Axe": ([Item("Iron Ingot"), Item("Iron Ingot"), Item("Iron Ingot"), Item("Stick"), Item("Stick")],
                         Tool("Iron Axe", 250, "Iron")),
            "Golden Pickaxe": (
            [Item("Gold Ingot"), Item("Gold Ingot"), Item("Gold Ingot"), Item("Stick"), Item("Stick")],
            Tool("Golden Pickaxe", 32, "Gold")),
            "Diamond Pickaxe": ([Item("Diamond"), Item("Diamond"), Item("Diamond"), Item("Stick"), Item("Stick")],
                                Tool("Diamond Pickaxe", 1561, "Diamond")),
            "Netherite Pickaxe": ([Item("Netherite Ingot"), Tool("Diamond Pickaxe", 1561, "Diamond")],
                                  Tool("Netherite Pickaxe", 2031, "Netherite"))
        }

    def craft(self, tool_name, inventory):
        if tool_name not in self.recipes:
            print(f"Рецепт {tool_name} не найден")
            return None

        requirements, result = self.recipes[tool_name]

        for item in requirements:
            if inventory.count(item.get_name()) < 1:
                print(f"Не хватает {item.get_name()} для создания {tool_name}")
                return None

        for item in requirements:
            inventory.remove(item.get_name(), 1)

        inventory.add(result)
        print(f"Создано: {result.info()}")
        return result

    def disassemble(self, tool_name, inventory):
        if tool_name not in self.recipes:
            print(f"Рецепт {tool_name} не найден")
            return None

        requirements, result = self.recipes[tool_name]

        if inventory.count(tool_name) < 1:
            print(f"Не хватает {tool_name} для разборки")
            return None

        inventory.remove(tool_name, 1)

        for item in requirements:
            inventory.add(item)

        print(f"Разобрано: {tool_name}")
        return requirements


inv = Inventory()
inv.add(Item("Diamond"), 3)
inv.add(Item("Stick"), 2)
inv.add(Item("Netherite Ingot"), 1)

crafting_table = CraftingTable()

print("До крафта:", inv.show())
crafting_table.craft("Diamond Sword", inv)
crafting_table.craft("Netherite Sword", inv)
print("После крафта:", inv.show())

crafting_table.disassemble("Netherite Sword", inv)
print("После разборки:", inv.show())
