class Array:
    def __init__(self):
        self.data = []

    def append(self, value):
        self.data += [value]

    def insert(self, index, value):
        if index < 0 or index > len(self.data):
            raise IndexError("Index out of range")
        self.data = self.data[:index] + [value] + self.data[index:]

    def remove(self, value):
        if value not in self.data:
            raise ValueError("Value not found in array")
        index = self.data.index(value)
        self.data = self.data[:index] + self.data[index+1:]

    def pop(self, index=None):
        if index is None:
            index = len(self.data) - 1
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of range")
        value = self.data[index]
        self.data = self.data[:index] + self.data[index+1:]
        return value

    def get(self, index):
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of range")
        return self.data[index]

    def set(self, index, value):
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of range")
        self.data[index] = value

    def length(self):
        return len(self.data)

    def display(self):
        print(self.data)

    def find(self, value):
        for i in range(len(self.data)):
            if self.data[i] == value:
                return i
        return -1

    def clear(self):
        self.data = []
