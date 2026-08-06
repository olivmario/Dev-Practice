class OrderLog:
    def __init__(self, N):
        self.N = N
        self.log = [None] * N
        self.index = 0
        self.size = 0

    def record(self, order_id):
        self.log[self.index] = order_id
        self.index = (self.index + 1) % self.N
        
        if self.size < self.N:
            self.size += 1

    def get_last(self, i):
        if i > self.size:
            raise IndexError("elementos insuficientes")
        
        position = (self.index - i) % self.N
        return self.log[position]