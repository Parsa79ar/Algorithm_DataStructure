class Node : 
    def __init__(self, data, next = None, prev = None) :
        self.data = data
        self.next = next
        self.prev = prev

class DLL :
    def __init__(self) :
        self.head = None
        self.last = None
        self.len = 0

    def addFirst(self, data) :
        newNode = Node(data)
        if self.len == 0 :
            self.head = newNode
            self.last = newNode
        else :
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        self.len += 1 

    def addLast(self, data) :
        newNode = Node(data)
        if self.len == 0 :
            self.head = newNode
            self.last = newNode
        else :
            self.last.next = newNode
            newNode.prev = self.last
            self.last = newNode
        self.len += 1 

    def deleteFirst(self) :
        pass
