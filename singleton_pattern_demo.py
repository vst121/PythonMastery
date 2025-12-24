import threading
import time
from typing import Optional, Any

# Method 1: Using __new__ method
class SingletonMeta(type):
    """Metaclass for creating Singleton classes."""

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Logger(metaclass=SingletonMeta):
    """Logger singleton using metaclass approach."""

    def __init__(self, name: str = "DefaultLogger"):
        self.name = name
        self.logs = []
        print(f"Logger '{self.name}' initialized")

    def log(self, message: str, level: str = "INFO") -> None:
        """Log a message."""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {level}: {message}"
        self.logs.append(log_entry)
        print(log_entry)

    def get_logs(self) -> list:
        """Get all logged messages."""
        return self.logs.copy()

# Method 2: Using class variable and __new__
class DatabaseConnection:
    """Database connection singleton using __new__ approach."""

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("Creating new database connection...")
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, host: str = "localhost", port: int = 5432):
        # __init__ is called every time, but we only set attributes once
        if not hasattr(self, 'initialized'):
            self.host = host
            self.port = port
            self.connected = False
            self.initialized = True
            print(f"Database connection configured for {host}:{port}")

    def connect(self) -> None:
        """Simulate database connection."""
        if not self.connected:
            print(f"Connecting to database at {self.host}:{self.port}")
            time.sleep(0.5)  # Simulate connection time
            self.connected = True
            print("Connected successfully!")
        else:
            print("Already connected")

    def disconnect(self) -> None:
        """Simulate disconnection."""
        if self.connected:
            print("Disconnecting from database...")
            self.connected = False
            print("Disconnected")
        else:
            print("Not connected")

    def execute_query(self, query: str) -> str:
        """Simulate query execution."""
        if not self.connected:
            return "Error: Not connected to database"
        return f"Executed: {query} -> Result: Mock data"

# Method 3: Decorator approach
def singleton(cls):
    """Decorator to make a class singleton."""
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

@singleton
class ConfigurationManager:
    """Configuration manager singleton using decorator."""

    def __init__(self, config_file: str = "config.json"):
        self.config_file = config_file
        self.settings = {}
        self._load_config()
        print(f"ConfigurationManager initialized with {config_file}")

    def _load_config(self) -> None:
        """Simulate loading configuration."""
        # In real implementation, this would load from file
        self.settings = {
            "debug": True,
            "max_connections": 100,
            "timeout": 30
        }

    def get_setting(self, key: str) -> Any:
        """Get a configuration setting."""
        return self.settings.get(key, None)

    def set_setting(self, key: str, value: Any) -> None:
        """Set a configuration setting."""
        self.settings[key] = value
        print(f"Setting updated: {key} = {value}")

# Thread-safe singleton (for demonstration)
class ThreadSafeSingleton:
    """Thread-safe singleton implementation."""

    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                # Double-check locking
                if cls._instance is None:
                    print("Creating thread-safe singleton instance...")
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value: str = "default"):
        if not hasattr(self, 'initialized'):
            self.value = value
            self.initialized = True
            print(f"ThreadSafeSingleton initialized with value: {value}")

# Demonstration functions
def demonstrate_logger() -> None:
    """Demonstrate Logger singleton."""
    print("\n--- Logger Singleton ---")

    logger1 = Logger("AppLogger")
    logger2 = Logger("DifferentName")  # This should return the same instance

    print(f"Same instance? {logger1 is logger2}")
    print(f"Logger name: {logger1.name}")  # Will be "AppLogger" from first call

    logger1.log("Application started")
    logger1.log("Processing data", "DEBUG")
    logger1.log("Error occurred", "ERROR")

    print(f"Total logs: {len(logger1.get_logs())}")

def demonstrate_database() -> None:
    """Demonstrate DatabaseConnection singleton."""
    print("\n--- Database Connection Singleton ---")

    db1 = DatabaseConnection("prod-db", 5432)
    db2 = DatabaseConnection("dev-db", 3306)  # Should return same instance

    print(f"Same instance? {db1 is db2}")
    print(f"Host: {db1.host}, Port: {db1.port}")  # Will be from first call

    db1.connect()
    db2.connect()  # Should show already connected

    result = db1.execute_query("SELECT * FROM users")
    print(result)

    db1.disconnect()

def demonstrate_config() -> None:
    """Demonstrate ConfigurationManager singleton."""
    print("\n--- Configuration Manager Singleton ---")

    config1 = ConfigurationManager("app_config.json")
    config2 = ConfigurationManager("other_config.json")  # Same instance

    print(f"Same instance? {config1 is config2}")
    print(f"Config file: {config1.config_file}")  # From first call

    print(f"Debug setting: {config1.get_setting('debug')}")
    config1.set_setting("new_setting", "value")
    print(f"New setting: {config2.get_setting('new_setting')}")  # Accessible from both

def demonstrate_thread_safe() -> None:
    """Demonstrate thread-safe singleton."""
    print("\n--- Thread-Safe Singleton ---")

    def create_singleton(value):
        singleton = ThreadSafeSingleton(value)
        print(f"Thread {threading.current_thread().name}: {singleton.value}")

    # Create multiple threads trying to create singleton
    threads = []
    for i in range(3):
        thread = threading.Thread(target=create_singleton, args=(f"value_{i}",))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    # Verify only one instance exists
    s1 = ThreadSafeSingleton()
    s2 = ThreadSafeSingleton()
    print(f"Final check - Same instance? {s1 is s2}")

if __name__ == "__main__":
    print("Demonstrating Singleton Design Pattern in Python:")
    print("=" * 60)

    demonstrate_logger()
    demonstrate_database()
    demonstrate_config()
    demonstrate_thread_safe()

    print("\nThe Singleton Pattern ensures a class has only one instance")
    print("and provides a global point of access to that instance.")
    print("Common uses: loggers, database connections, configuration managers.")