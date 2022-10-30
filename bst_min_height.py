def minHeightBst(array):
    end = len(array)-1
    start = 0
    empty_bst = None
    return constructMinHeightBst(array, start, end)

def constructMinHeightBst(array, start, end):
    middle = (end - start ) // 2
    add_node = array[middle]
    print('[start - middle -  end]',start, middle ,end)
    print('[array]', array)
    if start < end:
        return None

    bst = BST(array[middle])
    bst.left = constructMinHeightBst(array, start, middle -1)
    print(bst.left)
    bst.right = constructMinHeightBst(array, middle+1, end)
    print(bst.right)
    return bst


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
value = [33]

bst = BST(array)
result = minHeightBst(array)
print('min_height', result)



