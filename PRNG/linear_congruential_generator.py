class LinearCongruentialGenerator:
    def __init__(self, is_bit=False, seed=1, a=1664525, c=1013904223, m=2**32):
    # def __init__(self, is_bit=False, seed=1, a=5, c=2, m=123):
        self.is_bit = is_bit
        self.state = int(seed) % m
        self.a = a
        self.c = c
        self.m = m

    def next(self):
        self.state = (self.a * self.state + self.c) % self.m
        if self.is_bit:
            return self.state & 1
        else:
            return self.state / (self.m - 1)

if __name__ == '__main__':
    lcg = LinearCongruentialGenerator()

    # Générez quelques nombres pseudo-aléatoires entre 0 et 1
    for _ in range(10):
        print(lcg.next())
