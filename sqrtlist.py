from list_node import ListNode
from transparent_list import TransparentList
from math import sqrt, floor

#implementation of sqrtlist

class SqrtList:
    #initialize empty sqrtlist with dummy head and tail nodes
    def __init__(self):
        self.__size = 0
        self.__m = 0
        self.__meta = []
        self.__head = ListNode()
        self.__tail = ListNode(None, None, self.__head)

    #convert to string element by element
    def __str__(self):
        res = '['
        curr = self.__head.nxt
        while curr != self.__tail:
            res += str(curr.val) + ', '
            curr = curr.nxt
        if self.__size > 0:
            res = res[:-2]
        res += ']'# + ' || ' + str(list(map(str,self.__meta)))
        return res

    def __len__(self):
        return self.__size

    #create the secondary list
    def __buildMeta(self):

        #initialize it to an empty list
        self.__meta = []
        #update the m value
        self.__m = floor(sqrt(self.__size))

        #if the new m value is 0 then the secondary list should be empty
        if self.__m == 0:
            return
        curr = self.__head.nxt
        i = 0
        #traverse the entire list
        while curr != self.__tail:
            #once every m elements add the node to the secondary list
            if i % self.__m == 0:
                self.__meta.append(curr)
            curr = curr.nxt
            i += 1

    #get the node at position `idx`
    def __getNode(self, idx):
        #if m is 0 then the list must be empty so return the tail
        if self.__m == 0:
            return self.__tail
        #the index of the search's starting point in the secondary list
        mIdx = idx // self.__m
        #the number of remaining steps to the desired index when starting from that point
        remn = idx % self.__m
        while mIdx >= len(self.__meta):
            mIdx -= 1
            remn += self.__m
        #start search from the intermediate node
        curr = self.__meta[mIdx]
        #traverse the remaining nodes
        while remn > 0:
            curr = curr.nxt
            remn -= 1
        return curr

    #shift the stored nodes after the site of the removal by one forward to maintain the structure of the list
    def __advance(self, rIdx):
        #if the list is empty or the removal was done after the last stored node nothing needs to be done
        if self.__m == 0 or rIdx >= self.__m * len(self.__meta):
            return
        #the starting index for the shift
        mIdx = rIdx // self.__m
        #if the removal was not done exactly on a stored node, the shift should start one node later
        if rIdx % self.__m != 0:
            mIdx += 1 
        #traverse the ramaining list
        for i in range(mIdx, len(self.__meta)):
            #shift by one
            self.__meta[i] = self.__meta[i].nxt
            #this can only be done in the last element, if it stores the tail node or even none, remove it to avoid working with NoneType
            if self.__meta[i] == None or self.__meta[i].val == None:
                self.__meta.pop()
                break


    #shift the stored nodes after the site of the insertion by one backward to maintain the structure of the list
    def __retreat(self, iIdx):
        #if the list is empty there is nothing to be done
        if self.__m == 0:
            return
        #the starting index for the shift
        mIdx = iIdx // self.__m
        #if the insertion was not done exactly on a stored node, the shift should start one node later
        if iIdx % self.__m != 0:
            mIdx += 1
        #traverse the remaining list
        for i in range(mIdx, len(self.__meta)):
            #shift by one
            self.__meta[i] = self.__meta[i].prv

    #get the value at index `idx`
    def get(self, idx):
        #get the node at index `idx` and access its val field
        return self.__getNode(idx).val

    #set the value at index `idx`
    def set(self, val, idx):
        #get the node at index `idx` and update its val field with `val`
        self.__getNode(idx).val = val

    #insert a new node with value `val` at index `idx`
    #(after self.insert(val, idx), self.get(idx) will return val)
    def insert(self, val, idx = 0):
        #get the node currently at idx
        atIdx = self.__getNode(idx)
        #create a new node with the desired value and the above node as its next reference and the above nodes prv reference as its prv reference
        _ = ListNode(val, atIdx, atIdx.prv)
        self.__size += 1
        #if the size of the list has become too large, restructure the secondary list
        if self.__size >= self.__m ** 2 + self.__m - 1:
            self.__buildMeta()
        #otherwise shift stored nodes to maintain the integrity of the secondary list
        else:
            self.__retreat(idx)

    #remove the node at index `idx`
    def remove(self, idx):
        #get the node currently at `idx`
        atIdx = self.__getNode(idx)
        #if its previous node exists, update its nxt reference
        if atIdx.prv != None:
            atIdx.prv.nxt = atIdx.nxt
        #if its next node exists, update its prv reference
        if atIdx.nxt != None:
            atIdx.nxt.prv = atIdx.prv
        self.__size -= 1
        #if the size of the list has become too small, restructure the secondary list
        if self.__size <= self.__m ** 2 - self.__m + 1:
            self.__buildMeta()
        #otherwise shift stored nodes to maintain the integrity of the secondary list
        else:
            self.__advance(idx)
