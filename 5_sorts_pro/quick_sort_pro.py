# -*- encoding=utf-8 -*-


def quick_sort_1(to_sort):
    """

    :param to_sort:
    :return:
    """
    if to_sort is None:
        return
    if len(to_sort) == 0 or len(to_sort) == 1:
        return to_sort

    # __qs_1(to_sort, 0, len(to_sort) - 1)
    __qs_2(to_sort, 0, len(to_sort) - 1)

    return to_sort


def __qs_1(to_sort, low, high):
    """

    :param to_sort:
    :param low:
    :param high:
    :return:
    """
    if low >= high:
        return

    mid = __partition_1(to_sort, low, high)
    __qs_1(to_sort, low, mid-1)
    __qs_1(to_sort, mid+1, high)


def __partition_1(to_sort, low, high):
    """

    :param to_sort:
    :param low:
    :param high:
    :return:
    """
    tmp = to_sort[low]
    i = low
    for j in range(low+1, high+1):
        if to_sort[j] <= tmp:
            i += 1
            to_sort[j], to_sort[i] = to_sort[i], to_sort[j]

    to_sort[i], to_sort[low] = to_sort[low], to_sort[i]
    return i


def qs_demo_1():
    a = [3,2,4, 2, 4, 1, 3]
    quick_sort_1(a)
    print(a)


def __qs_2(to_sort, low, high):
    """

    :param to_sort:
    :param low:
    :param high:
    :return:
    """
    if low >= high:
        return

    mid = __partition_2(to_sort, low, high)
    __qs_2(to_sort, low ,mid-1)
    __qs_2(to_sort, mid+1, high)


def __partition_2(to_sort, low, high):
    start, end, key = low, high, to_sort[low]
    while start < end:
        while to_sort[end] >= key and start < end:
            end -= 1
        to_sort[start] = to_sort[end]
        while to_sort[start] <= key and start < end:
            start += 1
        to_sort[end] = to_sort[start]
    to_sort[end] = key
    return end




if __name__ == '__main__':
    qs_demo_1()