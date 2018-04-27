def func1():
    X = 88
    def func2():
        print(X)
    return func2

action=func1()
action()


def func3():
    Y=99
    def func4():
        print(Y)
    func4()
func3()


def f1():
    H=3
    def f2():
        def f3():
            print(H)
        f3()
    f2()
f1()