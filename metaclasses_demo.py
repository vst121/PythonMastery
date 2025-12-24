import time

class MetaMaster(type):
    """
    A custom Metaclass (the 'Master' class that creates other classes).
    In Python, classes are objects too, and their type is a metaclass.
    """
    
    def __new__(mcs, name, bases, attrs):
        """
        Intercepts class creation BEFORE the class object is created.
        Useful for modifying class attributes or validating structure.
        """
        print(f"\n[Metaclass] Creating class: {name}")
        
        # Example 1: Force all method names to be lowercase (Masterclass enforcement)
        new_attrs = {}
        for attr_name, attr_value in attrs.items():
            if not attr_name.startswith("__") and callable(attr_value):
                if not attr_name.islower():
                    print(f"  [!] Warning: Renaming '{attr_name}' to '{attr_name.lower()}' to follow standards.")
                    new_attrs[attr_name.lower()] = attr_value
                else:
                    new_attrs[attr_name] = attr_value
            else:
                new_attrs[attr_name] = attr_value
                
        # Example 2: Add a 'creation_time' to every class created with this metaclass
        new_attrs['creation_timestamp'] = time.time()
        
        return super().__new__(mcs, name, bases, new_attrs)

    def __init__(cls, name, bases, attrs):
        """
        Executes AFTER the class object has been created.
        """
        print(f"[Metaclass] Initializing class object: {name}")
        super().__init__(name, bases, attrs)

    def __call__(cls, *args, **kwargs):
        """
        Intercepts CLASS INSTANTIATION (when you do v = MyClass()).
        """
        print(f"[Metaclass] Intercepting instantiation of {cls.__name__}...")
        instance = super().__call__(*args, **kwargs)
        return instance

# --- Practical Example 1: Registry Pattern ---

class PluginRegistry(type):
    """Metaclass that automatically registers all subclasses."""
    plugins = {}

    def __new__(mcs, name, bases, attrs):
        new_cls = super().__new__(mcs, name, bases, attrs)
        if name != "BasePlugin":
            mcs.plugins[name] = new_cls
        return new_cls

class BasePlugin(metaclass=PluginRegistry):
    def run(self):
        raise NotImplementedError

class DataFilterPlugin(BasePlugin):
    def run(self):
        return "Filtering data..."

class EncryptionPlugin(BasePlugin):
    def run(self):
        return "Encrypting payload..."

# --- Demonstration ---

def demonstrate_metaclasses():
    print("Demonstrating Python Metaclasses (Metaprogramming):")
    print("=" * 55)

    # 1. Using our custom MetaMaster
    print("\n1. Custom Metaclass Enforcement:")
    class MyComponent(metaclass=MetaMaster):
        def DoSomething(self):  # Note the PascalCase (violates our 'lower' rule)
            return "Doing something!"
        
        def say_hello(self):
            return "Hello!"

    component = MyComponent()
    
    # Check if the method was renamed
    print(f"\nMethod 'DoSomething' exists? {hasattr(component, 'DoSomething')}")
    print(f"Method 'dosomething' exists? {hasattr(component, 'dosomething')}")
    print(f"Class created at: {component.creation_timestamp}")

    # 2. Registry Pattern Demo
    print("\n2. Plugin Registry Pattern:")
    print(f"Registered Plugins: {list(PluginRegistry.plugins.keys())}")
    
    for name, plugin_cls in PluginRegistry.plugins.items():
        p = plugin_cls()
        print(f"  Executing {name}: {p.run()}")

    # 3. Dynamic Class Creation (Using type() directly)
    print("\n3. Dynamic Class Creation using type():")
    DynamicClass = type("DynamicClass", (object,), {"attribute": 42, "greet": lambda self: "I was born dynamically!"})
    
    dc = DynamicClass()
    print(f"Class Name: {dc.__class__.__name__}")
    print(f"Attribute: {dc.attribute}")
    print(f"Greet: {dc.greet()}")

if __name__ == "__main__":
    demonstrate_metaclasses()

    print("\nMetaclasses are 'classes of classes'. They allow you to control")
    print("how classes are built, validated, and registered. This is the")
    print("highest level of Python OOP and is used by frameworks like")
    print("Django (for Models), Pydantic, and SQLAlchemy.")
