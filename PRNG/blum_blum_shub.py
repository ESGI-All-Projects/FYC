class BlumBlumShub:
    def __init__(self, is_bit=False, p=30000000091, q=40000000003, seed=5025504061):
        n = p * q
        self.is_bit = is_bit
        self.state = int(seed) % n
        self.p = p
        self.q = q
        self.max_value = n - 1

    def next(self):
        self.state = (self.state ** 2) % (self.p * self.q)
        if self.is_bit:
            return self.state & 1
        else:
            return self.state / (self.max_value - 1)
