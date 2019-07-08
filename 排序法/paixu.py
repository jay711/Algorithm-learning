#冒泡排序,（N）个元素必须执行（N-1）次扫描，第一次扫描需要比较（N-1）次，共比较（N-1）+（N-2）+...+1次
for i in range(7,-1,-1): #扫描次数
    for j in range(i):
        if data[j]>data[j+1]:
            data[j],data[j+1] = data[j+1],data[j]  #比较相邻两数
    print('第%d次排序后的结果是:'%(8-i))  #将各次扫描后的结果打印出来
    for j in range(8):
        print('%3d'%data[j],end=' ')
    print()
    
#选择排序，一开始在所有数据中挑选一个最小项放在第一个位置（假设从小到大排序），再从第二项开始挑选一个最小项放在第二个位置，以此重复，直到完成排序为止
def select(data):
    for i in range(7):
        for j in range(i+1,8):
            if data[i] > data[j]:
                data[i],data[j] = data[j],data[i]
    print()
    
#插入排序，将数组中的元素，逐一与已排序好的数据进行比较，前两个元素先排好，再将第三个元素插入适当的位置，所以这三个元素仍然是已排序好的，接着将第四个元素加入，重复此步骤，直到排序完成为止。
def insert(data):
    for i in range(1,SIZE):  #SIZE为数组大小
        tmp = data[i]   #tmp用于存放数据
        n0 = i-1   #当i=1时，n0=0
        while n0>=0 and tmp<data[n0]:
            data[n0+1] = data[n0]   #就把所有元素往后推一个位置
            n0 = n0-1
data[n0+1] = tmp #最小的元素放到第一个位置

#快速排序
def kuaisu(d,size,lf,rg): #定义快速排序函数，第一项键值为 d[lf],size 为数组长度
     if lf<rg:  #排序数据的左边与右边
         lf_idx = lf+1  
         while d[lf_idx]<d[lf]:  #从左到右，找出大于键值K的“i”，其中键值K为d[lf]
             if lf_idx+1>size:
                break
             lf_idx += 1
         rg_idx = rg
         while d[rg_idx] > d[lf]: #从右向左，找出小于键值K的“j”
             rg_idx -=1
         while lf_idx < rg_idx:  # 假如 i<j
             d[lf_idx],d[rg_idx] = d[rg_idx],d[lf_idx]  #那么Ki与Kj互换
             lf_idx +=1  #回到步骤（2）
             while d[lf_idx]<d[lf]:
                lf_idx += 1
             rg_idx -= 1
             while d[rg_idx] >d[lf]:
                rg_idx -=1
         d[lf],d[rg_idx] = d[rg_idx],d[lf]  #直到i>+j,就将K与Kj交换
         
         kuaisu(d,size,lf,rg_idx-1)   #以rg_idx为基准点分成左右两半以递归方式
         kuaisu(d,size,rg_idx+1,rg)   #分别以左右两半进行排序直至完成排序

# 这是一条测试行
