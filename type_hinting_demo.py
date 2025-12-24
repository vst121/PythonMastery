from typing import List, Dict, Optional, Union, Tuple, Any, Callable
import math

# Basic type hints
def greet(name: str) -> str:
    """Function with basic type hints."""
    return f"Hello, {name}!"

def calculate_area(radius: float) -> float:
    """Calculate circle area with type hints."""
    return math.pi * radius ** 2

# Collection type hints
def sum_list(numbers: List[int]) -> int:
    """Sum a list of integers."""
    return sum(numbers)

def create_user_profile(name: str, age: int, hobbies: List[str]) -> Dict[str, Union[str, int, List[str]]]:
    """Create a user profile dictionary."""
    return {
        "name": name,
        "age": age,
        "hobbies": hobbies
    }

# Optional types
def find_user(users: List[Dict[str, Any]], user_id: int) -> Optional[Dict[str, Any]]:
    """Find a user by ID, returns None if not found."""
    for user in users:
        if user.get("id") == user_id:
            return user
    return None

# Union types (or syntax in Python 3.10+)
def process_data(data: Union[str, int, List[str]]) -> str:
    """Process different types of data."""
    if isinstance(data, str):
        return f"String: {data.upper()}"
    elif isinstance(data, int):
        return f"Number: {data * 2}"
    elif isinstance(data, list):
        return f"List length: {len(data)}"
    else:
        return "Unknown type"

# Tuple type hints
def get_coordinates() -> Tuple[float, float]:
    """Return latitude and longitude as a tuple."""
    return (40.7128, -74.0060)  # New York City

# Callable type hints
def apply_function(func: Callable[[int], int], value: int) -> int:
    """Apply a function to a value."""
    return func(value)

# Custom class with type hints
class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def distance_to(self, other: 'Point') -> float:
        """Calculate distance to another point."""
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"

# Generic function
def first_element(items: List[Any]) -> Any:
    """Get the first element of a list."""
    return items[0] if items else None

# Type hints with default values
def configure_system(debug: bool = False, max_connections: Optional[int] = None) -> Dict[str, Any]:
    """Configure system with optional parameters."""
    config = {"debug": debug}
    if max_connections is not None:
        config["max_connections"] = max_connections
    return config

if __name__ == "__main__":
    print("Demonstrating Type Hinting in Python:")
    print("=" * 50)

    # Basic examples
    message = greet("Alice")
    print(f"Greet function: {message}")

    area = calculate_area(5.0)
    print(f"Circle area: {area:.2f}")

    # Collection examples
    numbers = [1, 2, 3, 4, 5]
    total = sum_list(numbers)
    print(f"Sum of {numbers}: {total}")

    profile = create_user_profile("Bob", 30, ["reading", "coding", "gaming"])
    print(f"User profile: {profile}")

    # Optional example
    users = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ]
    user = find_user(users, 1)
    print(f"Found user: {user}")

    missing_user = find_user(users, 3)
    print(f"Missing user: {missing_user}")

    # Union example
    print(process_data("hello"))
    print(process_data(42))
    print(process_data(["a", "b", "c"]))

    # Tuple example
    lat, lon = get_coordinates()
    print(f"Coordinates: {lat}, {lon}")

    # Callable example
    square = lambda x: x ** 2
    result = apply_function(square, 5)
    print(f"5 squared: {result}")

    # Class example
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    distance = p1.distance_to(p2)
    print(f"Distance between {p1} and {p2}: {distance}")

    # Generic example
    first = first_element([10, 20, 30])
    print(f"First element: {first}")

    # Default values example
    config1 = configure_system()
    config2 = configure_system(debug=True, max_connections=100)
    print(f"Default config: {config1}")
    print(f"Custom config: {config2}")

    print("\nType hints improve code readability, enable better IDE support,")
    print("and allow static type checkers like mypy to catch errors early.")
    print("They don't enforce types at runtime in standard Python.")