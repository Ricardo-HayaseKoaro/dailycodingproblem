class Orders:

    def __init__(self, n):
        self.log = []
        self.n = n  # max orders
        self.index = 0

    # works kinda in a circular way because of index, when log in full the index restart
    def record(self, order_id):
        if len(self.log) == self.n:
            self.log[self.index] = order_id
        else:
            self.log.append(order_id)  # append in the end of array
        self.index = (self.index + 1) % self.n

    def get_last(self, i):
        return self.log[self.index - i]  # return de Ith order but in reverse

