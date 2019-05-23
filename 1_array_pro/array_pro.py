# -*- encoding:utf-8 -*-
import sys

"""
关于数组的算法集锦
"""

"""
https://leetcode.com/tag/array/
"""


def three_sum_closest(a, target):
    n = len(a)
    a = sorted(a)
    sum = 0
    closest_tmp = sys.maxsize
    for i in range(0, n-1):
        if i > 1 and a[i] == a[i+1]:
            continue
        right = n-1
        left = i+1
        dis = a[i] - target
        while True:
            if right <= left:
                break
            tmp = a[right] + a[left] + dis
            if tmp < closest_tmp:
                closest_tmp = tmp
                sum = a[right] + a[left] + a[i]
            if tmp > 0:
                right -= 1
            elif tmp == 0:
                return target
            else:
                left += 1
    return sum

def three_sum_closest_test():
    a = [1, -1, 2, 5, 6, 8, 5, 4]
    c = three_sum_closest(a, 1)
    print(c)



if __name__ == '__main__':
    three_sum_closest_test()
