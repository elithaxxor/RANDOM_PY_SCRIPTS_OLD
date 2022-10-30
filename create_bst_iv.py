class Node():
    def __init__(self, value=None):
        self.value=value
        self.left=None
        self.right=None

class BST():
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, current_node):
        if value<current_node.value:
            if current_node.left == None:  #fills empty left node
                current_node.left = Node(value)
            else: #commits recursion
                self._insert(value, current_node.left)
        elif value > current_node.value:
            if current_node.right == None:
                current_node.right = Node(value)
            else:
                self._insert(value, current_node.right)
        else:
            print('value in tree')


    def display_tree(self):
        current_node = self.root
        if self.root != None:
            self._display_tree(current_node)

    def _display_tree(self, current_node):
        if current_node != None:
            self._display_tree(current_node.left)
            print(current_node.value)
            self._display_tree(current_node.right)

