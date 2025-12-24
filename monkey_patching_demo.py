import time

class ExternalAIModel:
    """
    Simulates a 3rd-party library class that we cannot modify directly.
    """
    def predict(self, input_data):
        print(f"  [ExternalModel] Processing '{input_data}'...")
        # Imagine this is an expensive network call
        time.sleep(1)
        return f"Prediction for {input_data}"

def patched_predict(self, input_data):
    """
    Our new function that will replace the original 'predict' method.
    This demonstrates injecting custom logic (like logging or caching) 
    into an existing class at runtime.
    """
    print(f"  [PATCHED] Intercepted call with data: {input_data}")
    # We can still call the original logic if we saved it elsewhere, 
    # but here we'll just return a faster mock result.
    return f"FAST Prediction for {input_data}"

def demonstrate_monkey_patching():
    print("Demonstrating Monkey Patching in Python:")
    print("=" * 60)

    # 1. Behavior BEFORE patching
    print("\n1. Original Behavior:")
    model = ExternalAIModel()
    start = time.time()
    result1 = model.predict("Query A")
    print(f"Result: {result1} (Took {time.time() - start:.2f}s)")

    # 2. Applying the Monkey Patch
    # We replace the class's method with our standalone function at runtime.
    print("\n2. Applying Monkey Patch (Changing ExternalAIModel.predict)...")
    ExternalAIModel.predict = patched_predict

    # 3. Behavior AFTER patching
    print("\n3. Patched Behavior:")
    start = time.time()
    result2 = model.predict("Query B")
    print(f"Result: {result2} (Took {time.time() - start:.2f}s)")
    
    # 4. Patching built-in modules (Commonly used in testing/mocking)
    print("\n4. Patching Module-level functions (Simulating 'time.sleep' skip):")
    original_sleep = time.sleep
    time.sleep = lambda x: print(f"  [PATCH] Suppressed sleep for {x} seconds.")
    
    start = time.perf_counter()
    time.sleep(100) # This would normally take 100 seconds!
    print(f"Execution continued immediately. Duration: {time.perf_counter() - start:.4f}s")
    
    # Restore for safety
    time.sleep = original_sleep

if __name__ == "__main__":
    demonstrate_monkey_patching()

    print("\nMonkey Patching is the technique of replacing or extending code")
    print("at runtime without modifying the source. It is extremely powerful")
    print("for unit testing (mocking) and fixing bugs in third-party libraries,")
    print("but should be used sparingly as it can make debugging difficult.")
