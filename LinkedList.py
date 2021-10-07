class Node:
    def __init__(this):
        this.data = None
        this.next = None

class LinkedList:
    def __init__(this):
        this.head = None
        

node1 = Node()
node1.data = 1

node2 = Node()
node2.data = 2

node3 = Node()
node3.data = 3

linkedList = LinkedList()
linkedList.head = node1
node1.next = node2
node2.next = node3
node3.next = None

currNode = linkedList.head

while (currNode is not None):
    print (currNode.data)
    currNode = currNode.next
