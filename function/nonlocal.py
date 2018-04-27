def func():
    name1='int'
    def f2():
        name1='string'
        print(name1)
    f2()
func()

def tester(start):
    state = start
    def nested(label):
        nonlocal state
        print(label, state)
        state += 1
    return nested

F=tester(11)
F('spam')
F('foo')
F('eggs')


# 这个方法不太明白， 而且这个方法语法不对， 需要研究修改

# def tester(start):
#     def nested(label):
#         print(label, nested.state)
#     nested.state += 1
#     nested.state = start
#     return nested
#
# M = tester(0)
# M('spam')
# M('ham')