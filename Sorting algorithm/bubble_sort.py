#bubble sort
def swap(tgt, src):
	temp = tgt
	tgt = src
	src = temp
	return tgt, src

def bbl_srt(lst):
	for i in range(len(lst)):
		for j in range(i + 1, len(lst)):
			if lst[i] > lst[j]:
				lst[i], lst[j] = swap(lst[i], lst[j])
	return lst

arr = [int(i) for i in input("Enter list elements: ").split()]
print("Sorted array is: ", bbl_srt(arr))