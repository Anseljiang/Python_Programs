#消除最后一行的空行
import os   
f = open('2.txt','rb+')
f.seek(-2 ,os.SEEK_END)
f.truncate()
f.close()