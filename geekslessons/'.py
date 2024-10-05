class Figure:
    unit = "см"

    def init(self):
        pass

    def calculate_area(self):
        pass

    NotImplementedError("Subclasses should implement this method")

    def info(self):
        pass

    NotImplementedError("Subclasses should implement this method")


class Square(Figure):

    def init(self, side_length):
        super().__init()
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length ** 2

    def info(self, square=None):
        area = self.calculate_area()
        print(f"Square side Lenght:{self.side_length}{self.unit}, area:"
              f"{area}{self.unit}.")

        square1 = Square(5)
        square2 = Square(3)
        square_list = [square1, square2]

        for square_list in square_list:
            square.info()


class Rectangle(Figure):
    def __init(self, length, __width):
        super().__init()
        self.length = __length
        self.width = __width

    def calculate_area(self):
        return (self.length *
                self.length)

    def info(self):
        area = self.calculate_area()
        print(f"Rectangle length:{self.length}{self.unit} width:"
              f"{self.width}"f"{self.unit} area:{area}{self.unit}")

        rectangle1 = Rectangle(5, 8)
        rectangle2 = Rectangle(3, 6)
        rectangle3 = Rectangle(4, 10)
        rectangle_list = [rectangle1, rectangle2, rectangle3]

        for rectangle in rectangle_list:
            rectangle.info()