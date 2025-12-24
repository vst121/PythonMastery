from abc import ABC, abstractmethod
from typing import List

# Component Interface
class FileSystemComponent(ABC):
    """Abstract base class for file system components."""

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def get_size(self) -> int:
        """Get the size of the component."""
        pass

    @abstractmethod
    def display(self, indent: str = "") -> None:
        """Display the component with indentation."""
        pass

    def add(self, component: 'FileSystemComponent') -> None:
        """Add a component (only for composites)."""
        raise NotImplementedError("Cannot add to a leaf component")

    def remove(self, component: 'FileSystemComponent') -> None:
        """Remove a component (only for composites)."""
        raise NotImplementedError("Cannot remove from a leaf component")

    def get_child(self, index: int) -> 'FileSystemComponent':
        """Get a child component (only for composites)."""
        raise NotImplementedError("Leaf components have no children")

# Leaf
class File(FileSystemComponent):
    """Represents a file (leaf component)."""

    def __init__(self, name: str, size: int):
        super().__init__(name)
        self._size = size

    def get_size(self) -> int:
        return self._size

    def display(self, indent: str = "") -> None:
        print(f"{indent}File: {self.name} ({self._size} bytes)")

# Composite
class Directory(FileSystemComponent):
    """Represents a directory (composite component)."""

    def __init__(self, name: str):
        super().__init__(name)
        self._children: List[FileSystemComponent] = []

    def add(self, component: FileSystemComponent) -> None:
        """Add a child component."""
        self._children.append(component)

    def remove(self, component: FileSystemComponent) -> None:
        """Remove a child component."""
        self._children.remove(component)

    def get_child(self, index: int) -> FileSystemComponent:
        """Get a child component by index."""
        return self._children[index]

    def get_size(self) -> int:
        """Calculate total size of all children."""
        return sum(child.get_size() for child in self._children)

    def display(self, indent: str = "") -> None:
        print(f"{indent}Directory: {self.name}/")
        for child in self._children:
            child.display(indent + "  ")

# Another example: Graphics system
class GraphicComponent(ABC):
    """Abstract base class for graphic components."""

    @abstractmethod
    def draw(self, indent: str = "") -> None:
        pass

    @abstractmethod
    def move(self, x: int, y: int) -> None:
        pass

    def add(self, component: 'GraphicComponent') -> None:
        raise NotImplementedError("Cannot add to a primitive component")

    def remove(self, component: 'GraphicComponent') -> None:
        raise NotImplementedError("Cannot remove from a primitive component")

class Circle(GraphicComponent):
    """Primitive graphic: Circle."""

    def __init__(self, x: int, y: int, radius: int):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, indent: str = "") -> None:
        print(f"{indent}Drawing Circle at ({self.x}, {self.y}) with radius {self.radius}")

    def move(self, x: int, y: int) -> None:
        self.x += x
        self.y += y
        print(f"Circle moved to ({self.x}, {self.y})")

class Rectangle(GraphicComponent):
    """Primitive graphic: Rectangle."""

    def __init__(self, x: int, y: int, width: int, height: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, indent: str = "") -> None:
        print(f"{indent}Drawing Rectangle at ({self.x}, {self.y}) {self.width}x{self.height}")

    def move(self, x: int, y: int) -> None:
        self.x += x
        self.y += y
        print(f"Rectangle moved to ({self.x}, {self.y})")

class GraphicGroup(GraphicComponent):
    """Composite graphic: Group of graphics."""

    def __init__(self, name: str):
        self.name = name
        self._children: List[GraphicComponent] = []

    def add(self, component: GraphicComponent) -> None:
        self._children.append(component)

    def remove(self, component: GraphicComponent) -> None:
        self._children.remove(component)

    def draw(self, indent: str = "") -> None:
        print(f"{indent}Drawing Group: {self.name}")
        for child in self._children:
            child.draw(indent + "  ")

    def move(self, x: int, y: int) -> None:
        print(f"Moving Group: {self.name} by ({x}, {y})")
        for child in self._children:
            child.move(x, y)

# Client code
def demonstrate_file_system() -> None:
    """Demonstrate file system composite pattern."""
    print("File System Composite Pattern:")
    print("-" * 40)

    # Create files
    file1 = File("document.txt", 1024)
    file2 = File("image.jpg", 2048)
    file3 = File("script.py", 512)
    file4 = File("data.csv", 3072)

    # Create directories
    root = Directory("root")
    docs = Directory("documents")
    images = Directory("images")
    project = Directory("project")

    # Build hierarchy
    docs.add(file1)
    docs.add(file4)
    images.add(file2)
    project.add(file3)

    root.add(docs)
    root.add(images)
    root.add(project)

    # Display structure
    root.display()

    # Calculate total size
    print(f"\nTotal size of root directory: {root.get_size()} bytes")

    # Demonstrate operations on individual components
    print(f"\nSize of documents directory: {docs.get_size()} bytes")
    print(f"Size of script.py: {file3.get_size()} bytes")

def demonstrate_graphics() -> None:
    """Demonstrate graphics composite pattern."""
    print("\n\nGraphics Composite Pattern:")
    print("-" * 40)

    # Create primitives
    circle1 = Circle(10, 10, 5)
    circle2 = Circle(20, 20, 8)
    rect1 = Rectangle(5, 5, 10, 15)
    rect2 = Rectangle(30, 30, 20, 10)

    # Create groups
    shapes_group = GraphicGroup("Basic Shapes")
    all_graphics = GraphicGroup("All Graphics")

    # Build hierarchy
    shapes_group.add(circle1)
    shapes_group.add(rect1)

    all_graphics.add(shapes_group)
    all_graphics.add(circle2)
    all_graphics.add(rect2)

    # Draw all graphics
    all_graphics.draw()

    # Move all graphics
    print("\nMoving all graphics by (5, 5):")
    all_graphics.move(5, 5)

    # Draw again to show new positions
    print("\nAfter moving:")
    all_graphics.draw()

if __name__ == "__main__":
    print("Demonstrating Composite Design Pattern in Python:")
    print("=" * 60)

    demonstrate_file_system()
    demonstrate_graphics()

    print("\nThe Composite Pattern allows treating individual objects")
    print("and compositions of objects uniformly, enabling tree-like")
    print("structures where clients don't need to distinguish between")
    print("leaves and composites.")