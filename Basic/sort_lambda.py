# 这个示例可以知道
# 1. 函数可以作为参数进行传递
#    通过这种方法可以将函数做更进一步的抽象
# 2. lambda 的用法，使得调用这类函数更简单
# 一个通用的排序算法
def sort_list_comm(work , key):
  for j in range(len(work)-1):
    for i in range(len(work)-1):
        if key(work[i]) > key(work[i+1]):
            work[i],work[i+1] = work[i+1],work[i]

# 普通list排序
work = [2,9,6,5]
sort_list_comm(work, lambda x :x)
print work

#  OUTPUT:
#  [2, 5, 6, 9]

# 将排序规则，通过key传入，key是一个函数
# 取每个元祖中的第一个元素进行排序
work = [(1,4),(5,1),(2,3)]
sort_list_comm(work, lambda x: x[1])
print work

#  OUTPUT:
#  [(5, 1), (2, 3), (1, 4)]

# 元祖中最大的元素进行排序
work = [(1,4),(5,1),(2,3)]
sort_list_comm(work, lambda x: max(x))
print work

#  OUTPUT:
#  [(2, 3), (1, 4), (5, 1)]

