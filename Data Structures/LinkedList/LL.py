class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
# Creating node elements
node1=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)
node5=Node(50)

# Linking nodes to each other
node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5

# Setting head of the nodes
head = node1
curr = head

# Traversing the LinkedList: O(n)
while curr is not None:
    print(curr.data, end=" -> ")
    curr = curr.next
print(None)

# Adding element at the start: O(1) operation

newNode = Node(5)
newNode.next = head
head = newNode

curr = head

while curr is not None:
    print(curr.data, end=' -> ')
    curr=curr.next
print(None)

# Deleting the node from the beginning: O(1)

if head is not None:
    head=head.next

curr = head

while curr is not None:
    print(curr.data, end=' -> ')
    curr=curr.next
print(None)

# Delete the node at the end: O(n)
curr=head

if curr is None:
    print("List is empty")

elif curr.next is None:
    curr=None

else:
    while curr.next.next is not None:
        curr = curr.next
    curr.next = None

curr = head

while curr is not None:
    print(curr.data, end=' -> ')
    curr=curr.next
print(None)

# Deleting a particular node: O(n)
curr = head

while curr.next.data!=30:
    curr = curr.next
curr.next = curr.next.next

curr = head

while curr is not None:
    print(curr.data, end=' -> ')
    curr=curr.next
print(None)

# Adding an element at the end of the linkedlist

curr = head
newNode2 = Node(60)
while curr.next is not None:
    curr = curr.next
curr.next = newNode2

curr = head

while curr is not None:
    print(curr.data, end=' -> ')
    curr=curr.next
print(None)