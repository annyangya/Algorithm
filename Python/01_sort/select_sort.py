from typing import List


def select_sort(sort_list: List):
    size = len(sort_list)
    for i in range(size):
        min = i
        for j in range(i, size):
            if sort_list[j] < sort_list[i]:
                min = j
        sort_list[i],  sort_list[min] = sort_list[min], sort_list[i]
    return sort_list


if __name__ == '__main__':
    a = [-1, 3, 4, -2, 6, 3, 7, 4, 5]
    select_sort(a)
    print(a)