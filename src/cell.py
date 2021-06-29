class Cell:
    def __init__(self, x, y=None):
        self.data = x
        self.next = y

    def first(self):
        return self.data

    def rest(self):
        return self.next

    def set_first(self, x):
        self.data = x

    def set_rest(self, x):
        self.next = x
