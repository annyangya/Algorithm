import typing


def quick_sort(sort_list: typing.List, left: int, right: int):
    """快排"""
    _quick_sort_next(sort_list, left, right)


def _quick_sort_next(sort_list: typing.List, left: int, right: int):
    """先比较数据，再合并"""
    if left < right:
        mid = __partition(sort_list, left, right)
        _quick_sort_next(sort_list, left, mid)
        _quick_sort_next(sort_list, mid + 1, right)


def __partition(sort_list: typing.List, left: int, right: int):
    key = sort_list[left]  # 标记值，与key值比较大小
    # 首尾两个指针，右边的遇到比key值小时，与最左边的互换， 左边的遇到比key值大时，与最右边的互换
    while left < right:
        while left < right and sort_list[right] >= key:
            right -= 1
        sort_list[left] = sort_list[right]
        while left < right and sort_list[left] <= key:
            left += 1
        sort_list[right] = sort_list[left]
    sort_list[left] = key
    return left


if __name__ == '__main__':
    a = [-1, 3, 4, -2, 6, 3, 7, 4, 5]
    quick_sort(a, 0, len(a) - 1)
    print(a)
