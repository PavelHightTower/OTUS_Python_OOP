class Rectangle:
    """This class return Rectangle"""
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b
        self.area = side_a * side_b

    # def __str__(self):
    #     return f"Rectangle with side: {self.side_a} and side: {self.side_b}"
    #
    # def __repr__(self):
    #     return f"Rectangle with side: {self.side_a} and side: {self.side_b}"


r = Rectangle(1, 2)
print(dir(r))
