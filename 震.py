#元组的创建方式
m=('fang','song',90,'遮')#直接括号法
print(m)

h=tuple(('gui','qu','lai') ) #添加函数tuple
print(h)

#向元组中的列表添加元素
t=(10,[20,30],9)
print(t)
t[1].append(99) #使用函数append
print(t)

#元组的遍历
s=(1,2,13,5,9,)
for item in s:
    print(item)

#集合的创建
s={1,2,3,4,5,6} #直接括号法
print(s)

f=set(range(10)) #使用内置函数set
print(f)

#集合的判断
g=set(range(8))
print(10 in g)
print(10 not in g)

#增加元素
g.add('光')
print(g)
g.update(range(10,20))
print(g)

#删除
g.remove(2)
print(g)
g.discard(100)
print(g)
g.pop()
print(g)
g.clear()
print(g)

#判断集合是否相等
a1={1,2,3,4,5}
a2={5,4,3,2,1}
print(a1==a2)

#判断一个集合是否是另一个集合的子集
b1={1,2,3,4,5678}
b2={1,2,3}
print(b2.issubset(b1))

#判断一个集合是否是另一个集合的超集
print(b1.issuperset(b2))

#判断两个集合有没有交集
print(b2.isdisjoint(b1))

#集合的数学操作
print(b1.intersection(b2)) #求交集
print(b1.union(b2))  #求并集
print(b1.difference(b2)) #求差集

#集合生成式
o={i for i in range(10)}
print(o)

