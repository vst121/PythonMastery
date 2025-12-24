from abc import ABC, abstractmethod
import time
import os

# Subject Interface
class DataSource(ABC):
    """Abstract interface for data sources."""

    @abstractmethod
    def read_data(self) -> str:
        """Read data from the source."""
        pass

    @abstractmethod
    def write_data(self, data: str) -> None:
        """Write data to the source."""
        pass

# Real Subject
class RealFileDataSource(DataSource):
    """Real implementation that actually reads/writes files."""

    def __init__(self, filename: str):
        self.filename = filename
        print(f"RealFileDataSource: Opening file {filename}")

    def read_data(self) -> str:
        print(f"RealFileDataSource: Reading from {self.filename}")
        try:
            with open(self.filename, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return ""

    def write_data(self, data: str) -> None:
        print(f"RealFileDataSource: Writing to {self.filename}")
        with open(self.filename, 'w') as file:
            file.write(data)

# Virtual Proxy - Lazy Loading
class LazyFileDataSource(DataSource):
    """Virtual proxy that creates the real object only when needed."""

    def __init__(self, filename: str):
        self.filename = filename
        self._real_datasource = None
        print(f"LazyFileDataSource: Proxy created for {filename} (not opened yet)")

    def _get_real_datasource(self) -> RealFileDataSource:
        """Lazy initialization of the real data source."""
        if self._real_datasource is None:
            print(f"LazyFileDataSource: Initializing real data source for {self.filename}")
            self._real_datasource = RealFileDataSource(self.filename)
        return self._real_datasource

    def read_data(self) -> str:
        return self._get_real_datasource().read_data()

    def write_data(self, data: str) -> None:
        self._get_real_datasource().write_data(data)

# Protection Proxy - Access Control
class ProtectedFileDataSource(DataSource):
    """Protection proxy that controls access based on user permissions."""

    def __init__(self, datasource: DataSource, user_role: str):
        self._datasource = datasource
        self.user_role = user_role
        self.allowed_roles = ["admin", "editor"]

    def _check_permission(self, operation: str) -> bool:
        """Check if the user has permission for the operation."""
        if self.user_role not in self.allowed_roles:
            print(f"ProtectedFileDataSource: Access denied for {self.user_role} - {operation} not allowed")
            return False
        print(f"ProtectedFileDataSource: Access granted for {self.user_role} - {operation}")
        return True

    def read_data(self) -> str:
        if self._check_permission("read"):
            return self._datasource.read_data()
        return "Access denied"

    def write_data(self, data: str) -> None:
        if self._check_permission("write"):
            self._datasource.write_data(data)
        else:
            print("Write operation blocked")

# Smart Proxy - Caching and Logging
class SmartFileDataSource(DataSource):
    """Smart proxy that adds caching and logging functionality."""

    def __init__(self, datasource: DataSource):
        self._datasource = datasource
        self._cache = {}
        self._access_log = []

    def read_data(self) -> str:
        cache_key = "read_data"
        if cache_key in self._cache:
            print("SmartFileDataSource: Returning cached data")
            self._log_access("read", "cache")
            return self._cache[cache_key]

        print("SmartFileDataSource: Reading fresh data")
        data = self._datasource.read_data()
        self._cache[cache_key] = data
        self._log_access("read", "fresh")
        return data

    def write_data(self, data: str) -> None:
        print("SmartFileDataSource: Writing data and clearing cache")
        self._datasource.write_data(data)
        self._cache.clear()  # Invalidate cache on write
        self._log_access("write", "direct")

    def _log_access(self, operation: str, source: str) -> None:
        """Log access operations."""
        timestamp = time.strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {operation} from {source}"
        self._access_log.append(log_entry)

    def get_access_log(self) -> list:
        """Get the access log."""
        return self._access_log.copy()

# Client code
def demonstrate_proxy(proxy: DataSource, name: str) -> None:
    """Demonstrate proxy functionality."""
    print(f"\n--- Demonstrating {name} ---")

    # Read data
    data = proxy.read_data()
    print(f"Read data: '{data}'")

    # Write data
    proxy.write_data("Hello, Proxy Pattern!")

    # Read again
    data = proxy.read_data()
    print(f"Read data again: '{data}'")

if __name__ == "__main__":
    print("Demonstrating Proxy Design Pattern in Python:")
    print("=" * 60)

    filename = "test_file.txt"

    # Clean up any existing file
    if os.path.exists(filename):
        os.remove(filename)

    # Virtual Proxy demonstration
    print("\n1. Virtual Proxy (Lazy Loading):")
    lazy_proxy = LazyFileDataSource(filename)
    demonstrate_proxy(lazy_proxy, "Lazy Proxy")

    # Protection Proxy demonstration
    print("\n2. Protection Proxy (Access Control):")
    real_ds = RealFileDataSource(filename)
    protected_admin = ProtectedFileDataSource(real_ds, "admin")
    protected_guest = ProtectedFileDataSource(real_ds, "guest")

    print("Admin access:")
    demonstrate_proxy(protected_admin, "Protected Proxy (Admin)")

    print("\nGuest access:")
    demonstrate_proxy(protected_guest, "Protected Proxy (Guest)")

    # Smart Proxy demonstration
    print("\n3. Smart Proxy (Caching and Logging):")
    smart_proxy = SmartFileDataSource(RealFileDataSource(filename))
    demonstrate_proxy(smart_proxy, "Smart Proxy")

    print("\nAccess log:")
    for entry in smart_proxy.get_access_log():
        print(f"  {entry}")

    # Clean up
    if os.path.exists(filename):
        os.remove(filename)

    print("\nThe Proxy Pattern provides a surrogate that controls access")
    print("to another object, adding functionality like lazy loading,")
    print("access control, caching, and logging without changing the original object.")