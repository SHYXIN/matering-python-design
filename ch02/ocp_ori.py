class Rectangle:
    def __init__(self, width: float, height: float):
        self.width: float = width
        self.height: float = height

class Circle:
    def __init__(self, radius: float):
        self.radius = radius

def calculate_arae(shape) -> float:
    if isinstance(shape, Rectangle):
        return shape.width * shape.height
    elif isinstance(shape, Circle):
        return shape.radius **2 * 3.14
