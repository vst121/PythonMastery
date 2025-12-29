from abc import ABC, abstractmethod
from typing import Optional

# Base Handler Instance
class SupportHandler(ABC):
    """Abstract base class for the Chain of Responsibility."""
    
    def __init__(self):
        self._next_handler: Optional[SupportHandler] = None

    def set_next(self, handler: 'SupportHandler') -> 'SupportHandler':
        """Set the next handler in the chain and return it to allow chaining."""
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: str, level: int) -> bool:
        """Handle the request. Returns True if handled, False otherwise."""
        if self._next_handler:
            return self._next_handler.handle(request, level)
        
        print(f"Request '{request}' (Level {level}) could not be handled.")
        return False

# Concrete Handler 1: Junior Support
class JuniorSupport(SupportHandler):
    """Handles basic requests (Level 1)."""
    
    def handle(self, request: str, level: int) -> bool:
        if level <= 1:
            print(f"[Junior Support] Handled: {request}")
            return True
        return super().handle(request, level)

# Concrete Handler 2: Senior Support
class SeniorSupport(SupportHandler):
    """Handles intermediate requests (Level 2)."""
    
    def handle(self, request: str, level: int) -> bool:
        if level <= 2:
            print(f"[Senior Support] Handled: {request}")
            return True
        return super().handle(request, level)

# Concrete Handler 3: Technical Lead
class TechnicalLead(SupportHandler):
    """Handles complex technical requests (Level 3)."""
    
    def handle(self, request: str, level: int) -> bool:
        if level <= 3:
            print(f"[Technical Lead] Handled: {request}")
            return True
        return super().handle(request, level)

# Concrete Handler 4: Manager
class Manager(SupportHandler):
    """Handles critical or administrative requests (Level 4)."""
    
    def handle(self, request: str, level: int) -> bool:
        if level <= 4:
            print(f"[Manager] Handled: {request}")
            return True
        return super().handle(request, level)

def run_demo():
    """Main demonstration logic."""
    print("Demonstrating Chain of Responsibility Design Pattern in Python:")
    print("=" * 60)

    # 1. Setup the Chain
    # Junior -> Senior -> Tech Lead -> Manager
    junior = JuniorSupport()
    senior = SeniorSupport()
    lead = TechnicalLead()
    manager = Manager()

    junior.set_next(senior).set_next(lead).set_next(manager)

    # 2. Define various requests
    requests = [
        ("Change password", 1),
        ("Advanced configuration", 2),
        ("Database optimization", 3),
        ("Budget approval", 4),
        ("Company acquisition", 10)  # Level too high for the chain
    ]

    # 3. Process requests starting from the first handler
    for description, level in requests:
        print(f"Submitting Request: '{description}' (Level {level})")
        junior.handle(description, level)
        print("-" * 30)

    print("\nKey Takeaways:")
    print("- Decouples the sender of a request from its receivers.")
    print("- Multiple objects are given a chance to handle the request.")
    print("- You can dynamicallly re-order the chain or add/remove handlers.")
    print("- Promotes Single Responsibility and Open/Closed principles.")

if __name__ == "__main__":
    run_demo()

# The Chain of Responsibility pattern creates a chain of receiver objects for a 
# request. This pattern decouples the sender and receiver of a request based 
# on the type of request. Each handler contains a reference to another handler. 
# If one object cannot handle the request, it passes it to the next handler.
