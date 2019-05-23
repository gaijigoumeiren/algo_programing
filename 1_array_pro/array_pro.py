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

if __name__ == '__main__':
    # three_sum_closest_test()
    four_sum_test()
