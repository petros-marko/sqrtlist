from sqrtlist import SqrtList
from random import randint

tester = []
testee = SqrtList()

for i in range(10000):
    cmd = randint(0, 3)
    if cmd == 0:
        wh = randint(0, len(tester))
        tester.insert(wh, i)
        testee.insert(i, wh)
        if str(tester) != str(testee).split(' || ')[0]:
            print('insertion error')
    elif cmd == 1:
        if len(tester) < 1:
            continue
        wh = randint(0, len(tester) - 1)
        tester.pop(wh)
        testee.remove(wh)
        if str(tester) != str(testee).split(' || ')[0]:
            print('deletion error')
    elif cmd == 2:
        if len(tester) < 1:
            continue
        wh = randint(0, len(tester) - 1)
        if tester[wh] != testee.get(wh):
            print('access error')
    else:
        if len(tester) < 1:
            continue
        wh = randint(0, len(tester) - 1)
        tester[wh] = i
        testee.set(i, wh)
        if str(tester) != str(testee).split(' || ')[0]:
            print('setting error')
