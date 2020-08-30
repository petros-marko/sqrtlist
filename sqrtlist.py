from list_node import ListNode
from transparent_list import TransparentList
from math import sqrt, floor

#implementation of sqrtlist

class SqrtList:
    #initialize empty sqrtlist with dummy head and tail nodes
    def __init__(self):
        self.size = 0
        self.m = 0
        self.meta = []
        self.head = ListNode()
        self.tail = ListNode(None, None, self.head)

    #convert to string element by element
    def __str__(self):
        res = '['
        curr = self.head.nxt
        while curr != self.tail:
            res += str(curr.val) + ', '
            curr = curr.nxt
        if self.size > 0:
            res = res[:-2]
        res += ']'# + ' || ' + str(list(map(str,self.meta)))
        return res

    def __len__(self):
        return self.size

    #create the secondary list
    def buildMeta(self):

        #initialize it to an empty list
        self.meta = []
        #update the m value
        self.m = floor(sqrt(self.size))

        #if the new m value is 0 then the secondary list should be empty
        if self.m == 0:
            return
        curr = self.head.nxt
        i = 0
        #traverse the entire list
        while curr != self.tail:
            #once every m elements add the node to the secondary list
            if i % self.m == 0:
                self.meta.append(curr)
            curr = curr.nxt
            i += 1

    #get the node at position `idx`
    def getNode(self, idx):
        #if m is 0 then the list must be empty so return the tail
        if self.m == 0:
            return self.tail
        #the index of the search's starting point in the secondary list
        mIdx = idx // self.m
        #the number of remaining steps to the desired index when starting from that point
        remn = idx % self.m
        while mIdx >= len(self.meta):
            mIdx -= 1
            remn += self.m
        #start search from the intermediate node
        curr = self.meta[mIdx]
        #traverse the remaining nodes
        while remn > 0:
            curr = curr.nxt
            remn -= 1
        return curr

    #shift the stored nodes after the site of the removal by one forward to maintain the structure of the list
    def advance(self, rIdx):
        #if the list is empty or the removal was done after the last stored node nothing needs to be done
        if self.m == 0 or rIdx >= self.m * len(self.meta):
            return
        #the starting index for the shift
        mIdx = rIdx // self.m
        #if the removal was not done exactly on a stored node, the shift should start one node later
        if rIdx % self.m != 0:
            mIdx += 1 
        #traverse the ramaining list
        for i in range(mIdx, len(self.meta)):
            #shift by one
            self.meta[i] = self.meta[i].nxt
            #this can only be done in the last element, if it stores the tail node or even none, remove it to avoid working with NoneType
            if self.meta[i] == None or self.meta[i].val == None:
                self.meta.pop()
                break


    #shift the stored nodes after the site of the insertion by one backward to maintain the structure of the list
    def retreat(self, iIdx):
        #if the list is empty there is nothing to be done
        if self.m == 0:
            return
        #the starting index for the shift
        mIdx = iIdx // self.m
        #if the insertion was not done exactly on a stored node, the shift should start one node later
        if iIdx % self.m != 0:
            mIdx += 1
        #traverse the remaining list
        for i in range(mIdx, len(self.meta)):
            #shift by one
            self.meta[i] = self.meta[i].prv

    #get the value at index `idx`
    def get(self, idx):
        #get the node at index `idx` and access its val field
        return self.getNode(idx).val

    #set the value at index `idx`
    def set(self, val, idx):
        #get the node at index `idx` and update its val field with `val`
        self.getNode(idx).val = val

    #insert a new node with value `val` at index `idx`
    #(after self.insert(val, idx), self.get(idx) will return val)
    def insert(self, val, idx = 0):
        #get the node currently at idx
        atIdx = self.getNode(idx)
        #create a new node with the desired value and the above node as its next reference and the above nodes prv reference as its prv reference
        _ = ListNode(val, atIdx, atIdx.prv)
        self.size += 1
        #if the size of the list has become too large, restructure the secondary list
        if self.size >= self.m ** 2 + self.m - 1:
            self.buildMeta()
        #otherwise shift stored nodes to maintain the integrity of the secondary list
        else:
            self.retreat(idx)

    #remove the node at index `idx`
    def remove(self, idx):
        #get the node currently at `idx`
        atIdx = self.getNode(idx)
        #if its previous node exists, update its nxt reference
        if atIdx.prv != None:
            atIdx.prv.nxt = atIdx.nxt
        #if its next node exists, update its prv reference
        if atIdx.nxt != None:
            atIdx.nxt.prv = atIdx.prv
        self.size -= 1
        #if the size of the list has become too small, restructure the secondary list
        if self.size <= self.m ** 2 - self.m + 1:
            self.buildMeta()
        #otherwise shift stored nodes to maintain the integrity of the secondary list
        else:
            self.advance(idx)
