#implementation of a Doubly Linked Node
class ListNode:
    #constructor with optional arguments for value, next and previous
    #providing a next or previous reference also updates the corresponding references in the other node as well
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
