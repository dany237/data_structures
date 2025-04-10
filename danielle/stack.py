class Stack:
    def __init__(self, para=None):
        if para is None:
            self.stack = []
        else:
            self.stack = para

    def push(self, newElement):
        self.stack.append(newElement)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return "Stack is empty"

    def top(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            return "Stack is empty"

    def isEmpty(self):
        return len(self.stack) == 0

    def display_stack(self):
        print(self.stack)
