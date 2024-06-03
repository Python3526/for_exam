from typing import Optional


class FullAlphabet:
    def __init__(self, stop: int, step: Optional[int] = None):
        self.alphabet = [chr(i) for i in range(96, 123)]
        self.step = step or 1
        self.stop = stop
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.stop > self.count:
            self.count += self.step
            return self.alphabet[self.count]
        else:
            raise StopIteration
