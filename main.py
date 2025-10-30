class Item:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class Tool:
    def __init__(self, name, durability, material, level=1):
        self.__name = name
        self.__durability = durability
        self.__material = material
        self.__level = level

    def get_name(self):
        return self.__name

    def get_durability(self):
        return self.__durability

    def get_material(self):
        return self.__material

    def get_level(self):
        return self.__level

    def upgrade(self):
        self.__level += 1
        self.__durability += 100
        print(f"{self.__name} улучшен до уровня {self.__level}!")

    def info(self):
        return f"{self.__name} (Материал: {self.__material}, Прочность: {self.__durability}, Уровень: {self.__level})"


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

    def find_tool(self, tool_name):
        for item in self.items:
            if isinstance(item, Tool) and item.get_name() == tool_name:
                return item
        return None

    def show(self):
        from collections import Counter
        c = Counter([f"{item.get_name()} (ур.{item.get_level()})" if isinstance(item, Tool) else item.get_name() for item in self.items])
        return dict(c)


class CraftingTable:
    def __init__(self):
        self.recipes = {
            "Diamond Sword": ([Item("Diamond"), Item("Diamond"), Item("Stick")], Tool("Diamond Sword", 1561, "Diamond")),
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
            "Golden Pickaxe": ([Item("Gold Ingot"), Item("Gold Ingot"), Item("Gold Ingot"), Item("Stick"), Item("Stick")],
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

    def upgrade_tool(self, tool_name, inventory):
        tool = inventory.find_tool(tool_name)
        if not tool:
            print(f"Инструмент {tool_name} не найден в инвентаре")
            return False
        
        if tool.get_level() >= 3:
            print(f"{tool_name} уже максимального уровня!")
            return False
            
        if inventory.count("Diamond") < 1:
            print(f"Не хватает Diamond для улучшения {tool_name}")
            return False
            
        inventory.remove("Diamond", 1)
        tool.upgrade()
        return True


inv = Inventory()
inv.add(Item("Diamond"), 5)
inv.add(Item("Stick"), 3)
inv.add(Item("Netherite Ingot"), 1)

crafting_table = CraftingTable()

print("До крафта:", inv.show())
crafting_table.craft("Diamond Sword", inv)
print("После крафта:", inv.show())

crafting_table.upgrade_tool("Diamond Sword", inv)
crafting_table.upgrade_tool("Diamond Sword", inv)
crafting_table.upgrade_tool("Diamond Sword", inv)
print("После прокачки:", inv.show())

crafting_table.craft("Netherite Sword", inv)
print("После создания Netherite:", inv.show())

