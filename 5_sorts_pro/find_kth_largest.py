# -*- encoding:utf-8 -*-
import random


def findKthLargest_quick(nums, k: int) -> int:
    """
    leetcode 215，不加random，600ms， 加了random, 40ms
    :param nums:
    :param k:
    :return:
    """
    if nums is None:
        return
    if len(nums) == 0 or k > len(nums):
        return
    if len(nums) == 1 and k == 1:
        return nums[0]

    def _partitation(to_sort, low, high):
        rr = random.randint(low, high)
        to_sort[rr], to_sort[low] = to_sort[low], to_sort[rr]
        j, provit = low, to_sort[low]
        for i in range(low + 1, high + 1):
            if to_sort[i] > provit:
                j += 1
                to_sort[i], to_sort[j] = to_sort[j], to_sort[i]
        to_sort[j], to_sort[low] = to_sort[low], to_sort[j]
        return j

    def _find_k(to_sort, low, high):
        mid = _partitation(to_sort, low, high)
        if mid + 1 > k:
            return _find_k(to_sort, low, mid - 1)
        elif mid + 1 < k:
            return _find_k(to_sort, mid + 1, high)
        else:
            return to_sort[mid]

    return _find_k(nums, 0, len(nums) - 1)


def findKthLargest_heap(nums, k):
    if nums is None:
        return
    if len(nums) == 0 or len(nums) < k:
        return
    if len(nums) == 1:
        return nums[0]

    def heapify(nums, idx, end):
        while True:
            large_idx = idx
            left_idx = idx * 2 + 1
            right_idx = idx * 2 + 2
            if left_idx <= end and nums[left_idx] > nums[large_idx]:
                large_idx = left_idx
            if right_idx <= end and nums[right_idx] > nums[large_idx]:
                large_idx = right_idx

            if large_idx != idx:
                nums[large_idx], nums[idx] = nums[idx], nums[large_idx]
                idx = large_idx
            else:
                break

    nums_count = len(nums)
    for i in range(int((nums_count-2)/2), -1, -1):
        heapify(nums, i, nums_count - 1)
    for j in range(k):
        last = nums_count - 1 - j
        nums[0], nums[last] = nums[last], nums[0]
        heapify(nums, 0, last-1)
    return nums[nums_count - k]


def fklh_demo():
    nums = [3, 2, 1, 5, 6, 4]
    a = findKthLargest_heap(nums, 2)
    print(a)
    print(nums)

if __name__ == '__main__':
    fklh_demo()



