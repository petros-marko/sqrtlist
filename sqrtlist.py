from list_node import ListNode
from transparent_list import TransparentList
from math import sqrt, floor

class SqrtList:
    def __init__(self):
        self.size = 0
        self.m = 0
        self.meta = TransparentList()
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
        res += ']'#+ ' || ' + str(self.meta)
        return res

    def __len__(self):
        return self.size

    def buildMeta(self):
        self.m = self.size
        self.meta = TransparentList()
        step = floor(sqrt(self.m))
        if step == 0:
            return
        curr = self.head.nxt
        for i in range(self.size):
            if i % step == 0:
                self.meta.insert(curr, len(self.meta))
            curr = curr.nxt

    def getNode(self, idx):
        if idx > self.size:
            return None
        if self.m == 0:
            return self.tail
        mIdx = idx // floor(sqrt(self.m))
        remaining = idx % floor(sqrt(self.m))
        if mIdx >= len(self.meta):
            mIdx -= 1
            remaining += floor(sqrt(self.m))
        curr = self.meta.get(mIdx)
        for i in range(remaining):
            curr = curr.nxt
        return curr

    def advance(self, removalIdx):
        if self.m == 0:
            return
        startIdx = removalIdx // floor(sqrt(self.m))
        if removalIdx % floor(sqrt(self.m)) != 0:
            startIdx += 1
        curr = self.meta.getNode(startIdx)
        while curr.val != None:
            curr.val = curr.val.nxt
            curr = curr.nxt

    def retreat(self, insertionIdx):
        if self.m == 0:
            return
        startIdx = insertionIdx // floor(sqrt(self.m))
        if insertionIdx % floor(sqrt(self.m)) != 0:
            startIdx += 1
        curr = self.meta.getNode(startIdx)
        while curr.val != None:
            curr.val = curr.val.prv
            curr = curr.nxt

    def get(self, idx):
        return self.getNode(idx).val

    def set(self, val, idx):
        self.getNode(idx).val = val

    def insert(self, val, idx = 0):
        atIdx = self.getNode(idx)
        _ = ListNode(val, atIdx, atIdx.prv)
        self.size += 1
        if self.size >= self.m + floor(sqrt(self.m)):
            self.buildMeta()
        else:
            self.retreat(idx)

    def remove(self, idx):
        atIdx = self.getNode(idx)
        atIdx.prv.nxt = atIdx.nxt
        atIdx.nxt.prv = atIdx.prv
        self.size -= 1
        if self.size <= self.m - floor(sqrt(self.m)):
            self.buildMeta()
        else:
            self.advance(idx)
