cheng= dict(nane='辰',tue=200,fix='东') #创建字典
print(cheng)

cheng['明']=100 #添加字典元素
print(cheng)

print(cheng.get('nane')) #查找字典元素
 
print('tue' in cheng) #判断kyes


keys=cheng.keys() #获取所有keys
print(keys)
print(type(keys))
print(id(keys))

lu=cheng.values() #获取所有valuse
print(lu)
print(type(lu))

items=cheng.items() #获取所有字典元素
print(items)
print(type(items))
print(list(items))

for items in cheng: #字典的遍历
    print(items)
# 字典生成式
long=['ni','shi','sha','bi'] # 创建列表
fang=[20,30,40,50]
hui={item:price  for item ,price in zip(long,fang)}    #字典生成式
print(hui)

kan=['西','北','望','长','安']
qian=[9,5,8,7,3,1,0]
som={itme:price for item,price in zip (kan,qina) }


















