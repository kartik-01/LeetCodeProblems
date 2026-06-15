class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Traversing the LL 
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print(None)

    # Inserting element at the start
    def insert_at_start(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    # Inserting element at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:          # guard: empty list
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    # Deleting element at the start
    def delete_at_start(self):
        if self.head:
            self.head = self.head.next

    # Deleting element at the end 
    def delete_at_end(self):
        if self.head is None:          # guard: empty list
            return
        if self.head.next is None:     # guard: single element
            self.head = None
            return
        curr = self.head
        while curr.next.next:
            curr = curr.next
        curr.next = None

    # Deleting a particular element 
    def delete_value(self, value):
        if self.head is None:          # guard: empty list
            return
        if self.head.data == value:    # guard: target is the head
            self.head = self.head.next
            return
        curr = self.head
        # added "curr.next and" so a missing value stops instead of crashing
        while curr.next and curr.next.data != value:
            curr = curr.next
        if curr.next:                  # only delete if found
            curr.next = curr.next.next


# ----- demo: same sequence as your original script -----
if __name__ == "__main__":
    ll = LinkedList()
    for v in [10, 20, 30, 40]:
        ll.insert_at_end(v)
    ll.print_list()

    ll.insert_at_start(5)
    ll.print_list()

    ll.insert_at_end(50)
    ll.print_list()

    ll.delete_at_start()
    ll.print_list()

    ll.delete_at_end()
    ll.print_list()

    ll.delete_value(20)
    ll.print_list()