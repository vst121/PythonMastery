from abc import ABC, abstractmethod

# Target Interface: What the client expects
class ModernUSBSocket(ABC):
    """The Target interface that the client code uses."""
    
    @abstractmethod
    def connect_usb(self) -> str:
        pass

# Adaptee: The incompatible interface that needs adapting
class LegacySerialDevice:
    """An existing interface that is incompatible with the Target."""
    
    def connect_serial_pin(self) -> str:
        return "Connected via old 9-pin Serial Port."

# Adapter: Bridges the gap
class SerialToUSBAdapter(ModernUSBSocket):
    """
    The Adapter makes the Legacy interface compatible with the Modern interface.
    It wraps the Legacy object and translates the calls.
    """
    
    def __init__(self, legacy_device: LegacySerialDevice):
        self.legacy_device = legacy_device

    def connect_usb(self) -> str:
        # Translate the modern request into a legacy call
        print("[Adapter] Translating USB signal to Serial...")
        legacy_response = self.legacy_device.connect_serial_pin()
        return f"Converted: {legacy_response}"

# Client Code
def computer_usb_port(device: ModernUSBSocket):
    """The client only knows how to talk to ModernUSBSocket."""
    print(f"Computer: Attempting to connect device...")
    status = device.connect_usb()
    print(f"Status: {status}")

def run_demo():
    """Main demonstration logic."""
    print("Demonstrating Adapter Design Pattern in Python:")
    print("=" * 60)

    # 1. We have a legacy device
    old_printer = LegacySerialDevice()
    print(f"Step 1: We have an old Serial Printer, but the computer only has USB.")
    
    # 2. Trying to plug it in directly would fail (in static languages) 
    # or just be incompatible with the expected API.
    # computer_usb_port(old_printer) # This would raise AttributeError: 'LegacySerialDevice' has no attribute 'connect_usb'

    # 3. Use an Adapter to bridge the gap
    print("\nStep 2: Connecting the printer using an Adapter.")
    adapter = SerialToUSBAdapter(old_printer)
    
    # 4. Now the computer can talk to it
    computer_usb_port(adapter)

    print("\nKey Takeaways:")
    print("- Allows incompatible interfaces to work together.")
    print("- Wraps an existing class with a new interface.")
    print("- Useful for integrating legacy code or 3rd-party libraries without modifying them.")
    print("- Follows the 'Wrapper' concept, similar to Decorators but focuses on interface conversion.")

if __name__ == "__main__":
    run_demo()

# The Adapter Pattern acts as a bridge between two incompatible interfaces. 
# This pattern involves a single class which is responsible to join functionalities 
# of independent or incompatible interfaces. A real-life example could be a 
# card reader which acts as an adapter between memory card and a laptop.
