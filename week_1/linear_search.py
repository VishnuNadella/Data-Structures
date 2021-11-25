#linear search
req_lst = [int(i) for i in input("Enter the list elements: ").split()]
tar_num = int(input("Enter the number to be found: "))
c = 0
for i in range(len(req_lst)):
	if tar_num == req_lst[i]:
		c += 1
		break
if c == 1:
	print("Number found")
else:
	print("Number not found")