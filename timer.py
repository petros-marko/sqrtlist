from sqrtlist import SqrtList
from transparent_list import TransparentList
from random import randint

#simple utility for doing time comparisons between a simple linked list and an sqrtlist
#leave the desired initialization uncommented and comment the other one out
#run the program with the unix time utility to see the performance improvement of sqrtlist

#tester = TransparentList()
tester = SqrtList()

#perform 1e7 operations on the list
#each time an operation is decided randomly with equal probability
#if the operation chosen is not possible on the current list, it is just skipped

for i in range(10000000):
    cmd = randint(0, 3)
    #insert operation
    if cmd == 0:
        wh = randint(0, len(tester))
        tester.insert(i, wh)
    #remove operation
    elif cmd == 1:
        if len(tester) < 1:
            continue
        wh = randint(0, len(tester) - 1)
        tester.remove(wh)
    #get operation
    elif cmd == 2:
        if len(tester) < 1:
            continue
        wh = randint(0, len(tester) - 1)
        tester.get(wh)
    #set operation
    else:
        if len(tester) < 1:
            continue
        wh = randint(0, len(tester) - 1)
        tester.set(i, wh)
