from chest import Chest
from button import Button
from tamagochi import Tamagochi

chest = Chest(["Кристал", "Чары усиления", "Улучшение брони"])
chest.lock_out()
chest.open()
chest.close()
chest.lock_up()


button = Button("Пока пока", x = 1, y = 1, a = 1, b = 1, color="красный")
button.press()

button.re_color("черный")
button.re_rext("Привет")
print(button.re_size(new_x = 15, new_y = 20, new_a = 10, new_b = 10))

button.button_info()


tamagochi = Tamagochi("ГГ")
tamagochi.play()
tamagochi.play()
tamagochi.play()
tamagochi.play()
tamagochi.play()
tamagochi.feed()
tamagochi.sleep()
tamagochi.need()
tamagochi.work()
tamagochi.status()
tamagochi.feed()
