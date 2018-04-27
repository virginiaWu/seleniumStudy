print('old list is:', list(open('script.py')))
withNotrip=[line.rstrip() for line in open('script.py')]
print('split wrap list is:', withNotrip)
print('tuple is:', tuple(open('script.py')))
print('sorted list is:', sorted(open('script.py')))



def f(a, b, c, d):
    print(a, b, c, d)

f(1,2,4,5)
# f(*open('script.py'))

R=range(5)
I=iter(R)
# for i in range(10):
#     print(next(I))

while True:
    try:
        B=next(I)
    except StopIteration:
        break
    print(B)


# map function
foo=list(map(abs, (-1,-2,4)))
print('abs list is:', foo)

# filter function
filterTest=['spam', '', 'ni', 'foo', '']
print('after filter list is:', list(filter(bool, filterTest)))

D=dict(a=1, dfa=2, cc=6)
print('dict is:', D)
for key in D.keys():
    print('key:', key)

for (k, v) in D.items():
    print('key:', k, ' value:', v)
