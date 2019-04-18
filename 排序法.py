#冒泡排序
for i in range(7,-1,-1): #扫描次数
    for j in range(i):
        if data[j]>data[j+1]:
            data[j],data[j+1] = data[j+1],data[j]  #比较相邻两数
    print('第%d次排序后的结果是:'%(8-i))  #将各次扫描后的结果打印出来
    for j in range(8):
        print('%3d'%data[j],end=' ')
    print()
