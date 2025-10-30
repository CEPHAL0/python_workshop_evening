# Inheritance
# One class inherits the methods and attributes of another class
# Parent - Child Relationship
# Sharing of attributes and methods
# To remove the redundancies

# Single Inheritance

# Base Class
class Shape:
    area = 0
    perimeter = 0
    name = ""

    def __repr__(self):
        information = f"""
            Area: {self.area}
            Perimter: {self.perimeter}
            Name: {self.name}
        """
        return information


# 5 different child classes

# Children Classes
class Rectangle(Shape):
    length = 0
    breadth = 0

    def calc_area(self):
        self.area = self.length * self.breadth

    def calc_perimeter(self):
        self.perimeter = 2 * (self.length + self.breadth)


class Circle(Shape):
    radius = 0

    def calc_area(self):
        self.area = 3.14 * (self.radius ** 2)
        self.area = round(self.area, 4)

    def calc_perimeter(self):
        self.perimeter = 3.14 * 2 * self.radius
        self.perimeter = round(self.perimeter, 4)

class Square(Shape):
    length = 0
    
    def calc_area(self):
        self.area = self.length ** 2
    def calc_perimeter(self):
        self.perimeter = 4 * self.length


rect1 = Rectangle()
rect1.name = "Rectangle"
rect1.length = 5
rect1.breadth = 5

rect1.calc_area()
rect1.calc_perimeter()
print(rect1)


circ1 = Circle()
circ1.name = "Circle"
circ1.radius = 9

circ1.calc_area()
circ1.calc_perimeter()
print(circ1)
