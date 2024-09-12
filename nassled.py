class Human: # При наследовании, этот класс стал родительским, а тот, что наследует - дочерним.
    head = True

    def say_hello(self):
        print("Здравствуйте")


class Student(Human): # в скобках указываю откуда будет "наследоваться" наш класс.
    # Дочерний класс. Наследует атрибуты родительского класса
    def about(self):
        print("Я студент")

class Teacher(Human):
    pass


human = Human()
student = Student()
teacher = Teacher()
print(human.head) # True
student.about() # вызов метода класса. # Я студент
print(student.head) # True
# human.about() # AttributeError: 'Human' object has no attribute 'about'
teacher.say_hello()
student.say_hello()
