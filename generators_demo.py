def fibonacci_generator(n):
    """Generator function that yields the first n Fibonacci numbers."""
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

def square_generator(limit):
    """Generator that yields squares of numbers from 0 up to but not including limit."""
    for i in range(limit):
        yield i ** 2

if __name__ == "__main__":
    print("Demonstrating Generators with yield:")
    print("\nFibonacci sequence (first 10 numbers):")
    fib_gen = fibonacci_generator(10)
    for num in fib_gen:
        print(num, end=" ")
    print()

    print("\nSquares of numbers from 0 to 9:")
    square_gen = square_generator(10)
    for square in square_gen:
        print(square, end=" ")
    print()

    print("\nGenerators are memory-efficient and can be used in loops or with next().")
    print("Example: Using next() on a new generator:")
    fib_gen2 = fibonacci_generator(5)
    print(f"First: {next(fib_gen2)}")
    print(f"Second: {next(fib_gen2)}")
    print(f"Third: {next(fib_gen2)}")