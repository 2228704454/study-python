#常出现的语法错误
# long=input('请输入你的体重')
#if long>=60:  input输入的函数是str类型，而60是int类型，两者之间不能相互比较
 #   print('抱歉，你很肥胖')

long=input('请输入你的体重')
if int(long)>=60:         #将long 转换成为int类型进行比较
    print('抱歉，你很肥胖')
    print(type(60))

#while i < 10： i这个变量没有赋值
#    print(i) 括号用的是中文括号
#没有正确的语法

i=20             #将变量i进行赋值
while i <30:
    print(i)     #改掉中文的括号
    i=i+1        # 添加一个正确的语法

# for i in range(3):
  #  yonghu=input('请输入用户名')
   # mima=input('请输入密码')
    #if yonghu='longlufang' and mima='211223':    一个等号是赋值，两个等号才是比较
        #print('登陆成功')
        #break
   # else:
       # print('输入有误，请重新输入')
#else:
   # print('对不起，错误次数过多。请24小时后重试')

#for i in range(3):
  #yonghu=input('请输入用户名')
  #mima=input('请输入密码')
 #if yonghu=='longlufang' and mima=='211223':
        #print('登陆成功')
        #break
  #else:
       #print('输入有误，请重新输入')
#else:
   #print('对不起，错误次数过多。请24小时后重试')

#lst=[11,22,33,44]
#print(lst[4])  列表索引是0开始计算的

#lst=[11,22,33,44]
#print(lst[3])

#异常处理机制 try与except结构
try:
    a=int(input('请输入一个整数'))
    b=int(input('请输入一个整数'))
    sh=a/b
    print('结果为',sh)
except ZeroDivisionError:
    print('对不起，被除数不能为0')
except ValueError:
    print('输入数据类型必须为数字串')
print('程序结束')

# try ...except...else 结构
try:
    c=int(input('请输入一个整数'))
    d=int(input('请输入一个整数'))
    fc=a/b

except BaseException as e:
    print('出错了',e)
else:
    print('结果为', fc)

#try...except...else...finally 结构
