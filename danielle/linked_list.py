class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to next node


class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # 2. Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # 3. Insert at specific position
    def insert_at_position(self, data, position):
        if position == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        current = self.head
        for i in range(position - 1):
            if not current:
                raise Exception("Position out of bounds")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    # 4. Delete by value
    def delete_value(self, value):
        current = self.head
        if current and current.data == value:
            self.head = current.next
            return
        prev = None
        while current and current.data != value:
            prev = current
            current = current.next
        if current:
            prev.next = current.next
        else:
            print("Value not found")

    # 5. Delete by position
    def delete_at_position(self, position):
        if not self.head:
            return
        if position == 0:
            self.head = self.head.next
            return
        current = self.head
        for i in range(position - 1):
            if not current.next:
                raise Exception("Position out of bounds")
            current = current.next
        if current.next:
            current.next = current.next.next

    # 6. Search for a value
    def search(self, value):
        current = self.head
        index = 0
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1

    # 7. Reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # 8. Display list
    def display(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        print(" → ".join(nodes))

    # 9. Get length
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    # 10. Convert to Python list
    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result