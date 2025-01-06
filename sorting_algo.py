import random


def bubble_sort(arr):
    i = 0
    j = len(arr)
    swapped = False
    while j > 1:
        while i < j - 1:
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
            i += 1
        if not swapped:
            break
        swapped = False
        j -= 1
        i = 0
    return arr

def selection_sort(arr):
    mn = arr[0]
    current_index = 0
    mn_index = 0
    while current_index < len(arr)-1:
        for i , ele in enumerate(arr[current_index:]):
            if ele < mn:
                mn = ele
                mn_index = i
        if mn_index != current_index:
            arr[current_index], arr[mn_index+current_index] =  arr[mn_index+current_index],arr[current_index]
        current_index += 1
        mn = arr[current_index]
        mn_index = current_index
    return arr

def selection_sort_2(arr):
    i = 0
    while i < len(arr):
        minimum = arr[i]
        minimum_index = i
        for j, item in enumerate(arr[i + 1:]):
            if item < minimum:
                minimum = item
                minimum_index = j + i + 1
        arr[i], arr[minimum_index] = arr[minimum_index], arr[i]
        i += 1
    return arr

def insertion_sort(arr):
    i = 0
    while i < len(arr)-1:
        i += 1
        j = i
        while j > 0:
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1],arr[j]
                j -= 1
            else:
                break
    return arr




print(bubble_sort([random.randint(0,100) for _ in range(10)]))
#print(selection_sort([random.randint(0,100) for _ in range(10)]))
print(selection_sort_2([random.randint(0,100) for _ in range(10)]))
print(insertion_sort([random.randint(0,100) for _ in range(10)]))