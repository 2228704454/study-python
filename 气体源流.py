#函数的创建
def long (a,b):
    c=a+b            #运行函数体
    return c         #结束运行
result=long(10,20)   #给出实际参数之后跳转运行
print(result)        #打印结果

#函数的参数传递  位置传参
def long (a,b):     #a和b是形参
    c=a+b
    return c
result=long(10,20)  #10和20是实参
print(result)

#关键字传参
fang=long(a=50,b=20)
print(fang)
#函数的调用
def guang (lu1,lu2):   #函数的形参及定义
    lu1=100
    lu2.append(10)
    print(lu1)
    print(lu2)
n1=11                  #不可变对象 lu1的实际参数
n2=[11,22,33]          #可变对象   lu2的实际参数
guang(n1,n2)
print(n1)
print(n2)
                       #使用位置传参，不可变参数函数无法改变实参值

#函数的返回值
def gui (zhu):
    odd=[] #存奇数
    even=[] #存偶数
    for i in zhu:
        if i%2:       #如果除以2之后为0
            odd.append(i)  #输出结果
        else:
            even.append(i)
    return odd,even   #结束函数，存储返回值
print(gui([10,43,54,56,76,31,50,10,8,])) #调用函数
#1.如果没有返回值，可以不用加return
#2.如果返回值是1，会直接返回结果
#3.如果是多个值，会采用元组的数据类型输出

#函数参数的定义
def lei(a,b=10):   #b是默认值参数
    print(a,b)

lei(100)
#只有一个参数时，有默认参数的值会使用默认参数
lei(20,30)
#有两个参数时，默认参数值会被替换掉

#个数可变的位置参数
def hui(*dong):
    print(*dong)

hui(10)
hui(10,55,33,44,66,)   #可以传多个参数

#个数可变的关键字参数
def hou(**ming):
    print(ming)

hou(a=20,c=44,ll=88)
#个数可变的位置参数和关键字参数只能定义一个，在一个函数的定义过程中，可以有个数可变的位置形参，个数可变的关键字形参，注意事项：个数可变的位置形参要放在前面。

#列表的位置传参
def fun(a,b,c):
    print(a)
    print(b)
    print(c)

gu=[22,33,44,]
fun(*gu)

字典的使用
def ehc(**efi):
    print(efi)

ehc(q=11,b=22,c=33)







