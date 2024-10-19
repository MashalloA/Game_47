def bubble_sort(sorting):
    n = len(sorting)
    for i in range(n):
        for j in range(0, n-i-1):
            if sorting[j] > sorting[j+1]:
                sorting[j], sorting[j+1] = sorting[j+1], sorting[j]
    return sorting


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return f"Element {target} found at index {mid}"
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return f"Element {target} not found"



unsorted_list = [5, 2, 9, 1, 5, 6]
sorted_list = bubble_sort(unsorted_list)
print(sorted_list)

sorted_list = [1, 2, 5, 5, 6, 9]
print(binary_search(sorted_list, 6))
