#字符串的驻留机制
a='gui'
b="gui"
print(a,id(a))
print(b,id(b))

s1='hui' #字符串的id相同
s2='hui'
print(s1 is s2)

s1=''  #长度为0的id相等
s2=''
print(s1 is s2)

s1='o' #长度为1的id相等
s2='o'
print(s1 is s2)

#字符串的查询
s='long'
print(s.find('g')) #查询字符串出现的第一个位置，如果不存在出现报错
print(s.rfind('o')) #查询字符串出现的最后一个位置，如果不存在出现报错

#字符串大小写转换方式    ,转换过后内存地址会发生改变
a='longlufang'  #所有字符转成大写
s=a.upper()
print(s)

f=a.lower() #所有字符转成小写
print(f)

g='Mong Yun' #大写转小写，小写转大写
c=g.swapcase()
print(c)

p='mong' #第一个字符转成大写，其余小写
d=p.capitalize()
print(d)

u='MONg,SHUI,OUJIO' #单词第一个字符大写，剩下的小写
m=u.title()
print(m)

#字符串的常规操作
e='三体' #居中对齐
print(e.center(52,'+'))
#左对齐
print(e.ljust(20,'_'))
#右对齐
print(e.rjust(20,'+'))
#右对齐，默认参数0
print(e.zfill(20))

#字符串的分割
h='hello,world,python'
print(h.split(sep='|'))

#判断字符串
print(1,'hong'.isidentifier()) #判断是否是合法的标识符
print(2,'hong'.isspace()) #判断是否全由空白字符组成
print(3,'hong'.isspace()) #判断是否全是由字母组成
print(4,'hong'.isalpha()) #判断是否全是由十进制数字组成
print(5,'hong'.isnumeric()) #判断是否全是由数字组成
print(6,'hong'.isalnum()) #判断是否全是由数字组成

#字符串的替换操作
lis='wai,wai,wai,xie,xie'
print(lis)
print(lis.replace('wai','wang'))

#元组和列表中的字符串的合并
lst=['reng','yi','dao','dei']
print('+'.join(lst))
print('-'.join('rang'))

#切片操作
ls='ming,tian'
print(ls[2:5:4])

#格式化字符串
name='李大爷'    #百分号法
age=20
print('我叫%s,今年%i岁'%(name,age) )
print('我叫{0},今年{1}'.format(name,age)) #format函数法
print('%10d' % 99) #10表示宽度
print('% .3f' % 3.1415926) #.3表示小数点前三位

#字符串的编码转换
s='散入武林松柏中'
byte=s.encode(encoding='GBK') #使用GBK格式编码，一个中文占两个字节
print(byte)
print(byte.decode(encoding='GBK')) #解码

p='西北望长安'
byte=p.encode(encoding='UTF-8') #使用UFT-8格式编码，一个中文占三个字节
print(byte)
print(byte.decode(encoding='UTF-8')) #解码





