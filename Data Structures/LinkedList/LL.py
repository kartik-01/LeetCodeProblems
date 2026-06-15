class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
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


# Traverse the LinkedList - O(n)
curr = head

while curr:
    print(curr.data, end=" -> ")
    curr = curr.next
print(None)

# Insert at the start - O(1)
curr = head

node0=Node(5)
node0.next = head
head = node0
# Traverse
curr = head

while curr:
    print(curr.data, end=" -> ")
    curr = curr.next
print(None)

# Insert at the end - O(n)
curr = head
node5 = Node(50)

if head is None:
    head = node5
else:
    while curr.next:
        curr = curr.next
    curr.next = node5

# Traverse
curr = head

while curr:
    print(curr.data, end=" -> ")
    curr = curr.next
print(None)

# Delete at the start - O(1)

curr = head

if head is not None:
    head = head.next

# Traverse
curr = head

while curr:
    print(curr.data, end=" -> ")
    curr = curr.next
print(None)


# Delete at the end - O(n)

curr = head

if head is None:
    pass
elif curr.next is None:
    head = None
else:
    while curr.next.next:
        curr = curr.next
    curr.next = None

# Traverse
curr = head

while curr:
    print(curr.data, end=" -> ")
    curr = curr.next
print(None)

# Delete a particular node - O(n)

curr = head
target = 30

if head is None:
    pass
elif head.data == target:
    head = head.next
else:
    while curr.next and curr.next.data != target:
        curr = curr.next
    if curr.next:
        curr.next = curr.next.next

# Traverse
curr = head

while curr:
    print(curr.data, end=" -> ")
    curr = curr.next
print(None)
