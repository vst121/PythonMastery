from abc import ABC, abstractmethod
from typing import List

# Receiver: The object that performs the actual work
class Light:
    """The Receiver class that knows how to perform operations."""
    
    def __init__(self, name: str):
        self.name = name
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"[{self.name}] Light is now ON")

    def turn_off(self):
        self.is_on = False
        print(f"[{self.name}] Light is now OFF")

# Command Interface
class Command(ABC):
    """The Command abstract base class."""
    
    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass

# Concrete Commands
class LightOnCommand(Command):
    """Command to turn on a light."""
    
    def __init__(self, light: Light):
        self.light = light

    def execute(self) -> None:
        self.light.turn_on()

    def undo(self) -> None:
        self.light.turn_off()

class LightOffCommand(Command):
    """Command to turn off a light."""
    
    def __init__(self, light: Light):
        self.light = light

    def execute(self) -> None:
        self.light.turn_off()

    def undo(self) -> None:
        self.light.turn_on()

class MacroCommand(Command):
    """A Command that executes a sequence of other commands."""
    
    def __init__(self, commands: List[Command]):
        self.commands = commands

    def execute(self) -> None:
        print("--- Executing Macro ---")
        for command in self.commands:
            command.execute()

    def undo(self) -> None:
        print("--- Undoing Macro ---")
        for command in reversed(self.commands):
            command.undo()

# Invoker: The object that requests the command to be executed
class SimpleRemoteControl:
    """The Invoker class that triggers commands and manages history for undo."""
    
    def __init__(self):
        self.history = []

    def press_button(self, command: Command):
        """Execute a command and save it to history."""
        command.execute()
        self.history.append(command)

    def press_undo(self):
        """Undo the last executed command."""
        if self.history:
            command = self.history.pop()
            print(f"Undoing: {command.__class__.__name__}")
            command.undo()
        else:
            print("Nothing to undo.")

def run_demo():
    """Main demonstration logic."""
    print("Demonstrating Command Design Pattern in Python:")
    print("=" * 60)

    # 1. Setup Receivers
    living_room_light = Light("Living Room")
    kitchen_light = Light("Kitchen")

    # 2. Setup Commands
    lr_on = LightOnCommand(living_room_light)
    lr_off = LightOffCommand(living_room_light)
    kitchen_on = LightOnCommand(kitchen_light)
    kitchen_off = LightOffCommand(kitchen_light)

    # 3. Setup Invoker
    remote = SimpleRemoteControl()

    # 4. Demonstrate Single Commands
    print("Step 1: Operating individual lights")
    remote.press_button(lr_on)
    remote.press_button(kitchen_on)
    print()

    # 5. Demonstrate Undo
    print("Step 2: Testing Undo")
    remote.press_undo() # Should turn off Kitchen light
    print()

    # 6. Demonstrate Macro Command (Party Mode)
    print("Step 3: Macro Command (Party Mode - All Lights ON)")
    party_mode = MacroCommand([lr_on, kitchen_on])
    remote.press_button(party_mode)
    print()

    # 7. Undo Macro
    print("Step 4: Undoing Macro")
    remote.press_undo()
    print()

    print("Key Takeaways:")
    print("- Decouples the object that invokes the operation from the one that knows how to perform it.")
    print("- Commands are first-class objects; they can be stored, passed, and manipulated.")
    print("- Enables complex features like undo/redo and macro recording.")
    print("- New commands can be added without changing existing code (Open/Closed Principle).")

if __name__ == "__main__":
    run_demo()

# The Command Design Pattern encapsulates a request as an object, thereby letting 
# you parameterize clients with different requests, queue or log requests, 
# and support undoable operations. It's widely used in UI frameworks for 
# button actions and in systems requiring transactional history.
