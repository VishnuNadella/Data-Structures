class Queue():
    def __init__(self):
        self.queue_sz = int(input("Enter queue size: "))
        self.front = -1
        self.rear = -1
        self.queue = None

    def create(self):
        '''Create a Queue of specified Length'''
        self.queue = [0 for _ in range(self.queue_sz)]
        

    def isfull(self):
        if self.rear == (self.queue_sz - 1):
            return 1
        return 0

    def isemt(self):
        if self.front == (self.rear):
            return 1
        return 0

    def enqueue(self):
        '''Addition of elements into the queue which is also known as Enqueue'''
        if self.isfull():
            print("-------------Queue is full-------------")
        else:
            self.rear += 1
            self.queue[self.rear] = int(input("Enter element: "))

    def dequeue(self):
        '''Deletion of elements from  the queue which is also known as Dequeue'''
        if self.isemt():
            print("-------------Queue is empty-------------")
        else:
            self.front += 1
            self.queue[self.front] = 0

    def Display(self): #this code is just for displaying the queue elements
        '''Intelligent display function to echo elements inside the queue if any exists'''
        req = self.queue[self.front + 1:self.rear + 1]
        if len(req) != 0:
            print(*req)
        elif len(req) == 0:
            if self.rear == self.queue_sz - 1:
                print("-------------Queue is empty-------------")
            else:
                print("-------------Enqueue elements in queue-------------")


Que = Queue()
Que.create()
cnd = True

while cnd:
    print("Menu (Enter number):\n\t1. Enqueue\n\t2. Dequeue\n\t3. Display\n\t4. Quit")
    query = int(input("Enter value: "))
    if query == 1:
        Que.enqueue()
    elif query == 2:
        Que.dequeue()
    elif query == 3:
        Que.Display()
    elif query == 4:
        print("Quitting...")
        cnd = False
    else:
        print("Please enter a number that exists in the menu")