# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
## must adhere to bst property -- a nodes value must be greater than the nodes to the left and less <= values on the right

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        print('self.value', self.value)

    def insert(self, value):  ## o(log)n and o(1)
        current_node = self
        while True:
            if value < current_node.value:
                if current_node.left is None:
                    current_node = BST(value)  ## insert element to left of empty node
                    print('insert found [right]', current_node.value)
                    break
                else:
                    current_node = current_node.left  ## continue traversing
                    print('traversing[left]..', current_node)
            else:
                if current_node.right is None:
                    current_node.right = BST(value)
                    print('insert found [left]', current_node)
                    break
                else:
                    current_node = current_node.right
                    print('traversing[right]..', current_node.right)
        return self  ##  recursive call execution

    def contains(self, value):  ## searching algorothim
        current_node = self
        while current_node is not None:
            if value < current_node.value:
                current_node = current_node.left
                print('current_node [search]- [left]', current_node)
            elif value > current_node.value:
                current_node = current_node.right
                print('current_node [search]- [right]', current_node)
            else:
                print('does not contain', value)
                break
        return False

    def remove(self, value, parent_node=None):  # first serarch
        current_node = self
        while current_node is not None:
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
            elif current_node.right > value:
                current_node.right = value

            else: ## start removal processs
                if current_node.left is not None and current_node.right is not None:
                    current_node.value = current_node.right.getMinValue()
                    current_node.right.remove(current_node.value, current_node) ## (two child nodes present) # parent node keeps the deleted node from defualiting. parent node will be passed on as default node

                elif parent_node is None:
                    if current_node.left is not None:
                        current_node.value = current_node.left.value
                        current_node.right = current_node.left.right
                        current_node.left = current_node.left.left
                    elif current_node.right is not None:
                        current_node.value = current_node.right.value
                        current_node.right = current_node.right.left
                        current_node.right = current_node.right.right


                elif parent_node.left == current_node: # one child node or none --> check if current node is left or right child.
                    parent_node.left = current_node.left if current_node.left is not None else current_node.right
                elif parent_node.right == current_node:
                    parent_node.left = current_node.left if current_node.left is not None else current_node.right
                break
        return self


    def getMinValue(self): # left value is smaller than right in BT
        current_node = self
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value
nums = [12, 6, 18, 19, 21, 11, 3, 5, 4, 24, 18, 10]
val = 10
for num in nums:
    tree = BST(num)
    insert_result = tree.insert(val)
    search_result = tree.contains(10)
    delete_result = tree.remove(10)
    print('insert_result', insert_result)
    print('search_result', search_result)


