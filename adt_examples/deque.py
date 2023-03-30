"""Implementing deque."""


class Deque:
    """Do it in this class."""

    def __init__(self, val):
        self.n = val
        self.holder = [None]*val
        self.start = 0
        self.end = 0
        self.length = 0

    def append(self, x):
        """Appending to the end."""
        self.holder[self.end] = x
        self.end = (self.end + 1) % self.n
        self.length = self.length + 1

    def appendleft(self, x):
        """Appending to the beginning."""
        self.start = (self.start - 1) % self.n
        self.holder[self.start] = x
        self.length += 1

    def pop(self): 
        """Remove the last item, if exists."""
        if self.length:
            self.end = (self.end - 1) % self.n
            out = self.holder[self.end]
            self.holder[self.end] = None
            self.length -= 1
            return out

    def popleft(self):
        """Remove first item if exists."""
        if self.length:
            out = self.holder[self.start]
            self.holder[self.start] = None
            self.start = (self.start + 1) % self.n
            self.length -= 1
            return out

    def peek(self):
        """Return last item without remove."""
        return self.holder[(self.end - 1) % self.n]
    
    def peekleft(self):
        """Return first item without remove."""
        return self.holder[self.start]
    
    def __len__(self):
        """Return length."""
        return self.length
    
    def __iter__(self):
        return DequeIterator(self)
    

class DequeIterator:
    """Create iterator for a Deque."""

    def __init__(self, deque):
        self.deque = deque
        self.n = self.deque.n
        self.pos = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.pos >= self.deque.length:
            raise StopIteration
        
        out = self.deque.holder[(self.deque.start + self.pos) % self.n]
        self.pos += 1
        return out