def ins_srt(lst):
	for i in range(1, len(lst)):
		val = lst[i]
		idx = i - 1
		while idx >= 0 and lst[idx] > val:
			lst[idx + 1] = lst[idx]
			idx -= 1
		lst[idx + 1] = val
	return lst

arr = [int(i) for i in input().split()]

print("Sorted array is: ", ins_srt(arr))