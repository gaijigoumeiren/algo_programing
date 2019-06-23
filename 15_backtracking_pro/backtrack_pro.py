# -*- encoding -*-

count = 0

def all_sort(strs, start, end):
    """

    :param strs:
    :param start:
    :param end:
    :return:
    """

    if start == end:
        print(" ".join(strs))
        global count
        count += 1
    else:
        for j in range(start, end+1):
            if not find_deplicate(strs, start, j):
                strs[j], strs[start] = strs[start], strs[j]
                all_sort(strs, start+1, end)
                strs[j], strs[start] = strs[start], strs[j]

def find_deplicate(strs, start, de_idx):
    flag = False
    for i in range(start, de_idx):
        if strs[i] == strs[de_idx] and start != de_idx:
            flag = True
    return flag

def all_sort_demo():
    a = ['a', 'b', 'a', 'd']
    all_sort(a, 0, len(a)-1)
    global count
    print(count)

if __name__ == '__main__':
    all_sort_demo()
