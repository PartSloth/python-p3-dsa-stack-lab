class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        if self.full() == False:
            self.items.append(item)

    def pop(self):
        if self.isEmpty() == False:
            return self.items.pop()

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        return self.size() == self.limit

    def search(self, target):
        if target in self.items:
            return (self.size() - self.items.index(target)) - 1
        else:
            return -1