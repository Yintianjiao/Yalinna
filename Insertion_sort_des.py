import time


def descending_order(a_sort):
    a_len = len(a_sort)
    t_start = time.time()
    for j in range(1, a_len):
        key = a_sort[j]
        i = j - 1
        while i >= 0 and a_sort[i] > key:
            a_sort[i+1] = a_sort[i]
            i = i - 1
        a_sort[i+1] = key
    t_end = time.time()
    print("执行时间为%f"%(t_end - t_start))
    return a_sort


l = input("请输入您需要排序的整数序列，不同数字之间用逗号隔开:")
l = list(l.split(','))
l_num = [eval(num) for num in l]
l_sort = descending_order(l_num)
print(l_sort)