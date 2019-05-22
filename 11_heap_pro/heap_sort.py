# -*- encoding:utf-8 -*-


def build_heap(a, n):
    """
    建堆时间复杂度为O(n)
    :param a:
    :param n:
    :return:
    """
    start = int((n-1)/2)
    for i in range(start, -1, -1):
        heapify(a, n, i)

def heapify(a, n, i):
    while(True):
        max_pos = i
        if i*2+1 < n and a[i] < a[i*2+1]:
            max_pos = i*2+1
        if i*2+2 < n and a[max_pos] < a[i*2+2]:
            max_pos = i*2+2
        if max_pos == i:
            break
        a[i], a[max_pos] = a[max_pos], a[i]
        i = max_pos


def heap_sort(a):
    n = len(a)
    build_heap(a, n)
    k = n-1
    while k > 0:
        a[0], a[k] = a[k], a[0]
        k = k - 1
        heapify(a, k, 0)

def heap_sort_test():
    a = [5, 4, 6, 8, 1, 2, 16, 21, 0, -1]
    heap_sort(a)
    print(a)

if __name__ == '__main__':
    heap_sort_test()



