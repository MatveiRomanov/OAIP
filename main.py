from chest import Chest
from button import Button

chest = Chest(["Кристал", "Чары усиления", "Улучшение брони"])
chest.lock_out()
chest.open()
chest.close()
chest.lock_up()



button = Button("Пока пока", color="красный")
button.press()

button.re_color("черный")
button.re_rext("Привет")
button.re_size("Маленький")

button.button_info()
