# figures = ["triangle", "rectangle", "square"]

# def triangle_area():
#     a = float(input("Enter the base of the triangle: "))
#     h = float(input("Enter the height of the triangle: "))
#     return 0.5 * a * h

# def rectangle_area():
#     a = float(input("Enter the first side of the rectangle: "))
#     b = float(input("Enter the second side of the rectangle: "))
#     return a * b

# def square_area():
#     a = float(input("Enter the side of the square: "))
#     return a * a

# print("List of geometric figures: ", figures)

# while True:
#     figure = input("Enter the name of the geometric figure: ")
#     if figure == "stop":
#         break
#     elif figure in figures:
#         if figure == "triangle":
#             print("The area of the triangle is: ", triangle_area())
#             break
#         elif figure == "rectangle":
#             print("The area of the rectangle is: ", rectangle_area())
#             break
#         elif figure == "square":
#             print("The area of the square is: ", square_area())
#             break
#     else:
#         print("The figure is not in the list of figures")

#Zosia 
from abc import ABC, abstractmethod

supported_geometry_types = ["rectangle", "triangle", "circle"]
geometry_type = None
while geometry_type is None or geometry_type not in supported_geometry_types:
    geometry_type = input(
        f"Enter type of geometry (must be in: "
        + ", ".join(supported_geometry_types)
        + "): "
    )

class Shape(ABC):
    @abstractmethod
    def __init__(self) -> None:
        self._name = None
        self._parameters = {}
        self.area = None

    @abstractmethod
    def _calculate_area(self):
        pass

    def get_parameters(self):
        for param_key, param_val in self._parameters.items():
            while self._parameters[param_key] <= 0:
               self._parameters[param_key] = int(
                   input(f"Enter {self._name} {param_key}: ")
               )

    def get_area(self):
        self._calculate_area()
        print(f"Area of {self._name} is equal: {self.area}")

class Rectangle(Shape):
    def __init__(self) -> None:
        super().__init__()
        self._parameters = {"width": 0, "height": 0}
        self._name = "rectangle"

    def _calculate_area(self):
        self.area = self._parameters["width"] * self._parameters["height"]

class Triangle(Shape):
    def __init__(self) -> None:
        super().__init__()
        self._parameters = {"base": 0, "height": 0}
        self._name = "triangle"

    def _calculate_area(self):
        self.area = 0.5 * self._parameters["base"] * self._parameters["height"]

class Circle(Shape):
    def __init__(self) -> None:
        super().__init__()
        self._parameters = {"radius": 0}
        self._name = "circle"

    def calculate_area(self):
        self.area = math.pi * self._parameters["radius"] ** 2

if geometry_type == "rectangle":
    geomery = Rectangle()
elif geometry_type == "triangle":
    geomery = Triangle()
elif geometry_type == "circle":
    geomery = Circle()

geomery.get_parameters()
geomery.get_area()