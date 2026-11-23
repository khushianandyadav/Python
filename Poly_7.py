'''
Create a class Shape with a method calculate_area(). Override it in Circle, Rectangle, and Triangle to calculate their respective areas.
'''

class Shape:
    def calculate_area(self):
        pass

class Circle(Shape):
    def calculate_area(self, radius):
        pi = 3.14
        area = (pi * (radius**2))
        return area

class Rectangle(Shape):
    def calculate_area(self, length, width):
        area = length * width
        return area

class Triangle(Shape):
    def calculate_area(self, base, height):
        area = 0.5 * base * height
        return area

c = Circle()
r = Rectangle()
t = Triangle()

print(c.calculate_area(4))
print(r.calculate_area(4, 5))
print(t.calculate_area(7, 12))
    
