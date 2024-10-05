class Figure:
    unit = "cm"
    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass

class Square(Figure):
    def __init__(self, __side_length):
        super().__init__()
        self.side_length = __side_length

    def calculate_area(self):
        return self.side_length ** 2

    def info(self):
        area = self.calculate_area()
        print(f"Square side length: {self.side_length}{Figure.unit}, area: {area}{Figure.unit}")

class Rectangle(Figure):
    def __init__(self, __length, __width):
        super().__init__()
        self.length = __length
        self.width = __width

    def calculate_area(self):
        return self.length * self.width

    def info(self):
        area = self.calculate_area()
        print(f"Rectangle length: {self.length}{Figure.unit},"
              f" width: {self.width}{Figure.unit}, area: {area}{Figure.unit}")

if __name__ == "__main__":
    figures = [
        Square(15),
        Square(5),
        Rectangle(5, 6),
        Rectangle(9, 8),
        Rectangle(7, 9)
    ]

    for figure in figures:
        figure.info()