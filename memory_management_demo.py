import sys
import gc
import ctypes

class LargeObject:
    """
    A class to demonstrate object lifecycle.
    The __del__ method is called when the object's reference count reaches zero.
    """
    def __init__(self, name):
        self.name = name
        print(f"  [Memory] Allocated: {self.name}")

    def __del__(self):
        print(f"  [Memory] Deallocated: {self.name}")

def ref_count(address):
    """Utility to get reference count at a specific memory address."""
    return ctypes.c_long.from_address(address).value

def demonstrate_memory_management():
    print("Demonstrating Memory Management & Garbage Collection in Python:")
    print("=" * 65)

    # 1. Reference Counting
    print("\n1. Reference Counting (Standard behavior):")
    obj1 = LargeObject("Object_1")
    obj_address = id(obj1)
    
    print(f"   Initial ref count: {sys.getrefcount(obj1) - 1}") # -1 because getrefcount creates a temp ref
    
    obj2 = obj1
    print(f"   Ref count after adding obj2: {sys.getrefcount(obj1) - 1}")
    
    print("   Deleting obj1 and obj2 references...")
    del obj1
    del obj2 # Object_1 should be deallocated here immediately
    
    # 2. Circular References (The limit of Reference Counting)
    print("\n2. The Diamond Problem: Circular References:")
    class Node:
        def __init__(self, name):
            self.name = name
            self.link = None
        def __del__(self):
            print(f"  [GC] Dead node collected: {self.name}")

    node_a = Node("Node_A")
    node_b = Node("Node_B")
    
    # Create a circular reference
    node_a.link = node_b
    node_b.link = node_a
    
    print("   Created circular reference: A -> B -> A")
    
    # Delete the local variables
    print("   Deleting local variables node_a and node_b...")
    del node_a
    del node_b
    
    # Notice that the objects ARE NOT DEALLOCATED yet because they still reference each other
    print("   (Objects still exist in memory due to the cycle!)")

    # 3. Manual Garbage Collection
    print("\n3. Triggering Manual Garbage Collection:")
    print("   Running gc.collect()...")
    collected = gc.collect()
    print(f"   Garbage collector finished. Objects collected: {collected}")

    # 4. GC Generations
    print("\n4. Understanding GC Generations:")
    # Python uses 3 generations (0, 1, 2). Objects that survive a collection move up.
    print(f"   Current GC Thresholds (Gen 0, 1, 2): {gc.get_threshold()}")
    print(f"   Current GC Counts: {gc.get_count()}")

if __name__ == "__main__":
    # Disable automatic GC for a moment to clearly show the circular reference issue
    gc.disable()
    try:
        demonstrate_memory_management()
    finally:
        gc.enable()

    print("\nPython primarily uses Reference Counting for memory management.")
    print("When the count hits zero, the object is freed immediately. To handle")
    print("circular references, Python uses a Cyclic Garbage Collector that")
    print("periodically scans for and destroys unreachable clusters of objects.")
