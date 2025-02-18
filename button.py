class Button:
    def __init__(self, text, size="большой", color="серый"):
        self.text = text
        self.size = size
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

    def re_size(self, new_size):
        self.size = new_size
        print(f"Размер кнопки изменен на {self.size}")

    def button_info(self):
        print(f"Текст кнопки: '{self.text}', цвет: '{self.color}', размер: '{self.size}'")