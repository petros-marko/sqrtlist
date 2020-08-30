from sqrtlist import SqrtList
from random import randint

#simple utility for testing the correctness of list operations on sqrtlist

tester = []
testee = SqrtList()

#perform 1e5 operations on the python list and the sqrtlist and check for any mismatch on their effect
#there should be none
#each time an operation is decided randomly with equal probability
#if the operation chosen is not possible on the current list, it is just skipped
for i in range(100000):
    cmd = randint(0, 3)
    #insert operation
    if cmd == 0:
        wh = randint(0, len(tester))
        tester.insert(wh, i)
        testee.insert(i, wh)
        if str(tester) != str(testee).split(' || ')[0]:
            print('insertion error')
    #remove operation
    elif cmd == 1:
        if len(tester) < 1:
            continue
        wh = randint(0, len(tester) - 1)
        tester.pop(wh)
        testee.remove(wh)
        if str(tester) != str(testee).split(' || ')[0]:
            print('deletion error')
    #get operation
    elif cmd == 2:
        if len(tester) < 1:
            continue
        wh = randint(0, len(tester) - 1)
        if tester[wh] != testee.get(wh):
            print('access error')
    #set operation
    else:
        if len(tester) < 1:
            continue
        wh = randint(0, len(tester) - 1)
        tester[wh] = i
        testee.set(i, wh)
        if str(tester) != str(testee).split(' || ')[0]:
            print('setting error')
    print(tester)
    print(testee)
