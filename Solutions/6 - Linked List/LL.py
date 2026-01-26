class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = None

# Creating node elements
node1=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)

# Linking nodes to each other
node1.next=node2
node2.next=node3
node3.next=node4

# Setting head of the nodes
head = node1
curr = head

# Traversing the LinkedList: O(n)
while curr is not None:
    print(curr.data, end=" -> ")
    curr = curr.next
print("None")

# Adding element at the start: O(1) operation

new_node = Node(50)
new_node.next = head
head = new_node

curr = head
while curr is not None:
    print(curr.data, end=" -> ")
    curr = curr.next
print("None")

# Deleting the node from the beginning

if head is not None:
    head = head.next

curr = head
while curr is not None:
    print(curr.data, end=" -> ")
    curr = curr.next
print("None")