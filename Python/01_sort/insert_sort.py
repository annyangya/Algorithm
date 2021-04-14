from typing import List


def insert_sort(sort_list: List):
    size = len(sort_list)
    for i in range(1, size):
        for j in range(i, 0, -1):
            if sort_list[j - 1] > sort_list[j]:
                sort_list[j - 1], sort_list[j] = sort_list[j], sort_list[j - 1]
    return sort_list


if __name__ == '__main__':
    a = [-1, 3, 4, -2, 6, 3, 7, 4, 5]
    insert_sort(a)
    print(a)