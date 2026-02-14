# Creating linked list node
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# Populating Nodes
node1=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)
node5=Node(50)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5

# Traversing the Linkedlist
head = node1
curr = head

while curr:
    print(curr.data, end=' -> ')
    curr=curr.next
print(None)


# Adding element at the start
curr = head

node0=Node(5)
node0.next=node1
head=node0

curr=head
while curr:
    print(curr.data, end=' -> ')
    curr=curr.next
print(None)


# Deleting the node from the beginning
curr = head

if head:
    head=head.next

curr=head
while curr:
    print(curr.data, end=' -> ')
    curr=curr.next
print(None)
# Deleting the node at the end

curr = head

while curr.next.next:
    curr=curr.next
curr.next = None


while curr:
    print(curr.data, end = ' -> ')
print(None)
# Delete a particular node
