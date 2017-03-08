

import time

# bubble sort
def bubble_sort(input_list):
    # sanity check
    if len(input_list) <=1:
        return input_list
    for i in range(len(input_list)):
        for j in range(len(input_list)-i -1):
            if input_list[j] >= input_list[j+1]:
                temp = input_list[j]
                input_list[j] = input_list[j+1]
                input_list[j+1] = temp
    return input_list

# selection sort
def selection_sort(input_list):
    for i in range(len(input_list)):
        smallest_index, smallest = get_smallest(input_list[i:])
        if smallest_index == -1:
            continue
        else:
            temp = input_list[i + smallest_index]
            input_list[i + smallest_index] = input_list[i]
            input_list[i] = temp
    return input_list

def get_smallest(sub_list):
    smallest = 100
    smallest_index = -1
    for i in range(len(sub_list)):
        if sub_list[i] < smallest:
            smallest = sub_list[i]
            smallest_index = i
    return smallest_index, smallest

def get_largest(sub_list):
    largest = -1
    largest_index = -1
    for i in range(len(sub_list)):
        if sub_list[i] < largest:
            largest = sub_list[i]
            largest_index = i
    return largest_index, largest

# insertion sort
def insertion_sort(input_list):
    for i in range(len(input_list)):
        for j in range(0, i+1):
            pass

# merge sort
def merge_sort(A, p, r):
    if p < r:
        q = [(p + r) / 2]
    merge_sort(A, p, q)
    merge_sort(A, q+1, r)
    merge(A, p, q, r)

def merge(A, p, q, r):
    n1 = q-p+1
    n2 = r-q
    L = [None] * n1
    R = [None] * n2

    for i in range(n1):
        L[i] = A[p+i+1]

    for j in range(n2):
        R[i] = A[q + j]

    i = 1
    j = 1

    for k in range(p,r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        elif A[k] == R[j]:
            j = j + 1

# quick sort
def quick_sort():
    pass

def redix_sort():
    pass



input_list = [2,5,3,1,10,13,12]
start = int(round(time.time() * 1000))
print bubble_sort(input_list)
end = int(round(time.time() * 1000))
input_list = [2,5,3,1,10,13,12]
print selection_sort(input_list)
print merge_sort(input_list, )