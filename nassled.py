class Human: # При наследовании, этот класс стал родительским, а тот, что наследует - дочерним.
    head = True
    _legs = True
    __arms = True # "__" защищает от переопределения переменной в других классах

    def say_hello(self):
        print("Здравствуйте")

    def about(self):
        print(self.head)
        print(self._legs)
        print(self.__arms)


class Student(Human): # в скобках указываю откуда будет "наследоваться" наш класс.
    # Дочерний класс. Наследует атрибуты родительского класса
    pass
    # def about(self):
    #     print("Я студент")


class Teacher(Human):
    pass


# human = _Human()
# student = Student()
# teacher = Teacher()
# print(human.head) # True
# student.about() # вызов метода класса. # Я студент
# print(student.head) # True
# # human.about() # AttributeError: 'Human' object has no attribute 'about'
# teacher.say_hello()
# student.say_hello()
human = Human()
human.about()

student = Student()
student.about()

print(dir(human))