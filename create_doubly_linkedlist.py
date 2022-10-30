# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def context_manager(self, user_input,  *args, **kwargs):
        if user_input == 'remove':
            return self.remove(remove_var)
        if user_input == 'search':
            return self.containsNodeWithValue(search_val)

    def context_info(self, *args, **kwargs):
        print('initiating LL Removal:: [REMOVAL-VAL]', remove_var)
        print('initiating LL Removal:: [SEARCH-VAL]', search_val)
        print('[NODE-HEAD]:: [NODE-HEAD]', self.head, self.tail)

    def setHead(self, node):
        # Write your code here.
        pass

    def setTail(self, node):
        # Write your code here.
        pass

    def containsNodeWithValue(self, search_val):
        ''' returns true or false if linked list contains input val '''
        DoublyLinkedList.context_info(search_val)
        node = self.head()
        while node is not None and node.value != search_val:
            node = node.next
        return node is not None



    def insertBefore(self, node, nodeToInsert):
        ''' if dealing with linkeded list with one node, then there is nothing to insert '''
        if nodeToInsert == self.head and nodeToInsert == self.tail
            return
        pass

    def insertAfter(self, node, nodeToInsert):
        # Write your code here.
        pass

    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        pass

    def removeNodesWithValue(self, value):
        ''' combinatio of search and simple remove'''
        node = self.head

        while node is not None: # not at the end of LL
            node_to_remove = node # temporary variable--> linked lists need to be linked!!
            node = node.next
            if node_to_remove.value == value:
                self.remove(node)


    def remove(self, node):
        head_n = self.head
        tail = self.tail
        print('node',node)
        print('initiating LL Removal:: [REMOVAL-VAL]', remove_var)
        print('[NODE-HEAD]:: [NODE-HEAD]', head_n, tail)
        ''' test case, if head or tail are detected: if head or tail is moved, update to the next one '''
        if (remove_var == head_n ):
            self.head = self.head.next
            print('remove head traversal ', self.head)
        if (remove_var==tail):
            self.tail=self.tail.prev
            print('remove tail traversal ',self.tail)
        self.removeNodeBindings(remove_var)

    def removeNodeBindings(self, node):
        ''' defensive check to ensure not at tail/head. removes the bidnings and updates nodes next pointer to apropriate referecnce '''
        ''' remove the bindings of node, remove previous nodes pointer to point to next value [must make nodes accessable before overwritting] '''
        ''' defensive check, check the back of node '''
        ''' re assigns pointers, to avoid breaking linked list '''
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev

        ''' sets pointers to none '''
        node.prev = None
        node.next = None



search_val = 10
remove_var = 10
def main():
    array = [3,4,5,6,7]
#    node_1= Node(array)
    n = Node(array)
    ll=DoublyLinkedList()
    remove_results = ll.context_manager('remove', remove_var)
    search_results = ll.context_manager('search', search_val)

    print(remove_results)
    print(n.value)
    print()
if __name__ == "__main__":
    main()
