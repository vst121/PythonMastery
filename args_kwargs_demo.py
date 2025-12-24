def demonstrate_args_kwargs(*args, **kwargs):
    """
    Function to demonstrate *args and **kwargs.

    *args: Variable number of positional arguments (tuple)
    **kwargs: Variable number of keyword arguments (dictionary)
    """
    print("Demonstrating *args and **kwargs:")
    print(f"Number of positional arguments (*args): {len(args)}")
    print(f"Positional arguments: {args}")

    print(f"Number of keyword arguments (**kwargs): {len(kwargs)}")
    print(f"Keyword arguments: {kwargs}")

    # Example usage: Sum all positional args if they are numbers
    if args:
        try:
            total = sum(args)
            print(f"Sum of positional arguments: {total}")
        except TypeError:
            print("Positional arguments contain non-numeric values, cannot sum.")

    # Example usage: Print key-value pairs
    if kwargs:
        print("Keyword argument details:")
        for key, value in kwargs.items():
            print(f"  {key}: {value}")

def flexible_function(operation, *args, **kwargs):
    """
    A more practical example: Perform operations with flexible arguments.
    """
    print(f"\nPerforming '{operation}' with flexible arguments:")

    if operation == "add":
        result = sum(args)
        print(f"Addition result: {result}")
    elif operation == "multiply":
        result = 1
        for arg in args:
            result *= arg
        print(f"Multiplication result: {result}")
    elif operation == "concatenate":
        result = "".join(str(arg) for arg in args)
        print(f"Concatenation result: {result}")
    else:
        print(f"Unknown operation: {operation}")

    # Use kwargs for additional options
    if "verbose" in kwargs and kwargs["verbose"]:
        print("Verbose mode: All arguments processed successfully.")

if __name__ == "__main__":
    # Basic demonstration
    demonstrate_args_kwargs(1, 2, 3, name="Alice", age=30, city="New York")

    # More examples
    demonstrate_args_kwargs("hello", "world", debug=True, version=1.0)

    # Practical example
    flexible_function("add", 1, 2, 3, 4, verbose=True)
    flexible_function("multiply", 2, 3, 5)
    flexible_function("concatenate", "Python", " ", "is", " ", "awesome")

    print("\n*args and **kwargs allow functions to accept a variable number of arguments,")
    print("making them highly flexible for different use cases, especially in AI and data processing.")