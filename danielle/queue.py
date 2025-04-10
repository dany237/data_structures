class Queue:
    def __init__(self):
        self.items = []

    # 1. Enqueue
    def enqueue(self, item):
        self.items.append(item)

    # 2. Dequeue
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("Queue is empty")

    # 3. Peek (front)
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return None

    # 4. Check if empty
    def is_empty(self):
        return len(self.items) == 0

    # 5. Size
    def size(self):
        return len(self.items)

    # 6. Display
    def display(self):
        print("Queue:", self.items)
