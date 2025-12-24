class Vector:
    """
    A simple 2D vector class demonstrating various dunder methods.
    """

    def __init__(self, x, y):
        """Initialize the vector with x and y coordinates."""
        self.x = x
        self.y = y

    def __str__(self):
        """String representation for end users."""
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        """Official string representation for developers/debugging."""
        return f"Vector(x={self.x}, y={self.y})"

    def __len__(self):
        """Return the 'length' as the number of components (always 2 for 2D)."""
        return 2

    def __add__(self, other):
        """Add two vectors."""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        """Subtract two vectors."""
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __eq__(self, other):
        """Check equality of two vectors."""
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False

    def __lt__(self, other):
        """Compare vectors by their magnitude."""
        if isinstance(other, Vector):
            return (self.x**2 + self.y**2) < (other.x**2 + other.y**2)
        return NotImplemented

    def __getitem__(self, index):
        """Allow indexing like v[0] for x, v[1] for y."""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Vector index out of range")

    def __setitem__(self, index, value):
        """Allow setting values by index."""
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        else:
            raise IndexError("Vector index out of range")

    def __call__(self):
        """Make the vector callable, returning its magnitude."""
        return (self.x**2 + self.y**2)**0.5

class CustomList:
    """
    A simple list-like class demonstrating more dunder methods.
    """

    def __init__(self, items=None):
        self.items = items if items is not None else []

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __delitem__(self, index):
        del self.items[index]

    def __iter__(self):
        return iter(self.items)

    def __contains__(self, item):
        return item in self.items

if __name__ == "__main__":
    print("Demonstrating Dunder Methods in Python:")
    print("=" * 50)

    # Vector examples
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)

    print(f"v1: {v1}")  # __str__
    print(f"repr(v1): {repr(v1)}")  # __repr__
    print(f"len(v1): {len(v1)}")  # __len__

    v3 = v1 + v2  # __add__
    print(f"v1 + v2: {v3}")

    v4 = v1 - v2  # __sub__
    print(f"v1 - v2: {v4}")

    print(f"v1 == v2: {v1 == v2}")  # __eq__
    print(f"v1 < v2: {v1 < v2}")  # __lt__

    print(f"v1[0]: {v1[0]}")  # __getitem__
    v1[1] = 5  # __setitem__
    print(f"After v1[1] = 5: {v1}")

    print(f"v1(): {v1()}")  # __call__ (magnitude)

    print("\nCustom List Example:")
    cl = CustomList([1, 2, 3, 4, 5])
    print(f"len(cl): {len(cl)}")
    print(f"cl[2]: {cl[2]}")
    cl[2] = 99
    print(f"After cl[2] = 99: {cl[2]}")
    print(f"3 in cl: {3 in cl}")  # __contains__
    print(f"99 in cl: {99 in cl}")

    print("\nDunder methods (double underscore methods) allow custom objects")
    print("to behave like built-in types, enabling operator overloading and")
    print("special behaviors essential for advanced Python programming.")