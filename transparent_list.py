from list_node import ListNode

class TransparentList:
    def __init__(self):
        self.size = 0
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
        res += ']'
        return res

    def __len__(self):
        return self.size

    def get(self, idx):
        return self.getNode(idx).val

    def insert(self, val, idx = 0):
        atIdx = self.getNode(idx)
        _ = ListNode(val, atIdx, atIdx.prv)
        self.size += 1

    def set(self, val, idx):
        atIdx = self.getNode(idx)
        atIdx.val = val

    def remove(self, idx):
        atIdx = self.getNode(idx)
        atIdx.prv.nxt = atIdx.nxt
        atIdx.nxt.prv = atIdx.prv
        self.size -= 1

    def getNode(self, idx):
        if idx <= self.size / 2:
            curr = self.head.nxt
            for i in range(idx):
                curr = curr.nxt
            return curr
        curr = self.tail
        idx = self.size - idx
        for i in range(idx):
            curr = curr.prv
        return curr
