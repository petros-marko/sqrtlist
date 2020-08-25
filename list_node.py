class ListNode:
    def __init__(self, val = None, nxt = None, prv = None):
        self.val = val
        self.nxt = nxt
        self.prv = prv
        if nxt != None:
            nxt.prv = self
        if prv != None:
            prv.nxt = self

    def __str__(self):
        return 'N(' + str(self.val) + ')'
