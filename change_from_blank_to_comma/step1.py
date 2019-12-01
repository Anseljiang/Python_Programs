with open('1.txt','r') as fr:
    for line in fr.readlines():
        print("读取的数据为: %s" %(line))
        if ' ' in line:
            with open('2.txt','a') as fw:
                fw.write(','.join(line.split())+'\n') #注意，最后一行会是空行