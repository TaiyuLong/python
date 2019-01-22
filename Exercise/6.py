a = 10
b = 20
list = [1, 2, 3, 4, 5]

print("list=[1, 2, 3, 4, 5]")

if( a in list ):
    print("当a=", a, "时，变量a在list中")
else:
    print("当a=", a, "时，变量a不在list中")

if( b in list ):
    print("当b=", b, "时，变量b在list中")
else:
    print("当b=", b, "时，变量b不在list中")

# 修改变量a的值
a = 2
if( a in list):
    print("当a=", a, "时，变量a在list中")
else:
    print("当a=", a, "时，变量a不在list中")

# 修改变量b的值

b = 4
if( b in list ):
    print("当b=", b, "时，变量b在list中")
else:
    print("当b=", b, "时，变量b不在list中")
