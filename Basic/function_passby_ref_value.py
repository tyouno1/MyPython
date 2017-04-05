# 传值
gname = 'globalname'
def test4(gname):
  print gname
  gname = 'localname'
  print gname

test4(gname)
print gname

# OUTPUT
# globalname



# 传引用,list是传引用的
gname = ['globalname']
def test4(gname):
  print gname[0]
  gname[0] = 'localname'
  print gname[0]

test4(gname)
print gname[0]

# OUTPUT
# localname
