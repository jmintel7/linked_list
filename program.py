
class node:
    """A node in linked list"""

    def __init__(self, data = None):
        self.data = data
        self.next = None


class linked_list:
    """class of linked list"""

    def __init__(self):
        self.head = node() #no data and not indexable, used as a placeholder to point towards first element of the list

    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        elements = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elements.append(cur_node.data)
        print(elements)

    def get_index(self, index):
        if index >= self.length():
            print('ERROR: Index out of range')
            return None
        cur_node = self.head
        for i in range(index+1):
            cur_node = cur_node.next
        return cur_node.data

    def erase(self, index):
        if index >= self.length():
            print('ERROR: Index out of range')
            return None
        cur_node = self.head
        for i in range(index+1):
            last_node = cur_node
            cur_node = cur_node.next
        last_node.next = cur_node.next


