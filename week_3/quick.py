def partition(left, right, arr):
    pivot_index = left
    p = a[pivot_index]
    while(left < right):
        while(left < len(arr) and a[left] <= p):
            left += 1
        while(a[right] > p):
            right-= 1
        if(left < right):
            a[left], a[right] = a[right], a[left]
    a[right], a[pivot_index]= a[pivot_index], a[right]
    return right


def quick_sort(left, right, arr):
    if(left< right):
        d = partition(left, right, arr)
        quick_sort(left, d - 1, arr)
        quick_sort(d + 1, right, arr)


a = [int(i) for i in input().split()]
quick_sort(0, len(a) - 1, a)
print('Quick sort:', *a)
