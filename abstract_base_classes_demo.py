from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """
    Abstract Base Class representing a geometric shape.
    It defines a blueprint (contract) that all subclasses must follow.
    """

    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass

    def description(self):
        """
        Concrete method in an abstract class.
        Abstract classes can have standard methods with shared logic.
        """
        return f"I am a {self.__class__.__name__}."

class Circle(Shape):
    """Concrete implementation of Shape for a Circle."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    """Concrete implementation of Shape for a Rectangle."""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# --- Practical Example: AI Model Interface ---

class AIModel(ABC):
    """
    An abstract base class for AI models.
    Ensures every model has 'predict' and 'save' methods.
    """
    
    @abstractmethod
    def predict(self, data):
        """Make a prediction based on input data."""
        pass

    @abstractmethod
    def save(self, path):
        """Save model weights to a file."""
        pass

class TextGenerator(AIModel):
    def predict(self, data):
        return f"Generating text based on: '{data}'... [Done]"

    def save(self, path):
        print(f"Model saved to: {path}/text_gen.bin")

def demonstrate_abcs():
    print("Demonstrating Abstract Base Classes (ABCs) in Python:")
    print("=" * 55)

    # 1. Attempting to instantiate an abstract class (will fail)
    print("\n1. Instantiation Protection:")
    try:
        shape = Shape()
    except TypeError as e:
        print(f"   [!] Caught expected error: {e}")

    # 2. Using concrete subclasses
    print("\n2. Working with Subclasses:")
    shapes = [Circle(5), Rectangle(4, 6)]
    
    for s in shapes:
        print(f"{s.description()}")
        print(f"   Area: {s.area():.2f}")
        print(f"   Perimeter: {s.perimeter():.2f}")

    # 3. AI Model Example
    print("\n3. AI Model Interface Enforcement:")
    model = TextGenerator()
    print(f"   Prediction: {model.predict('Once upon a time')}")
    model.save("./models")

if __name__ == "__main__":
    demonstrate_abcs()

    print("\nAbstract Base Classes (ABCs) ensure that derived classes implement")
    print("specific methods, creating a formal interface. This is vital for")
    print("large systems where you want to guarantee that different components")
    print("(like different database drivers or AI models) share the same API.")
