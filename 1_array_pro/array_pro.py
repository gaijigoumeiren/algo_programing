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
            if abs(tmp) < abs(closest_tmp):
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


def fourSum_v1(nums, target):
    """
    这是我第一版的fourSum，速度超慢，39%
    一般人们都是化成twosum来做，前几层都是循环，直到twosum
    我在leetcode的讨论区看到一个哥们的Nsum的解决方案，也是化成twosum,但是没有用hashmap，在4sum的情况下领先100，时间复杂度最坏情况下为o(n^3)

    :param nums:
    :param target:
    :return:
    """
    n = len(nums)
    if n == 0:
        return []
    result = []
    nums.sort()
    # 加上这行判定后，速度从964 ms降到172ms，超过62%
    if 4 * nums[0] > target or 4 * nums[-1] < target:
        return []
    def three_sum(nums, start, end, target):
        result = []
        # 加上这行判定后，速度从964 ms降到172ms，超过62%
        if 3 * nums[start] > target or 3 * nums[end] < target:
            return []
        for i in range(start, end - 1):
            if i > start and nums[i] == nums[i - 1]:
                continue
            t_target = target - nums[i]
            right = end
            left = i + 1
            while True:
                if left >= right:
                    break
                tmp = t_target - nums[right] - nums[left]
                if tmp == 0:
                    result.append([nums[i], nums[right], nums[left]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    right -= 1
                elif tmp > 0:
                    left += 1
                else:
                    right -= 1
        return result

    for i in range(0, n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        t_target = target - nums[i]
        three_s = three_sum(nums, i + 1, n - 1, t_target)
        for th in three_s:
            th.append(nums[i])
            result.append(th)

    return result


def four_sum_test():
    a = [1, 0, -1, 0, -2, 2]
    rr = fourSum_v1(a, 0)
    print(rr)

def rectCover(number):
    # write code here
    """

    :param number:
    :return:
    """
    result = [0, 1, 2]
    if number == 0:
        return 0
    if number <= 2:
        return result[number]
    for i in range(3, number+1):
        result.append(result[i - 1] + result[i - 2])
    return result[-1]


"""
求一个数二进制中1的个数
https://www.nowcoder.com/questionTerminal/8ee967e43c2c4ec193b040ea7fbb10b8
rectCover(number) {
    if ( number < 1 ) return 0
    g = 1, f = 2;
    while (number-=1 ) {
        f = f + g;
        g = f - g;
    }
    return g;
}
"""


def reOrderArray(array):
    """
    输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
    https://www.nowcoder.com/practice/beb5aa231adc45b2a5dcc5b62c93f593?tpId=13&tqId=11166&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
    :param array:
    :return:
    """
    # write code here
    i = len(array) - 1
    j = i
    while j >= 0 and i >= 0:
        if array[i] % 2 == 0:
            i -= 1
        else:
            if j < i:
                j = j - 1
            else:
                j = i - 1
            while j >= 0 and array[j] % 2 != 0:
                j -= 1
            if j >= 0:
                tmp = array[j]
                array[j:i] = array[j + 1:i + 1]
                array[i] = tmp
                i -= 1
    return array


def orc_larger_than_half(arr):


if __name__ == '__main__':
    # three_sum_closest_test()
    rectCover(3)
