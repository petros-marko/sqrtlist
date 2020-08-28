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
        res += ']' + ' || ' + str(meta)
        return res

    def __len__(self):
        return self.size

    def buildMeta(self):
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
        pass

    def advance(self, rIdx):
        pass

    def retreat(self, iIdx):
        pass

    def get(self, idx):
        return self.getNode(idx)[0].val

    def set(self, val, idx):
        self.getNode(idx)[0].val = val

    def insert(self, val, idx = 0):
        pass

    def remove(self, idx):
        pass
