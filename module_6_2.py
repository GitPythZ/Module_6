#Задача "Изменять нельзя получать"
class Vehicle():
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self,  owner, model, engine_power, colour):
        self.owner = str(owner)
        self.__model = str(model)
        self.__engine_power = int(engine_power)
        self.__colour = str(colour)

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_hoursepower(self):
        return f"Мощность двигателя: {self.__engine_power} л. с."

    def get_colour(self):
        return f"Цвет: {self.__colour}"

    def print_info(self):
        print(f"{self.get_model()} \n{self.get_hoursepower()} \n{self.get_colour()} \nВладелец: {self.owner}")

    def set_colour(self, new_colour):
        self.new_colour = str(new_colour)
        marker = False
        for i in self.__COLOR_VARIANTS:
            if new_colour.upper() == i.upper():
                self.__colour = i
                marker = True
        if not marker:
            print(f"Нельзя сменить цвет на {new_colour}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, "blue")
vehicle1.print_info()
vehicle1.set_colour('Pink')
vehicle1.set_colour('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()