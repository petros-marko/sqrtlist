from sqrtlist import SqrtList
from random import randint

tester = []
testee = SqrtList()

for i in range(randint(20, 1000)):
    wh = randint(0, i)
    tester.insert(wh, i)
    testee.insert(i, wh)

print(str(tester) == str(testee))

for i in range(9 * len(tester) // 10):
    wh = randint(0, len(tester) - 1)
    tester.pop(wh)
    testee.remove(wh)

print(str(tester) == str(testee))

for i in range(randint(20, 1000)):
    wh = randint(0, len(tester) - 1)
    tester[wh] = i
    testee.set(i, wh)

print(str(tester) == str(testee))

match = True
for i in range(randint(20, 1000)):
    wh = randint(0, len(tester) - 1)
    if tester[wh] != testee.get(wh):
        match = False

print(match)

