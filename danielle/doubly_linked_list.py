class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # 1. Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    # 2. Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    # 3. Insert at position
    def insert_at_position(self, data, position):
        if position == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        curr = self.head
        for i in range(position - 1):
            if not curr:
                raise Exception("Position out of bounds")
            curr = curr.next
        new_node.next = curr.next
        new_node.prev = curr
        if curr.next:
            curr.next.prev = new_node
        curr.next = new_node

    # 4. Delete a node by value
    def delete_value(self, value):
        curr = self.head
        while curr:
            if curr.data == value:
                if curr.prev:
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next  # deleting head

                if curr.next:
                    curr.next.prev = curr.prev
                return
            curr = curr.next
        print("Value not found")

    # 5. Display forward
    def display_forward(self):
        curr = self.head
        values = []
        while curr:
            values.append(str(curr.data))
            curr = curr.next
        print(" ⇄ ".join(values))

    # 6. Display backward
    def display_backward(self):
        curr = self.head
        if not curr:
            print("Empty list")
            return
        while curr.next:
            curr = curr.next
        values = []
        while curr:
            values.append(str(curr.data))
            curr = curr.prev
        print(" ⇄ ".join(values))

    # 7. Length of the list
    def length(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    # 8. Reverse the list
    def reverse(self):
        curr = self.head
        prev_node = None
        while curr:
            prev_node = curr.prev
            curr.prev = curr.next
            curr.next = prev_node
            curr = curr.prev
        if prev_node:
            self.head = prev_node.prev
