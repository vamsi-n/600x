__author__ = 'vnellore'


def merge(left, right):

    i = 0
    j = 0
    result = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def merge_sort(list_to_sort):

    if len(list_to_sort) < 2:
        return list_to_sort

    middle = len(list_to_sort) / 2

    left = merge_sort(list_to_sort[0:middle])
    right = merge_sort(list_to_sort[middle:])

    return merge(left, right)


print merge_sort([9, 1, 5, 2, 7, 4, 3, -1])
