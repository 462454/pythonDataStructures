# 冒泡排序
def bubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


print(bubbleSort([24, 48, 65, 48, 22, 12, 36, 98, 45]))


def bubbleSort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] < alist[i + 1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubbleSort(alist)
print(alist)


# 短冒泡排序
def bubbleSort(alist):
    flag = True
    passnum = len(alist) - 1

    while passnum > 0 and flag:
        flag = False
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                flag = True
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp

        passnum = passnum - 1


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubbleSort(alist)
print(alist)


# 选择排序
def selectionSort(arr):
    for i in range(len(arr) - 1):
        # 记录最小数的索引
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        # i 不是最小数时，将 i 和最小数进行交换
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr


print(selectionSort([24, 48, 65, 48, 22, 12, 36, 98, 45]))


# 插入排序
def insertionSort(alist):
    for i in range(1, len(alist)):
        currentValue = alist[i]
        pos = i
        while pos > 0 and alist[pos - 1] > currentValue:
            alist[pos] = alist[pos - 1]
            pos = pos - 1

        alist[pos] = currentValue


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertionSort(alist)
print(alist)


# 希尔排序
def shellSort(alist):
    sublistcount = len(alist) // 2

    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)

        print('alist：', alist)

        sublistcount = sublistcount // 2


def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        currentValue = alist[i]

        pos = i
        while pos >= gap and alist[pos - gap] > currentValue:
            alist[pos] = alist[pos - gap]
            pos = pos - gap

        alist[pos] = currentValue


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shellSort(alist)
print(alist)
