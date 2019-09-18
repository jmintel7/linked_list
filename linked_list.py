

class node:

    def __init__(self, data = None):
        self.data = data
        self.next = None


class linked_list:

    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
        cur_node.next = new_node

    def length(self):
        cur_node = self.head
        total = 0
        while cur_node.next!= None:
            cur_node = cur_node.next
            total = total +1
        return total

    def display(self):
        pass

    def get_rollno(self, rollno):
        cur_node = self.head
        while cur_node.next!= None:
            cur_node = cur_node.next
            data = cur_node.data
            if data.rollno == rollno:
                return data
        print ('Student with the roll no does not exist')
        return None


    def erase(self, rollno):
        cur_node = self.head
        while cur_node.next != None:
            last_node = cur_node
            cur_node = cur_node.next
            data = cur_node.data
            if data.rollno == rollno:
                last_node.next = cur_node.next
                print('Record erased')
                return
        print('Student with the roll no does not exist')
        return None
