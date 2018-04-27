def gensquares(N):
    for i in range(N):
        yield i ** 2

for i in gensquares(5):
    print(i)

x = gensquares(3)
print(next(x))
print(next(x))
print(next(x))


def buildsquares(N):
    res = []
    for i in range(N):
        res.append(i ** 2)
    return res

print(buildsquares(3))
