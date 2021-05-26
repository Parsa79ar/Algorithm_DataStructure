class Node:
    def __init__(self, data) :
        self.data = data
        self.next = None
    
class SLL:
    def __init__(self, data) :
        self.head = Node(data)
        self.len = 0

    def addLast(self, data):
        newNode  = Node(data)
        if  self.len == 0 :
            self.head = newNode
        elif self.len == 1 :
            self.head.next = newNode
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = newNode
        self.len += 1

    def traverse(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next

    def addFirst(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        self.len += 1