class Button:
    def __init__(self, text, x, y, a, b, color="серый"):
        self.text = text
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.color = color

    def press(self):
        if self.color == "красный":
            print("Бабах!")
        else:
            print(f"Кнопка с названием '{self.text}' активирована")

    def re_rext(self, new_text):
        self.text = new_text
        print(f"Название измененно на {self.text}")

    def re_color(self, new_color):
        self.color = new_color
        print(f"Цвет кнопки изменен на {self.color}")

    def re_size(self, new_x, new_y, new_a, new_b):
        self.x,y,a,b = new_x, new_y, new_a, new_b
        print(f"Размер кнопки изменен на {self.x,y,a,b}")

    def button_info(self):
        print(f"Текст кнопки: '{self.text}', цвет: '{self.color}', расположение: x = {self.x} y = {self.y}, размер: a = {self.a}, b = {self.b}")
