# coding:utf-8


def searchInsert(nums, target):
    """
    leetcode 35题，搜索插入位置
    :param nums:
    :param target:
    :return:
    """
    start = 0
    end = len(nums) - 1
    while start != end:
        mid = (start + end) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            end = mid
        else:
            start = mid + 1

    if target > nums[start]:
        return start + 1
    else:
        return start