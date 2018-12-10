import random
import time
# import threading


def print_time(func):
    def wrapper(*args):
        t1 = time.time()
        result = func(*args)
        t2 = time.time()
        print(t2 - t1)
        return result
    return wrapper


@print_time
def bubble_sort(list1):
    for i in range(len(list1) - 1):
        exchange = False
        for j in range(len(list1) - 1 - i):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]
                exchange = True
        if not exchange:
            return


@print_time
def quick_sort(lis):
    def quick__sort(list1):
        list_len = len(list1)
        if list_len <= 1:
            return list1
        tep = list1[random.randint(0, list_len - 1)]
        left = []
        right = []
        for i in range(list_len):
            if tep > list1[i]:
                left.append(list1[i])
            else:
                right.append(list1[i])
        return quick__sort(left) + quick__sort(right)
    return quick__sort(lis)


data = list(range(1000))
random.shuffle(data)
data1 = data
bubble_sort(data1)
print(data1)
print(quick_sort(data))

# @print_time
# def quick_sort1():
#     data = list(range(1000))
#     random.shuffle(data)
#     data2 = data
#     da = quick_sort(data2)
#     print('快速排序', da)


# td1 = threading.Thread(target=bubble_sort1)
# td2 = threading.Thread(target=quick_sort1)
# td1.start()
# td2.start()
