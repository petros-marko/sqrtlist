from list_node import ListNode
from transparent_list import TransparentList
from math import sqrt, floor

class SqrtList:
    def __init__(self):
        self.size = 0
        self.m = 0
        self.meta = []
        self.head = ListNode()
        self.tail = ListNode(None, None, self.head)

    def __str__(self):
        res = '['
        curr = self.head.nxt
        while curr != self.tail:
            res += str(curr.val) + ', '
            curr = curr.nxt
        if self.size > 0:
            res = res[:-2]
        res += ']' + ' || ' + str(list(map(str,self.meta)))
        return res

    def __len__(self):
        return self.size

    def buildMeta(self):

        self.meta = []
        self.m = floor(sqrt(self.size))

        if self.m == 0:
            return
        curr = self.head.nxt
        i = 0
        while curr != self.tail:
            if i % self.m == 0:
                self.meta.append(curr)
            curr = curr.nxt
            i += 1

    def getNode(self, idx):
        if self.m == 0:
            return self.tail
        mIdx = idx // self.m
        remn = idx % self.m
        while mIdx >= len(self.meta):
            mIdx -= 1
            remn += self.m
        curr = self.meta[mIdx]
        while remn > 0:
            curr = curr.nxt
            remn -= 1
        return curr

    def advance(self, rIdx):
        if self.m == 0 or rIdx >= self.m * len(self.meta):
            return
        mIdx = rIdx // self.m
        if rIdx % self.m != 0:
            mIdx += 1 
        for i in range(mIdx, len(self.meta)):
            self.meta[i] = self.meta[i].nxt
            if self.meta[i] == None or self.meta[i].val == None:
                self.meta.pop()
                break


    def retreat(self, iIdx):
        if self.m == 0:
            return
        mIdx = iIdx // self.m
        if iIdx % self.m != 0:
            mIdx += 1
        for i in range(mIdx, len(self.meta)):
            self.meta[i] = self.meta[i].prv

    def get(self, idx):
        return self.getNode(idx).val

    def set(self, val, idx):
        self.getNode(idx).val = val

    def insert(self, val, idx = 0):
        atIdx = self.getNode(idx)
        _ = ListNode(val, atIdx, atIdx.prv)
        self.size += 1
        if self.size >= self.m ** 2 + self.m - 1:
            self.buildMeta()
        else:
            self.retreat(idx)

    def remove(self, idx):
        atIdx = self.getNode(idx)
        if atIdx.prv != None:
            atIdx.prv.nxt = atIdx.nxt
        if atIdx.nxt != None:
            atIdx.nxt.prv = atIdx.prv
        self.size -= 1
        if self.size <= self.m ** 2 - self.m + 1:
            self.buildMeta()
        else:
            self.advance(idx)
