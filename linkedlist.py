#First creating linked list
class LinkedList:
    def __init__(self):
        self.head=None
#Now creating nodes which will be linked
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
#Now creating 3 nodes
node1=Node('Kaniz')
node2=Node('Mitu')
node3=Node('Sifati')
node4=Node('Sadia')

lister=LinkedList()
lister.head=node1
lister.head.next=node2
lister.head=node2
lister.head.next=node3
lister.head=node3
lister.head.next=node4
lister.head=node4
lister.head.next=None

lister.head=node1
while(lister.head!=None):
    print(lister.head.data)
    lister.head=lister.head.next
