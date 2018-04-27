x = 88
def func1(m):
    global x
    x = 99 + m

func1(3)
print(x)


y,z = 1,2
def func2():
    global q
    q = y + z
func2()
print('q is-----', q)


a = 7
def func3():
    global a
    a=9
    print('a in dunc3 is:', a)

func3()
print('a in global is:', a)