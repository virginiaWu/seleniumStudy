import sys
showall1 = lambda x: list(map(sys.stdout.write, x))

showall1(['spam\n', 'ham\n', 'eggs\n'])

showall2 = lambda x: [sys.stdout.write(line) for line in x]

showall2(['bright\n', 'side\n', 'of\n', 'life\n'])


act = lambda x: lambda y: x + y
print(act(100)(99))


counters = [1,2,3,4,5,6]

def inc(x):
    return x + 3

print(list(map(inc, counters)))

print(list(map((lambda x: x+10), counters)))


def mymap(func, seq):
    res=[]
    for x in seq:
        res.append(func(x))
    return res

print(mymap(inc, counters))


print(list(map(pow, [1, 2, 3], [2,3,4])))    # 1**2, 2**3, 3**4


print(list(filter((lambda x: x>0), range(-5,5))))

from functools import reduce
print(reduce((lambda x, y: x * y), [1,2,3,4]))


def myreduce(func, seq):
    total = seq[0]
    for next in seq[1:]:
        total = func(total, next)
    return total

print(myreduce((lambda x, y: x * y), [1,2,3,4,5]))