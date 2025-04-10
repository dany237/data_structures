class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # 1. Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head

    # 2. Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            return
        new_node.next = self.head
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        self.head = new_node

    # 3. Delete a node
    def delete(self, key):
        if not self.head:
            print("List is empty")
            return

        curr = self.head
        prev = None

        # Case 1: Deleting head
        if curr.data == key:
            while curr.next != self.head:
                curr = curr.next
            if self.head == self.head.next:  # Only one node
                self.head = None
            else:
                curr.next = self.head.next
                self.head = self.head.next
            return

        # Case 2: Deleting other nodes
        curr = self.head
        while curr.next != self.head:
            prev = curr
            curr = curr.next
            if curr.data == key:
                prev.next = curr.next
                return

        print("Key not found")

    # 4. Display list
    def display(self):
        if not self.head:
            print("List is empty")
            return
        result = []
        curr = self.head
        while True:
            result.append(str(curr.data))
            curr = curr.next
            if curr == self.head:
                break
        print(" → ".join(result) + " → (back to head)")

    # 5. Get length
    def length(self):
        if not self.head:
            return 0
        count = 1
        curr = self.head.next
        while curr != self.head:
            count += 1
            curr = curr.next
        return count
