class CanSwim:
    def swim(self):
        return "Я плаваю"

class CanFly:
    def fly(self):
        return "Я летаю"

# Класс наследует способности обоих родителей
class Duck(CanSwim, CanFly):
    pass

donald = Duck()
print(donald.swim())
print(donald.fly())