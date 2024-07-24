import time

def merge_sort(data, drawrectangle, delay):
    merge_sort_helper(data, 0, len(data) - 1, drawrectangle, delay)
    drawrectangle(data, ['green' for x in range(len(data))])

def merge_sort_helper(data, left, right, drawrectangle, delay):
    if left < right:
        middle = (left + right) // 2
        merge_sort_helper(data, left, middle, drawrectangle, delay)
        merge_sort_helper(data, middle + 1, right, drawrectangle, delay)
        merge(data, left, middle, right, drawrectangle, delay)

def merge(data, left, middle, right, drawrectangle, delay):
    left_copy = data[left:middle + 1]
    right_copy = data[middle + 1:right + 1]

    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left

    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):
        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            data[sorted_index] = left_copy[left_copy_index]
            left_copy_index += 1
        else:
            data[sorted_index] = right_copy[right_copy_index]
            right_copy_index += 1
        sorted_index += 1
        drawrectangle(data, ['black' if x == sorted_index else 'red' for x in range(len(data))])
        time.sleep(delay)

    while left_copy_index < len(left_copy):
        data[sorted_index] = left_copy[left_copy_index]
        left_copy_index += 1
        sorted_index += 1
        drawrectangle(data, ['black' if x == sorted_index else 'red' for x in range(len(data))])
        time.sleep(delay)

    while right_copy_index < len(right_copy):
        data[sorted_index] = right_copy[right_copy_index]
        right_copy_index += 1
        sorted_index += 1
        drawrectangle(data, ['black' if x == sorted_index else 'red' for x in range(len(data))])
        time.sleep(delay)
