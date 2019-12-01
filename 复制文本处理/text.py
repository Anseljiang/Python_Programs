#https://www.cnblogs.com/j-c-y/p/10565033.html
ff = open('b.txt','w')  #打开一个文件，可写模式
with open('a.txt','r') as f:  #打开一个文件只读模式
    line = f.readlines()
    for line_list in line:
        line_new =line_list.replace('\n','')
        line_new =line_new+' '  #行末尾加上" "
        ff.write(line_new)