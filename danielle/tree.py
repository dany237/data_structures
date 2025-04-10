class TreeNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # 1. Insert
    def insert(self, value):
        def _insert(node, value):
            if not node:
                return TreeNode(value)
            if value < node.data:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)
            return node

        self.root = _insert(self.root, value)

    # 2. Search
    def search(self, value):
        def _search(node, value):
            if not node or node.data == value:
                return node
            if value < node.data:
                return _search(node.left, value)
            return _search(node.right, value)

        return _search(self.root, value)

    # 3. In-order traversal
    def inorder(self):
        result = []

        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.data)
                _inorder(node.right)

        _inorder(self.root)
        return result

    # 4. Pre-order traversal
    def preorder(self):
        result = []

        def _preorder(node):
            if node:
                result.append(node.data)
                _preorder(node.left)
                _preorder(node.right)

        _preorder(self.root)
        return result

    # 5. Post-order traversal
    def postorder(self):
        result = []

        def _postorder(node):
            if node:
                _postorder(node.left)
                _postorder(node.right)
                result.append(node.data)

        _postorder(self.root)
        return result

    # 6. Find min
    def find_min(self):
        curr = self.root
        while curr and curr.left:
            curr = curr.left
        return curr.data if curr else None

    # 7. Find max
    def find_max(self):
        curr = self.root
        while curr and curr.right:
            curr = curr.right
        return curr.data if curr else None

    # 8. Delete node
    def delete(self, value):
        def _delete(node, value):
            if not node:
                return node
            if value < node.data:
                node.left = _delete(node.left, value)
            elif value > node.data:
                node.right = _delete(node.right, value)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                # Replace with inorder successor
                temp = node.right
                while temp.left:
                    temp = temp.left
                node.data = temp.data
                node.right = _delete(node.right, temp.data)
            return node

        self.root = _delete(self.root, value)
