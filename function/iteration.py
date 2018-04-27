print(list(map(ord, 'spam')))

res = [ord(x) for x in 'spam']
print(res)

print([x**2 for x in range(10)])

print([x for x in range(5) if x % 2 == 0])

print(list(filter((lambda x: x % 2 == 0), range(5))))

req=[]
for x in range(5):
    if x % 2 == 0:
        req.append(x)
print(req)


def gensequences(N):
    for i in range(N):
        yield i ** 2

for i in gensequences(5):
    print(i)