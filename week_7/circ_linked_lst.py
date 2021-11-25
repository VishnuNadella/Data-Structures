#circular linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class circ_lnk_lst:
    def __init__(self):
        self.start = None #head         #this is static and contains the address of the root node
        self.latest_node = None #tail   #this should get updated all the time with new node address
    def create(self): #conditional statements outside the class (so as to not call create again and again)
        current_node = Node(input("Enter data: "))
        self.start = current_node #defining the starting node
        current_node.next = self.start #making this circular by pointing the node to itself
        self.latest_node = current_node         

    def insertion(self):
        current_node = Node(input("Enter data: "))
        # self.latest_node.next = current_node #this should add address of the curr node to previous node
        # current_node.next = self.start #this will make it circular
        current_node.next = self.start
        if self.start == self.latest_node:
            self.start.next = current_node
        else:
            self.latest_node.next = current_node
        self.latest_node = current_node


    def deletion(self):
        #at last
        if self.start.next == None:
            print("Nothing left to remove")
        else:
            if self.start.next == self.start:
                del self.start
            curr_node = self.start
            while curr_node.next.next != self.start:
                curr_node = curr_node.next
            #current node is the last but one node
            last_node = curr_node.next.next
            curr_node.next = self.start # link has been removed
            del last_node
            #update the latest node
            self.latest_node = curr_node
    def traversal(self):
        pass

    def Display(self):
        if self.start == None:
            print("Nothing in here")
        else:
            # terminator = self.start
            curr_node = self.start
            while curr_node.next != self.start:
                print(curr_node.data)
                curr_node = curr_node.next
            print(curr_node.data)


circ = circ_lnk_lst()
cnd = True
circ.create()
while cnd:
    print("Menu\n\t1. insert\n\t2. Display\n\t3. Delete\n\t4. Quit")
    query = int(input("Enter selected option: "))
    if query == 1:
        circ.insertion()
    elif query == 2:
        circ.Display()
    elif query == 3:
        circ.deletion()
    elif query == 4:
        print("Quitting...")
        cnd = False
    else:
        print("Select a valid option from menu")