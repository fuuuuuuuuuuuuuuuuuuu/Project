def deco(color: str):
    """
    Decorator that wraps a function's return value in ANSI color codes.

    Args:
        color (str): One of 'red', 'green', 'yellow', 'blue'.
    """
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "reset": "\033[0m"
    }
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            # Apply coloring only to strings or lists of strings
            if isinstance(result, str):
                return f"{colors.get(color, '')}{result}{colors['reset']}"
            if isinstance(result, list):
                return [f"{colors.get(color, '')}{line}{colors['reset']}" for line in result]
            return result
        return wrapper
    return decorator
