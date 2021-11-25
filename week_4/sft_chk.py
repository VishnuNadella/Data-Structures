class Stack():

    def __init__(self):
        self.top = -1
        self.stack_len = None
        self.stack = None

    def create(self, length):
        '''Pass size of the stack'''
        self.stack_len = length
        self.stack = [0 for _ in range(self.stack_len)]
        

    def isfull(self):
        '''Check whether the stack is full or not'''
        if self.top == self.stack_len - 1:
            return 1
        return 0

    def isemt(self):
        '''Check whether the stack is empty or not'''
        if self.top == -1:
            return 1
        return 0

    def push(self):
        '''Pushing or insertting of elements to the stack'''
        if self.isfull():
            print("-------------Stack is full-------------")
        else:
            self.top += 1
            self.stack[self.top] = input("Enter value: ")


    def Pop(self):
        '''Popping elements from the stack at last'''
        if self.isemt():
            print("-------------Stack is empty-------------")
        elif self.top != -1:
            self.stack[self.top] = 0
            self.top -= 1
            

    def Display(self):
        '''Display the stack'''
        if self.top == -1:
            print("-------------This is an empty stack-------------")
        else:
            req = self.stack[:self.top + 1]
            print("Your stack:", *req) #the below code belongs to stack

#implementation of stack
stack = Stack()#This also belongs to stack
stack_sze = int(input("Enter stack length: "))

stack.create(stack_sze)
cnd = True
while cnd:
    print("Menu (Enter Number):\n\t1. Push\n\t2. Pop\n\t3. Display\n\t4. Quit")
    query = int(input("Query: "))
    if query == 1:
    	stack.push()

    elif query == 2:
    	stack.Pop()

    elif query == 3:
        stack.Display()
    
    elif query == 4:
        print("Quitting...")
        cnd = False
    
    else:
        print("Please select valid option")