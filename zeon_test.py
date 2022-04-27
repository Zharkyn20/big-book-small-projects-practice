def foo(var, a = []):
    a.append(var)
    print(a)

foo(1)
foo(1, [])
foo(1)


class A:
    x = 1

class B(A):
    x = 2

class C(A):
    x = 3

print(A.x, B.x, C.x)
B.x = 3
print(A.x, B.x, C.x)



foo1 = [2, 8 , 9, 12, 22, 24, 16, 17, 19, 21, 31]

foo1 = [x for x in foo1[::2] if x%2 == 0]
print(foo1)
print(foo1[::2])