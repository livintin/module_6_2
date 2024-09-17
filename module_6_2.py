class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']  # цвет утверждённый «АВТОВАЗ»

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        return print(f"Модель: {self.__model}\n")

    def get_horsepower(self):
        return print(f"Мощность двигателя: {self.__engine_power}\n")

    def get_color(self):
        return print(f"Цвет: {self.__color}\n")

    def print_info(self):
        return print(f"Модель: {self.__model}\n"
                     f"Мощность двигателя: {self.__engine_power}\n"
                     f"Цвет: {self.__color}\n"
                     f"Владелец: {self.owner}")

    def set_color(self, new_color):
        a = []
        for color in self.__COLOR_VARIANTS:
            a.append(color.lower())
        if new_color.lower() in a:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
