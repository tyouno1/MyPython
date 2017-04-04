#coding:utf-8
# 列表推到式，不光可以使用简单的表达式，也可以使用函数
iter = [0,1,2,3,4,5]

def filter(x):
    return x%2 == 0

def translate(x):
    return x*x

# 效果等同于 [x*x for x in iter if x%2 == 0]
print [ translate(x) for x in iter if filter(x) ]
