from abc import ABC, abstractmethod
from typing import List

# Strategy Interface
class DiscountStrategy(ABC):
    """Abstract base class for discount strategies."""

    @abstractmethod
    def calculate_discount(self, total_amount: float) -> float:
        """Calculate the discount based on the total amount."""
        pass

# Concrete Strategy 1: Percentage Discount
class PercentageDiscount(DiscountStrategy):
    """A discount strategy that applies a percentage off."""

    def __init__(self, percentage: float):
        self.percentage = percentage

    def calculate_discount(self, total_amount: float) -> float:
        return total_amount * (self.percentage / 100)

# Concrete Strategy 2: Fixed Amount Discount
class FixedAmountDiscount(DiscountStrategy):
    """A discount strategy that subtracts a fixed amount."""

    def __init__(self, amount: float):
        self.amount = amount

    def calculate_discount(self, total_amount: float) -> float:
        # Prevent discount from being greater than the total
        return min(self.amount, total_amount)

# Concrete Strategy 3: No Discount
class NoDiscount(DiscountStrategy):
    """A default strategy that applies no discount."""

    def calculate_discount(self, total_amount: float) -> float:
        return 0.0

# Concrete Strategy 4: Bulk Discount (Conditional Strategy)
class BulkDiscount(DiscountStrategy):
    """A strategy that applies a discount only if total is above threshold."""

    def __init__(self, threshold: float, discount: float):
        self.threshold = threshold
        self.discount = discount

    def calculate_discount(self, total_amount: float) -> float:
        if total_amount >= self.threshold:
            return self.discount
        return 0.0

# Context
class Order:
    """The context class that uses a DiscountStrategy."""

    def __init__(self, customer_name: str, items: List[dict]):
        self.customer_name = customer_name
        self.items = items
        self._discount_strategy: DiscountStrategy = NoDiscount()

    @property
    def total_amount(self) -> float:
        """Calculate the raw total of all items."""
        return sum(item["price"] * item["quantity"] for item in self.items)

    def set_discount_strategy(self, strategy: DiscountStrategy):
        """Change the strategy at runtime."""
        print(f"Applying Strategy: {strategy.__class__.__name__}")
        self._discount_strategy = strategy

    def get_final_total(self) -> float:
        """Calculate the final total after applying the current strategy."""
        discount = self._discount_strategy.calculate_discount(self.total_amount)
        return self.total_amount - discount

    def __str__(self):
        return f"Order for {self.customer_name} | Total: {self.total_amount:.2f} | Final: {self.get_final_total():.2f}"

def run_demo():
    """Main demonstration logic."""
    print("Demonstrating Strategy Design Pattern in Python:")
    print("=" * 60)

    # Sample items
    shopping_cart = [
        {"name": "Laptop", "price": 1200.00, "quantity": 1},
        {"name": "Mouse", "price": 25.50, "quantity": 2},
        {"name": "Keyboard", "price": 80.00, "quantity": 1}
    ]

    my_order = Order("Alice", shopping_cart)
    print(f"Initial State: {my_order}")

    # 1. Apply Percentage Discount
    my_order.set_discount_strategy(PercentageDiscount(10)) # 10% OFF
    print(f"Result: {my_order}\n")

    # 2. Apply Fixed Amount Discount
    my_order.set_discount_strategy(FixedAmountDiscount(50)) # 50 units OFF
    print(f"Result: {my_order}\n")

    # 3. Apply Bulk Discount (Conditional)
    # Total is around 1331, so it should trigger if threshold is 1000
    my_order.set_discount_strategy(BulkDiscount(1000, 100))
    print(f"Result: {my_order}\n")

    # 4. Switch back to No Discount
    my_order.set_discount_strategy(NoDiscount())
    print(f"Result: {my_order}\n")

    print("Key Takeaways:")
    print("- Strategies are interchangeable at runtime.")
    print("- Context (Order) is decoupled from the algorithm implementation.")
    print("- New strategies can be added without modifying the context class (Open/Closed Principle).")

if __name__ == "__main__":
    run_demo()

# The Strategy Design Pattern defines a family of algorithms, encapsulates each one,
# and makes them interchangeable. Strategy lets the algorithm vary independently 
# from clients that use it. In this example, the Order doesn't care HOW the 
# discount is calculated; it just delegates the task to the strategy object.
