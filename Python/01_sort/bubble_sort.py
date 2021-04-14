from typing import List


def bubble_sort(sort_list: List):
    """冒泡排序"""
    size = len(sort_list)
    for i in range(size - 1):
        for j in range(i, size - 1):
            if sort_list[j] > sort_list[j + 1]:
                sort_list[j], sort_list[j + 1] = sort_list[j + 1], sort_list[j]
    return sort_list


def bubble_sort_yh(sort_list: List):
    """优化后的冒泡排序， 数据有序时不交换数据，直接退出循环"""
    size = len(sort_list)
    for i in range(size - 1):
        is_swap = False
        for j in range(i, size - 1):
            if sort_list[j] > sort_list[j + 1]:
                sort_list[j], sort_list[j + 1] = sort_list[j + 1], sort_list[j]
                is_swap = True
        if not is_swap:
            break
    return sort_list


if __name__ == '__main__':
    a = [-1, 3, 4, -2, 6, 3, 7, 4, 5]
    bubble_sort(a)
    print(a)
    b = [-1, 3, 4, -2, 6, 3, 7, 4, 5]
    bubble_sort_yh(b)
    print(b)