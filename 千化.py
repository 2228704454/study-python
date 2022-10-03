#变量的局部变量
def shu(a,b):
    c=a+b       #此时的c是函数定义里的变量，属于局部变量
    print(c)
shu(a=1,b=2)

#变量里的全局变量
name='😘' #此时的表情是属于全局变量
print(name)

def shu(a,b): #在其他函数中也可以输出
    c=a+b
    print(c)
    print(name)
shu(a=2,b=2)

def shu(a,b):
    global d  #函数中的局部变量加了global声明后，可以变换成为全局变量
    d=a+b
    print(d)
shu(a=5,b=2)

print(d)

#递归函数
def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)

print(fac(100))

#斐波那契数列求值
def hou(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return hou(n-1)+hou(n-2)

print(hou(6))

for o in range(1,7):
    print(hou(o))
