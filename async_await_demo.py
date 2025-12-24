import asyncio
import time
import random

async def fetch_data(task_id):
    """
    Simulates an asynchronous I/O-bound task (e.g., a database query or network request).
    """
    delay = random.uniform(0.5, 1.5)
    print(f"Task {task_id}: Starting (will take {delay:.2f}s)...")
    
    # asyncio.sleep is a non-blocking sleep (the 'await' gives control back to the event loop)
    await asyncio.sleep(delay)
    
    print(f"Task {task_id}: Completed.")
    return f"Result from {task_id}"

async def process_item(item):
    """
    Another coroutine demonstrating sequential awaiting within a loop.
    """
    print(f"  [AI Processing] Analyzing: {item}")
    await asyncio.sleep(0.3)
    return item.upper()

async def demonstrate_concurrency():
    """
    Main coroutine demonstrating how to run tasks concurrently.
    """
    print("Demonstrating Async / Await in Python:")
    print("=" * 60)

    # 1. Concurrent Execution with asyncio.gather
    print("\n1. Running Tasks Concurrently (asyncio.gather):")
    start_time = time.perf_counter()
    
    # Scheduling multiple coroutines to run 'simultaneously'
    results = await asyncio.gather(
        fetch_data("A"),
        fetch_data("B"),
        fetch_data("C")
    )
    
    end_time = time.perf_counter()
    print(f"\nAll tasks finished in {end_time - start_time:.2f} seconds.")
    print(f"Gathered Results: {results}")

    # 2. Sequential Await vs Concurrent (Comparison)
    print("\n2. Sequential Awaiting (Looping):")
    items = ["data_chunk_1", "data_chunk_2", "data_chunk_3"]
    processed_items = []
    
    for item in items:
        # This waits for each one to finish before starting the next
        result = await process_item(item)
        processed_items.append(result)
    
    print(f"Processed results: {processed_items}")

    # 3. Handling Exceptions in Async Blocks
    print("\n3. Handling Async Exceptions:")
    async def risky_task():
        await asyncio.sleep(0.2)
        raise ValueError("Something went wrong in the async task!")

    try:
        await risky_task()
    except ValueError as e:
        print(f"Caught expected error: {e}")

if __name__ == "__main__":
    # asyncio.run() is the standard entry point for async programs
    # It creates the event loop and manages its lifecycle.
    try:
        asyncio.run(demonstrate_concurrency())
    except KeyboardInterrupt:
        pass

    print("\nAsync/Await allows Python to handle many I/O-bound tasks concurrently")
    print("without the overhead of multiple threads. This is the foundation of")
    print("modern high-performance web servers (FastAPI) and AI data pipelines.")
