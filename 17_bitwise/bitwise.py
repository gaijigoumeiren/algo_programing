# -*- encoding:utf-8 -*-
import sys

def number_of_1(n):
    """
    数字二进制中1的个数，负数用补码表示
    解法1：如果一个数的二进制（补码）不是0，那么至少有一个1，那么n-1的效果是n的二进制的最右边的1变成0，而从这一位开始往右的所有0都变成1，
    让n&n-1，那么，最右边一位1变成0，而左边的所有都不收影响；结下找与操作后的结果中有多少个1。
    这里正数是肯定没有问题的，问题在于负数；
        -1 的补码：1111 1111; -1-1 = (-1)+(-1) = 1111 1111 + 1111 1111 = 1111 1110 反码：1111 1101 原码： 1000 0010：-2
        -1 & -2 = 1111 1111 & 1111 1110 = 1111 1110
        -3 的补码是 1111 1101 与 -2 1111 1110 = 1111 1100
        按理说这么一路下来就行了，但是python令人尴尬的地方就来了，它的int类型是可扩展的，比如说我们现在说int是32位，4字节，或者说64位8字节，
        但是python是可以超过这个限制转化为long的，这就导致了，如果直接与n & (n-1)的话，n-1可以无限小，也就是符号位无限高，这tm就永无尽头，while语句运行不完。
        所以要提前把它的长度定在32位或者64位，怎么定呢，我们就让如果小于0的话，直接与ffff ffff 32个1相与，这样的话高于32位的都被搞成0了，不就行了。

    :param n:
    :return:
    """
    result = 0
    if n < 0:
        n = n & 0xffffffff
    while n:
        n = n & (n-1)
        result += 1
    return result


def number_of_1_2(n):
    """
    数字二进制中1的个数，负数用补码表示
    解法2：上一个解法固定了32位，那这个直接也固定32位，往右移32次，每次与1相与，如果结果==1，那么就结果+1

    :param n:
    :return:
    """
    result = 0
    for _ in range(32):
        if n & 1 == 1:
            result += 1
        n = n >> 1
    return result


def subset(nums):
    """
    给定一个不重复的数组，返回这个数组的所有子集 leetcode 78
    解法1：时间超过69%，空间超过11%，卧槽这个时间复杂度感觉有O(n*2**n)
        是这样的，子集吗，其实就是某个元素在或者不在这个子集里面嘛，那么我们用一个长度为数组长度的二进制数代表某个子集里面包含哪些数字，那一共需要2**len(nums)个二进制，正好是0-2**len(nums)-1:
        然后循环看到底是哪一位是1，是1就添加到子集里面
    但是这种解法并不是很高效，还有一种更加高效的
    :param nums:
    :return:
    """
    if not nums or len(nums) == 0:
        return []
    result = []
    for n in range(2 ** len(nums)):
        tmp = []
        i = 0
        while n:
            if n & 1 == 1:
                tmp.append(nums[i])
            i += 1
            n = n >> 1
        result.append(tmp)
    return result


def subset_1(nums):
    """
    比上一种速度要快很多，首先构建[]的子集，然后构建[1]的子集，然后构建[1, 2]的子集，然后构建[1, 2, 3]的子集。
    这种的速度更加快。
    :param nums:
    :return:
    """
    result = [[]]
    for i in nums:
        for j in range(len(result)):
            result.append(result[j]+[i])
    return result

def subset_with_dup(nums):
    """
    给定一个有重复的数组，返回它所有的子集，子集不能有重复数组。leetcode 90
    解法：解法是逐个添加，在之前的记过基础上，构造更长数组的子集，但如果出现了重复的元素的话，子集就会有重复，为了避免重复，首先要做一个排序，然后后一个在构造子集的时候，就需要是否与之前的一个元素一样不一样了，不一样的话，就一样处理，如果一样，那么它只能往上一轮构造的一部分结果上添加，这部分就是上部分新加入结果集的那部分。
    :param nums:
    :return:
    """
    result = [[]]
    nums.sort()
    tmp = []
    for idx, n in enumerate(nums):
        if idx > 0 and nums[idx] == nums[idx - 1]:
            tmp_1 = []
            for j in tmp:
                t = j + [n]
                result.append(t)
                tmp_1.append(t)
            tmp = tmp_1
        else:
            tmp = []
            for j in range(len(result)):
                t = result[j] + [n]
                result.append(t)
                tmp.append(t)
    return result

def readBinaryWatch(num):
    """
    leetcode 401，二进制手表。
    讨巧解法，速度很快的
    :type num: int
    :rtype: List[str]
    """
    return ["%d:%02d" % (n, m) for n in range(12) for m in range(60) if (bin(n) + bin(m)).count('1') == num]


def readBinaryWatch_1(num):
    """
    leetcode 401，二进制手表。
    老实人解法：
    :param num:
    :return:
    """
    format_str = "%d:%02d"
    # 回头再说吧，今天不像看了。



if __name__ == '__main__':
    print(number_of_1_2(-1))
    print(sys.maxsize)
    a = [1]
    print(a+[2])

