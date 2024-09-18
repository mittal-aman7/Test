class MinStack:
    def __init__(self, val= float('inf')):
        self.val = val
        self.minimum = float('inf')
        self.stack = [tuple((self.val, self.minimum))]    # [(self.val, self.minimum)] is stored in the list

    def push(self, val : int):
        if val > self.stack[-1][1]:
            self.stack.append((val, self.stack[-1][1]))
        else:
            self.stack.append((val, val))
            self.minimum = val

    def pop(self):
        removed = self.stack.pop()
        return removed[0]

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]