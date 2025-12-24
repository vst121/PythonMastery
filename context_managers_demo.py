import time
from contextlib import contextmanager

class DatabaseConnection:
    """
    A class-based context manager simulating a database connection.
    Demonstrates the use of __enter__ and __exit__ dunder methods.
    """
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        """
        Setup phase: Executed when entering the 'with' block.
        Returns the resource to be used.
        """
        print(f"Connecting to database: '{self.db_name}'...")
        # Simulating connection setup
        return self

    def query(self, sql):
        """Simulate a database query."""
        print(f"Executing SQL on '{self.db_name}': {sql}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Teardown phase: Executed when leaving the 'with' block.
        Handles cleanup and potential exceptions.
        """
        print(f"Closing connection to database: '{self.db_name}'")
        if exc_type:
            print(f"  [!] An exception occurred: {exc_val}")
        
        # Returning False allows exceptions to propagate
        # Returning True would suppress them
        return False

@contextmanager
def execution_timer(task_name):
    """
    A function-based context manager using the @contextmanager decorator.
    A more concise way to create context managers for simple use cases.
    """
    print(f"\n>>> Starting Timer for: {task_name}")
    start_time = time.time()
    try:
        # The 'yield' expression divides 'setup' from 'teardown'
        yield
    finally:
        # Code here runs even if an exception occurs in the 'with' block
        end_time = time.time()
        duration = end_time - start_time
        print(f">>> Timer for {task_name} finished. Duration: {duration:.4f} seconds")

def demonstrate_context_managers():
    """
    Run demonstrations for different types of context managers.
    """
    print("Demonstrating Context Managers in Python:")
    print("=" * 50)

    # 1. Using a class-based context manager
    print("\n1. Class-based Context Manager Example:")
    with DatabaseConnection("UserDB") as db:
        db.query("SELECT * FROM users")
        db.query("UPDATE users SET last_login = NOW()")
    # 'db' connection is automatically closed here

    # 2. Using a function-based context manager
    print("\n2. Function-based Context Manager Example:")
    with execution_timer("Expensive AI Computation"):
        print("   Performing heavy processing...")
        time.sleep(0.5)
        print("   Processing complete.")

    # 3. Handling exceptions within context managers
    print("\n3. Handling Exceptions Example:")
    try:
        with DatabaseConnection("OrdersDB") as db:
            print("   Processing orders...")
            db.query("SELECT * FROM orders")
            # Simulating an error
            raise RuntimeError("Database connection lost unexpectedly!")
    except RuntimeError as e:
        print(f"   Caught runtime error in main block: {e}")

if __name__ == "__main__":
    demonstrate_context_managers()

    print("\nContext Managers (the 'with' statement) ensure that resources are")
    print("properly managed, handling both successful execution and exceptions.")
    print("They are critical for building robust and memory-efficient AI applications,")
    print("especially when dealing with file streams, GPUs, or network sockets.")
