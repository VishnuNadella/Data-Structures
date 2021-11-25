class Stack():

    def __init__(self):
        self.top = -1
        self.stack_len = None
        self.stack = None

    def create(self, length):
        '''Pass size of the array'''
        self.stack_len = length
        self.stack = [0 for _ in range(self.stack_len)]

    def isfull(self):
        # print("top: ", self.top)
        if self.top == self.stack_len - 1:
            return 1
        return 0

    def isemt(self):
        if self.top == -1:
            return 1
        return 0

    def push(self):
        if self.isfull():
            print("-------------Stack is full-------------")
        else:
            self.top += 1
            # print("Top in push:", self.top)
            self.stack[self.top] = input("Enter value: ")

    def Pop(self):
        if self.isemt():
            print("-------------Stack is empty------------")
        elif self.top != -1:
            # print("top in Pop:", self.top)
            # print("-----------The element which will be poped:", self.arr[self.top])
            self.stack[self.top] = 0
            self.top -= 1
            # print("-------top after poping:", self.top)
    def Display(self):
        req = self.stack[:self.top + 1]
        print(*req)

stack = Stack()
stack_sze = int(input("Enter array length: "))

stack.create(stack_sze)
cnd = True
while cnd:
    print("1. Push\n2. Pop\n3. Display\n4. Quit")
    query = int(input("Query: "))
    if query == 1:
		#top += 1
        stack.push()

    elif query == 2:
		#top -= 1
    	print("top is:", stack.top)
    	stack.Pop()

    elif query == 3:
        stack.Display()
        # print("top is now at:", stack.top)
        # print(*stk)
    
    elif query == 4:
        print("Quitting...")
        cnd = False
    
    else:
        print("Please select valid option")

	# elif query == 3:
    #     stack.Display()
	# 	# print("top is now at:", stack.top)
	# 	# print(*stk)

	# elif query == 4:
	# 	print("Quitting...")
	# 	cnd = False