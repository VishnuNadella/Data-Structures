#raw working model


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class SLinkedLst:
    def __init__(self):
        self.head  = None
        # self.count = 0

    
    def push_end(self, data):
        print("HEad:", self.head)
        new_node = Node(data)
        if self.head == None:
            print("HEad:", self.head)
            self.head = new_node
            print("HEad:", self.head)
            # self.count += 1
        else:
            print("head node data:", self.head.data)
            print("head node next:", self.head.next)
            temp = self.head #head node address
            while temp.next != None:
                temp = temp.next #next node address will be allcoated to temp
            # self.count += 1    
            temp.next = new_node #the non will now get allocated with rear object address
            print("last node:", temp.next)
            print("Count:", self.count)

    def push_front(self, data): #not required pop_front is required
        new_node = Node(data)
        new_node.next = self.head #link b\w nodes has been established
        self.head = new_node #head node allocation has been completed
        self.count += 1


    # def Pop(self):
    #     if self.head == None:
    #         print("Nothing left to remove")
    #     else:
    #         current_node = self.head
    #         lat_bt_1_nd = None
    #         while current_node.next != None:
    #             lat_bt_1_nd = current_node
    #             current_node = current_node.next
    #         # del temp.next #here the code is broken
    #         print("Current node:", current_node)
    #         print("last but one node:", lat_bt_1_nd)
    #         # del current_node
    #         if self.count > 1:
    #             del current_node
    #             self.count -= 1
    #             lat_bt_1_nd.next = None
    #         elif self.count == 1:#not working
    #             self.head = None
    #             self.count -= 1
    #         # print("Head:", current_node) #causing called before reference error
    #         print("Self. head status:", self.head)
    
    def POP(self): #efficient pop
        if self.head == None:
            print("Nothing left to remove")
        else:
            if self.head.next == None:
                del self.head
                # print(self.head)
                self.head = None
            else:
                current_node = self.head
                while current_node.next.next != None:
                    current_node = current_node.next
                del current_node.next
                current_node.next = None
                

    def Display(self):
        if self.head == None:
            print("Nothing to be displayed")
        else:
            print("Count is:", self.count)
            temp = self.head
            print("Elements are:", end = " ")
            while temp.next != None:
                print(temp.data, end = " ")
                temp = temp.next
            print(temp.data) #since while loop termminates and it wont print the data in last node
                

lnk_lst = SLinkedLst()
cnd = True

while cnd:
    print("Menu\n1. Push back\n2. Push front\n3. Pop\n4. Display\n5. Quit\n6. POP")
    query = int(input("Enter selected option: "))
    if query == 1:
        lnk_lst.push_end(int(input("Enter data: ")))
    elif query == 2:
        lnk_lst.push_front(int(input("Enter data: ")))
    elif query == 3:
        lnk_lst.Pop()
    elif query == 4:
        lnk_lst.Display()
    elif query == 5:
        print("Quitting...")
        cnd = False
    elif query == 6:
        lnk_lst.POP()
    else:
        print("Select a valid option from menu")