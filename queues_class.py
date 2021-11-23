# in middle i did enqueue a few elements(rear != size) and then i started dequeue all the enqueue elements 
# and now front reached rear but rear != size the cacn we say that the queue is empty since still we can 
# add elements

class Queue():
    def __init__(self):
        self.queue_sz = int(input("Enter queue size: "))
        self.front = -1
        self.rear = -1
        self.queue = None

    def create(self):
        self.queue = [0 for _ in range(self.queue_sz)]
        

    def isfull(self):
        print(f"rear: {self.rear} and Size {self.queue_sz}")
        if self.rear == (self.queue_sz - 1):
            return 1
        return 0

    def isemt(self):
        if self.front == (self.rear):
            return 1
        return 0

    def enqueue(self):
        if self.isfull():
            print("Queue is full")
            print("In side is full cnd:", self.queue)
        else:
            self.rear += 1
            print("Size of the queue:", self.queue_sz)
            print("Rear:", self.rear)
            self.queue[self.rear] = int(input("Enter element: "))

    def dequeue(self):
        print("Queue size:", self.queue_sz)
        print(f"front: {self.front} and rear {self.rear}")
        if self.isemt():
            print("Queue is empty")
        else:
            print(f"Before\nfront: {self.front} and rear {self.rear}")
            self.front += 1
            self.queue[self.front] = 0
            print(f"After\nfront: {self.front} and rear {self.rear}")

    def Display(self):
        req = self.queue[self.front + 1:self.rear + 1]
        print(len(req))
        print(*req)


Que = Queue()
Que.create()
#print("Created queue:", Que.Display)
cnd = True

while cnd:
    print("Menu (Enter number):\n\t1. Enqueue\n\t2. Dequeue\n\t3. Display\n\t4. Quit")
    query = int(input("Enter value: "))
    if query == 1:
        
        Que.enqueue()
        #print("Queue stats", Queue)
    elif query == 2:
        #print("Front Before:", front)
        Que.dequeue()
        
        #print("Front After:", front)
        #print("Queue stats", Queue)
    elif query == 3:
        Que.Display()
    elif query == 4:
        print("Quitting...")
        cnd = False
    else:
        print("Please enter a number that exists in the menu")