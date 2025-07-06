class Node:
    """
    A Node in a singly linked list.
    
    Attributes:
        data: The value stored in the node.
        next: A pointer to the next node in the list.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class LinkedList:
    """
    A singly linked list implementation.
    
    Attributes:
        head: The first node of the linked list.
    
    Methods:
        append(data): Add a node with the given data at the end of the list.
        prepend(data): Add a node with the given data at the beginning of the list.
        insert_after_node(prev_node, data): Insert a new node with the given data after the specified node.
        delete_node(key): Remove the first node that contains the given key (data).
        search(key): Search for a node containing the key.
        reverse(): Reverse the linked list in place.
        length(): Return the number of nodes in the list.
        display(): Print out the linked list in a readable format.
    """
    def __init__(self):
        self.head = None

    def append(self, data):
        """
        Append a new node with the specified data to the end of the list.
        """
        new_node = Node(data)
        # If the list is empty, assign new_node to head.
        if not self.head:
            self.head = new_node
            return

        # Otherwise, traverse to the end and add the new node.
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        """
        Prepend a new node with the specified data to the beginning of the list.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        """
        Insert a new node with the specified data after the given node.
        """
        # Check if the previous node exists.
        if not prev_node:
            raise ValueError("The given previous node must not be None.")

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        """
        Delete the first node in the list with the specified key (data).
        """
        current = self.head

        # If the head node itself holds the key, update head.
        if current and current.data == key:
            self.head = current.next
            return

        # Search for the key, keeping track of the previous node.
        previous = None
        while current and current.data != key:
            previous = current
            current = current.next

        # If the key was not present in the list, do nothing.
        if current is None:
            return

        # Unlink the node from the linked list.
        previous.next = current.next

    def search(self, key):
        """
        Search for a node that contains the specified data (key).
        
        Returns:
            The node if found, otherwise None.
        """
        current = self.head
        while current:
            if current.data == key:
                return current
            current = current.next
        return None

    def reverse(self):
        """
        Reverse the linked list in place.
        """
        previous = None
        current = self.head
        while current:
            next_node = current.next  # Store next node
            current.next = previous   # Reverse the link
            previous = current        # Move previous one step forward
            current = next_node       # Move current one step forward
        self.head = previous

    def length(self):
        """
        Return the number of nodes in the linked list.
        """
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def display(self):
        """
        Print the linked list in a readable format.
        """
        current = self.head
        list_str = ""
        while current:
            list_str += f"{current.data} -> "
            current = current.next
        list_str += "None"
        print(list_str)

    def __iter__(self):
        """
        Make the linked list iterable.
        """
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __repr__(self):
        """
        Return a string representation of the linked list.
        """
        nodes = [str(node) for node in self]
        return "LinkedList([" + ", ".join(nodes) + "])"


# Example usage
if __name__ == "__main__":
    # Create an empty linked list
    ll = LinkedList()

    # Append elements to the list
    ll.append(3)
    ll.append(5)
    ll.append(7)

    # Prepend an element
    ll.prepend(1)

    # Display the list
    print("Linked List:")
    ll.display()  # Expected output: 1 -> 3 -> 5 -> 7 -> None

    # Insert after the first node (after node with data=1)
    first_node = ll.head
    ll.insert_after_node(first_node, 2)
    print("\nAfter inserting 2 after the head:")
    ll.display()  # Expected: 1 -> 2 -> 3 -> 5 -> 7 -> None

    # Search for a node
    result = ll.search(5)
    print("\nSearch for 5 in the list:")
    print(result)  # Expected: Node(5)

    # Delete a node (delete node with data 3)
    ll.delete_node(3)
    print("\nAfter deleting node with data 3:")
    ll.display()  # Expected: 1 -> 2 -> 5 -> 7 -> None

    # Reverse the linked list
    ll.reverse()
    print("\nAfter reversing the list:")
    ll.display()  # Expected reversed order

    # Length of the list
    print("\nLength of the list:", ll.length())
