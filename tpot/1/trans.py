with open("AllElectronics.csv", 'r') as file:
    data_lines = file.readlines()
    data = [[] for i in data_lines]
    for i in range(len(data_lines)):
        data[i][:] = (item for item in data_lines[i].strip().split(","))

headers = []
featureList = []
labelList = []
for i in data[0]:
    headers.append(i)  # 提取第一行类别名称
del(data[0])

for row in data:
    labelList.append(row[-1])
    rowDict = {}
    for i in range(1,len(row)-1):    # 把每一行转换成一个字典，便于直接利用sklearn直接提供的库函数
        rowDict[headers[i]] = row[i]
    featureList.append(rowDict)
print(labelList)
print(featureList)