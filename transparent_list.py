from list_node import ListNode

#TransparentList is an implementation of a Doubly Linked List that exposes the underlying nodes to the programmer
#Initially it was meant to be used as the secondary list in the SqrtList class but now SqrtList uses a builtin python list for that purpose
#This class is useful for conducting the timer tests, since SqrtList is meant to be an improvement over a normal Linked List

class TransparentList:
    #initialize size as well as head and tail dummy nodes
    def __init__(self):
        self.size = 0
        self.head = ListNode()
        self.tail = ListNode(None, None, self.head)

    #turn the list into a string element by element
    def __str__(self):
        res = '['
        curr = self.head.nxt
        while curr != self.tail:
            res += str(curr.val) + ', '
            curr = curr.nxt
        if self.size > 0:
            res = res[:-2]
        res += ']'
        return res

    def __len__(self):
        return self.size

    #get the value at index `idx`
    def get(self, idx):
        #get the corresponding node and access its value
        return self.getNode(idx).val

    #insert the value `val` at the index `idx` 
    #(after the insertion self.get(`idx`) will return `val`)
    def insert(self, val, idx = 0):
        #get the current node at idx
        atIdx = self.getNode(idx)
        #create a new node with atIdx as its next reference and atIdx.prv as its previous reference
        #note that the three value constructor updates the references of the other nodes as well
        _ = ListNode(val, atIdx, atIdx.prv)
        #increment the size variable
        self.size += 1

    #update the value at index `idx` to `val`
    def set(self, val, idx):
        #get the node at idx
        atIdx = self.getNode(idx)
        #set its value field
        atIdx.val = val

    #remove the node at index `idx`
    def remove(self, idx):
        #get the current node at idx
        atIdx = self.getNode(idx)
        #update its previous node's next reference to point to its next reference
        atIdx.prv.nxt = atIdx.nxt
        #update its next node's previous reference to point to its previous reference
        atIdx.nxt.prv = atIdx.prv
        #decrease the size
        self.size -= 1

    #get the node at index `idx`
    def getNode(self, idx):
        #if the index is in the first half of the list
        if idx <= self.size / 2:
            curr = self.head.nxt
            #traverse the list going forward until the desired index
            for i in range(idx):
                curr = curr.nxt
            return curr
        #if the index is in the second half of the list
        curr = self.tail
        idx = self.size - idx
        #traverse the list going backward until the desired index
        for i in range(idx):
            curr = curr.prv
        return curr
