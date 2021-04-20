class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b


class Square:
    def __init__(self, a):
        self.a = a

    def get_area_square(self):
        return self.a ** 2

# добавляем клас Круг для вычесления площади
class Circle:
    def __init__(self, r, p=3.14):
        self.r = r
        self.p = p

    def get_area_circle(self):
        return (self.p * self.r) ** 2

