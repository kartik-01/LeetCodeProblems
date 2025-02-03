class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize an empty list with no head

    # Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head  # Point new_node's next to current head
        self.head = new_node  # Update head to new_node

    # Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:  # If list is empty
            self.head = new_node
            return
        temp = self.head
        while temp.next:  # Traverse to the last node
            temp = temp.next
        temp.next = new_node

    # Delete a node by value
    def delete_node(self, key):
        temp = self.head

        # If head needs to be deleted
        if temp and temp.data == key:
            self.head = temp.next  # Change head
            temp = None  # Free memory
            return

        # Search for the key to be deleted
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if not temp:  # Key not found
            return

        prev.next = temp.next  # Unlink the node from linked list
        temp = None

    # Display elements of the linked list
    def display(self):
        nodes = []
        temp = self.head
        while temp:
            nodes.append(temp.data)
            temp = temp.next
        print(" -> ".join(map(str, nodes)))


# Create a linked list instance
llist = LinkedList()

# Insert elements into the linked list
llist.insert_at_beginning(10)
llist.insert_at_beginning(20)
llist.insert_at_end(30)

# Display the linked list
print("Linked List:")
llist.display()

# Delete a node and display again
llist.delete_node(20)
print("After Deletion:")
llist.display()
