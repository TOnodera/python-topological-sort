class Node:
    def __init__(self, x, y=None):
        self.data = x
        self.next = y

    def first(self):
        return self.data

    def rest(self):
        return
