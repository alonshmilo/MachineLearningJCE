#func

def func1(a, b=4, c=4):
    print("a:", a, "b:", b, "c:",c)
print("#1:")
func1(2,c=56)

print("#2:")
func1(b=1, c=55, a=45)

print("-------------------------------------------------")

def func2(a, L=[]):
    print(id(L))
    L.append(a)
    return L

print(func2(1))
print(func2(2))
print(func2(3))
print(" ")
print("L is nottt initializing!!!")

print("-------------------------------------------------")

def func3(p1, *p2, **p3):
    print(p1)
    print(p2)
    print(p3)

func3(123)
func3(123, 'aaa', 1234)
func3(123, 'aaa', 1234, v1=1, v2=2)
func3(123, 'aaa', 'sgsdg', 2345, v1=1, v2=2)


print(" ")
print("* is tuple, ** is map")

print("-------------------------------------------------")
print("test line", ",")
print("test lineee")
