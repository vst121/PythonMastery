class Base:
    """The root of our diamond hierarchy."""
    def show(self):
        print("Base.show() called")

class Left(Base):
    """Inherits from Base."""
    def show(self):
        print("Left.show() starting")
        super().show()
        print("Left.show() finished")

class Right(Base):
    """Inherits from Base."""
    def show(self):
        print("Right.show() starting")
        super().show()
        print("Right.show() finished")

class Diamond(Left, Right):
    """
    Multiple Inheritance: Inherits from both Left and Right.
    Demonstrates the 'Diamond Problem' and MRO.
    """
    def show(self):
        print("Diamond.show() starting")
        super().show()
        print("Diamond.show() finished")

# --- Practical Example: Using Mixins ---

class JSONMixin:
    """A Mixin providing JSON serialization capability."""
    def to_json(self):
        import json
        # Simplified: Filter out underscore attributes
        data = {k: v for k, v in self.__dict__.items() if not k.startswith('_')}
        return json.dumps(data)

class LoggerMixin:
    """A Mixin providing logging capability."""
    def log(self, message):
        print(f"[LOG] {self.__class__.__name__}: {message}")

class UserProfile(LoggerMixin, JSONMixin):
    """
    A class that combines data with multiple behaviors using Mixins.
    """
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.log(f"Profile created for {username}")

def demonstrate_mro():
    print("Demonstrating Multiple Inheritance and MRO in Python:")
    print("=" * 60)

    # 1. Understanding MRO (Method Resolution Order)
    print("\n1. Method Resolution Order (The Diamond Problem):")
    d = Diamond()
    print("MRO for Diamond class:")
    for cls in Diamond.mro():
        print(f"  -> {cls.__name__}")
    
    print("\nCalling d.show():")
    d.show()
    # Note: Even though 'Left' and 'Right' both inherit from 'Base',
    # 'Base.show()' is only called ONCE thanks to Python's C3 Linearization.

    # 2. Using Mixins for flexible component design
    print("\n2. Practical Multi-Inheritance (Mixins):")
    user = UserProfile("python_master", "dev@example.com")
    print(f"JSON Export: {user.to_json()}")
    
    print("\nMRO for UserProfile:")
    print([cls.__name__ for cls in UserProfile.mro()])

    # 3. Super() with arguments
    print("\n3. Inspecting super() behavior:")
    # super() doesn't necessarily call the parent, it calls the NEXT class in the MRO
    print(f"Next in MRO after 'Left' (for a Diamond instance): {super(Left, d).__class__}")

if __name__ == "__main__":
    demonstrate_mro()

    print("\nMultiple Inheritance allows a class to derive features from multiple")
    print("sources. Method Resolution Order (MRO) defines the search order for")
    print("methods. Python uses the C3 Linearization algorithm to ensure that")
    print("base classes are only visited after their children, even in diamonds.")
