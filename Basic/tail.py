# coding=utf-8
import sys
import time

class Tail():
  def __init__(self, file_name, callback=sys.stdout.write):
    self.file_name = file_name
    self.callback = callback
  
  def follow(self, n=10):
    try:
      # 打开文件
      with open(self.file_name) as f:
        self._file = f
        # 到文件的最后
        self._file.seek(0,2)
        # 存储文件的字符长度
        self.file_length = self._file.tell()
        # 打印最后10行
        self.showLastLine(n)
        # 持续读文件
        while True:
          line = self._file.readline()
          if line:
            self.callback(line)
          time.sleep(1)
    except Exception , e:
      print 'open file error'
    
  def showLastLine(self, n):
      # 一行大概100个吧，这个数可以改成1或者1000 都行
      len_line = 100
      # n默认是10，也可以follow的参数传过来
      read_len = len_line*n
      # 用last_lines存储最后要处理的内容
      while True:
        # 如果要读取的1000个字符，大于之前存储文件长度，说明文件很小，可以直接读完返回
        # 读完文件，直接break
        if read_len > self.file_length:
          self._file.seek(0)
          last_lines=self._file.read().split('\n')[-n:]
          break
        # 先读倒数1000个，然后判断1000个字符里换行符的数量
        self._file.seek(-read_len,2)
        last_words = self._file.read(read_len)
        # count是换行符的数量
        count = last_words.count('\n')
        
        if count >=n:
          # 如果换行符的数量大于10 ,那就很好处理，直接截取返回
          last_lines = last_words.split('\n')[-n:]
          break
        # 换行符不够10个
        else:
          # 不够10行
          # 如果一个换行符也没有，那么我们就认为一行大概是100个
          if count == 0:
            len_perline = read_len
          # 如果有换行符，但是不足10个，就取一个平均值
          # 比如是4个的时候，就是1000/4=250个字符
          else:
            len_perline = read_len/count
            
          # 重新计算要读取的长度为2500，继续重新判断
          read_len = len_perline * n
      for line in last_lines:
          self.callback(line + '\n')

if __name__ == '__main__':
    # 使用默认的sys.stdout.write打印到屏幕
    py_tail = Tail('/data/mysqldata/3306/mysql-error.log')
    py_tail.follow()
