def f1(a, b, *c, **d):
    print(a,b,c,d)


f1(1,2,*(3,),**dict(ds=1))



def f2(a, *, b, c='eggs'):
    print(a, b, c)

f2(1,b=2,c=4)

