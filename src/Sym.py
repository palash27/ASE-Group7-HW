import math

class Sym:
    """
    Summarize a stream of symbols.
    """
    def __init__(self) -> None:
        self.n = 0
        self.has = {}
        self. most = 0
        self.mode = None
        
    def add(self, x):
        """
        update counts of things seen so far
        """
        if x != '?':
            self.n = self.n + 1
            self.has[x] = 1 + self.has.get(x, 0)
            if self.has[x] > self.most:
                self.most, self.mode = self.has[x], x

    def mid(self):
        """
        return the mode
        """
        return self.mode

    def div(self):
        """
        return the entropy
        """
        def fun(p):
            """
            pass `p` and return p time log of p to the base 2
            """
            return p*math.log(p,2)
        e = 0
        for _,n in self.has.items():
            e = e + fun(n/self.n)
        return -e

