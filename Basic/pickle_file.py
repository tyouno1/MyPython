#coding:utf8
import pickle

#增
def Create():
    users = {'pc':'123456', 'wd':'123', 'kk':'234'}
    fo = open('users.txt','wb')
    pickle.dump(users,fo)
    fo.close()

#删
def Delete():
    content={}
    f=open('users.txt')
    content = pickle.load(f)
    f.close()
    content.pop('kk')
    f=open('users.txt','wb')
    pickle.dump(content,f)
    f.close()

#改
def Modify():
    content={}
    f=open('users.txt')
    content = pickle.load(f)
    f.close()
    content['pc'] = '666666'
    f = open('users.txt','wb')
    pickle.dump(content,f)
    f.close()
    
def Select():
    content={}
    f=open('users.txt')
    content = pickle.load(f)
    f.close()
    print content
    for k,v in content.items():
        print k,v
        
if __name__ == '__main__':
    Create()
    Delete()
    Modify()
    Select()
