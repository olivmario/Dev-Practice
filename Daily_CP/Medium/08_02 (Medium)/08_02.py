class Cons:
    def __init__(self, one, two):
        self.one = one
        self.two = two
    
    def get_one(self):##car
        return self.one
    
    def get_two(self):##cdr
        return self.two

cons = Cons(3, 4)
print(cons.get_one())
print(cons.get_two())