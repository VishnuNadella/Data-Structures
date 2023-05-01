#binary search


def binary_search(lst, min_idx, max_idx, fnd):
	while min_idx <= max_idx:
		mid = max_idx // 2
		if lst[mid] == fnd:
			return mid
		elif lst[mid] > fnd:
			max_idx = mid - 1
		else:
			min_idx = mid + 1
	return -1

lst = [int(i) for i in input("Enter list elements: ").split()]
seh = int(input("Enter a number to search: "))
rt = binary_search(lst, 0, len(lst) - 1, seh)
if rt != -1:
	print("Element has been found")
else:
	print("Element has not been found")
