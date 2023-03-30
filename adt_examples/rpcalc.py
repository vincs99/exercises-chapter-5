"""Implement reverse polish calculator."""
from numbers import Number
import math


class RPCalc:
    """Do it in this class."""

    def __init__(self):
        self.stack = []
        self.binops = {"*", "/", "+", "-"}
        self.monops = {"sin", "cos"}

    def push(self, n):
        """Push numbers or do operations."""
        if isinstance(n, Number):
            self.stack.append(n)
            #print(self.stack)
        elif n in self.binops:
            second = self.pop()
            first = self.pop()
            self.stack.append(float(eval(f"{first}"+n+f"{second}")))
            #print(self.stack)
        elif n in self.monops:
            only = self.pop()
            self.stack.append(float(eval("math."+n+f"({only})")))  
            #print(self.stack)

    def pop(self):
        """Pops."""
        if len(self.stack):
            return self.stack.pop()

    def peek(self):
        """Return the top value."""
        return self.stack[-1]

    def __len__(self):
        """Return lenth."""
        return len(self.stack)
