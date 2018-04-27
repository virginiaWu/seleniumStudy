def mysum(L):
    first, *reset = L
    print('first is----', first)
    print('reset is----', reset)
    return first if not reset else first + mysum(reset)


print(mysum(['eggs', 'spam', 'ham']))


def sumtree(L):
    tot = 0
    for x in L:
        if not isinstance(x, list):
            print('x is list:', x)
            tot +=x
        else:
            print('x is:', x)
            tot += sumtree(x)
    return tot

M=[1,2,[34,5,6], 3,4]
print(sumtree(M))



# 函数注解

def func(a: 'spam'=5, b: (1, 10)=5, c:float=99) -> int:
    return a + b + c


print(func(1, 10))