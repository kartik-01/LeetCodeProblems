class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)

node1.next=node2
node2.next=node3
node3.next=node4

head = node1

# Traverse
curr = head

while curr:
    print(curr.data, end=" -> ")
    curr = curr.next
print(None)

# Insert at the start
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

# Insert at the end
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

# Delete at the start

curr = head

if head is not None:
    head = head.next

# Traverse
curr = head

while curr:
    print(curr.data, end=" -> ")
    curr = curr.next
print(None)


# Delete at the end

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

# Delete a particular node

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
