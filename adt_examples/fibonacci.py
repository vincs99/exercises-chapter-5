"""Make an interable Fibonacci module."""

class Fib:
    """Make it really."""

    def __init__(self):
        self.before = 0
        self.value = 1

    def __iter__(self):
        """Create basic iterator."""
        return self

    def __next__(self):
        """Recursively define the next Fibonacci."""
        c = self.before + self.value
        self.before = self.value
        self.value = c
        return c
