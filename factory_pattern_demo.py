from abc import ABC, abstractmethod
import math

# Abstract Product
class Shape(ABC):
    """Abstract base class for all shapes."""

    @abstractmethod
    def area(self) -> float:
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """Calculate the perimeter of the shape."""
        pass

    @abstractmethod
    def draw(self) -> str:
        """Return a string representation of the shape."""
        pass

# Concrete Products
class Circle(Shape):
    """Concrete implementation of a Circle."""

    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius

    def draw(self) -> str:
        return f"Drawing a Circle with radius {self.radius}"

class Square(Shape):
    """Concrete implementation of a Square."""

    def __init__(self, side: float):
        self.side = side

    def area(self) -> float:
        return self.side ** 2

    def perimeter(self) -> float:
        return 4 * self.side

    def draw(self) -> str:
        return f"Drawing a Square with side {self.side}"

class Triangle(Shape):
    """Concrete implementation of an Equilateral Triangle."""

    def __init__(self, side: float):
        self.side = side

    def area(self) -> float:
        return (math.sqrt(3) / 4) * self.side ** 2

    def perimeter(self) -> float:
        return 3 * self.side

    def draw(self) -> str:
        return f"Drawing an Equilateral Triangle with side {self.side}"

# Abstract Factory
class ShapeFactory(ABC):
    """Abstract factory for creating shapes."""

    @abstractmethod
    def create_shape(self, shape_type: str, **kwargs) -> Shape:
        """Create a shape based on type and parameters."""
        pass

# Concrete Factory
class BasicShapeFactory(ShapeFactory):
    """Concrete factory for basic shapes."""

    def create_shape(self, shape_type: str, **kwargs) -> Shape:
        shape_type = shape_type.lower()

        if shape_type == "circle":
            radius = kwargs.get("radius", 1.0)
            return Circle(radius)
        elif shape_type == "square":
            side = kwargs.get("side", 1.0)
            return Square(side)
        elif shape_type == "triangle":
            side = kwargs.get("side", 1.0)
            return Triangle(side)
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")

# Advanced Factory with additional features
class AdvancedShapeFactory(ShapeFactory):
    """Advanced factory with validation and logging."""

    def __init__(self):
        self.created_shapes = []

    def create_shape(self, shape_type: str, **kwargs) -> Shape:
        # Validation
        if shape_type.lower() == "circle":
            radius = kwargs.get("radius", 1.0)
            if radius <= 0:
                raise ValueError("Radius must be positive")
            shape = Circle(radius)
        elif shape_type.lower() == "square":
            side = kwargs.get("side", 1.0)
            if side <= 0:
                raise ValueError("Side must be positive")
            shape = Square(side)
        elif shape_type.lower() == "triangle":
            side = kwargs.get("side", 1.0)
            if side <= 0:
                raise ValueError("Side must be positive")
            shape = Triangle(side)
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")

        # Logging
        self.created_shapes.append(shape_type)
        print(f"Created a {shape_type} with parameters: {kwargs}")

        return shape

    def get_creation_stats(self) -> dict:
        """Get statistics of created shapes."""
        from collections import Counter
        return dict(Counter(self.created_shapes))

# Client code
def shape_processor(factory: ShapeFactory, shape_specs: list) -> None:
    """Process a list of shape specifications using the factory."""
    shapes = []

    for spec in shape_specs:
        shape = factory.create_shape(**spec)
        shapes.append(shape)

    print("\nProcessing created shapes:")
    for shape in shapes:
        print(f"{shape.draw()}")
        print(f"  Area: {shape.area():.2f}")
        print(f"  Perimeter: {shape.perimeter():.2f}")
        print()

if __name__ == "__main__":
    print("Demonstrating Factory Design Pattern in Python:")
    print("=" * 60)

    # Basic factory usage
    print("Using Basic Shape Factory:")
    basic_factory = BasicShapeFactory()

    shape_specs = [
        {"shape_type": "circle", "radius": 5.0},
        {"shape_type": "square", "side": 4.0},
        {"shape_type": "triangle", "side": 3.0}
    ]

    shape_processor(basic_factory, shape_specs)

    # Advanced factory usage
    print("Using Advanced Shape Factory:")
    advanced_factory = AdvancedShapeFactory()

    advanced_specs = [
        {"shape_type": "circle", "radius": 3.0},
        {"shape_type": "square", "side": 6.0},
        {"shape_type": "circle", "radius": 2.0}
    ]

    shape_processor(advanced_factory, advanced_specs)

    print("Creation statistics:")
    stats = advanced_factory.get_creation_stats()
    for shape_type, count in stats.items():
        print(f"  {shape_type}: {count}")

    print("\nThe Factory Pattern provides a way to create objects without")
    print("specifying the exact class of object that will be created.")
    print("This promotes loose coupling and makes the code more flexible.")