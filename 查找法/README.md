## 顺序查找法
### 实现过程
将数据一项一项地按顺序逐个查找，所以不管数据如何，都得从头到尾遍历一次。此法的优点是文件在查找前不需要进行任何的处理与排序，缺点为查找速度较慢。顺序查找是
一种适用于小数据文件的查找方法。
### 代码实现
```python
while val != -1:  #输入查找键值val，初始键值val=0，如果键值val=-1，则离开
    find = 0
    val = int(input('请输入查找键值:'))
    for i in range(80):
        if data[i] == val:
            print('在第%3d个位置找到键值[%3d]'%(i+1,data[i]))
            find += 1
    if find==0 and val!=1:
        print('######没有找到[%3d]#####'%val)
```
## 二分查找法
### 实现过程
二分查找法是将数据分割成两份，再比较键值与中间值的大小，如果键值小于中间值，可确定要查找的数据在前半段，否则在后半段。如此分割数次直到找到或确定不存在为止。
### 代码实现
```python
def bin_search(data,val):
    low = 0
    high = 49
    while low <= high and val != -1:
        mid = int((low+high)/2)
        if val  <data[mid]:
            print('%d介于位置%d[%3d]和中间值%d[%3d]之间，找左半边'\
                   %(val,low+1,data[low],mid+1,data[mid]))
            high = mid-1
        elif val > data[mid]:
            print('%d介于中间值位置%d[%3d]和%d[%3d]之间，找右半边'\
                   %(val,mid+1,data[mid],high+1,data[high]))
            low = mid+1
        else:
            return mid
    return -1
```
#
