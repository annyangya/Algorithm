from typing import List


def merge_sort(sort_list: List, left: int, right: int):
    """归并排序"""
    _merge_sort_next(sort_list, left, right)


def _merge_sort_next(sort_list: List, left: int, right: int):
    """先拆分数据，由下至上，逐层合并"""
    if left < right:
        mid = (left + right) // 2
        _merge_sort_next(sort_list, left, mid)
        _merge_sort_next(sort_list, mid + 1, right)
        __merge(sort_list, left, mid, right)


def __merge(sort_list: List, left: int, mid: int, right: int):
    i, j = left, mid + 1  # i， j分别是两个数组的指针，互相比较值的大小，再逐个移动
    temp = []
    while i <= mid and j <= right:
        if sort_list[i] <= sort_list[j]:
            temp.append(sort_list[i])
            i += 1
        else:
            temp.append(sort_list[j])
            j += 1
    remain_start = i if i <= mid else j
    remain_end = mid if i <= mid else right
    temp.extend(sort_list[remain_start: remain_end + 1])
    sort_list[left: right + 1] = temp



if __name__ == '__main__':
    a = [-1, 3, 4, -2, 6, 3, 7, 4, 5]
    merge_sort(a, 0, len(a) - 1)
    print(a)