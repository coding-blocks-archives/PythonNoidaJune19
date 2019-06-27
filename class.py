class A(object):
    x = 5
class B(A):
    pass
class C(A):
    x = 10
class D(B):
    pass
class E(D, C):
    pass

e = E()
print(e.x)
