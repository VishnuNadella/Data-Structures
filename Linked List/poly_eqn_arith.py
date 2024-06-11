class Node:
    def __init__(self, value, expre):
        self.value = value
        self.expre = expre
        self.next = None

class polynomial:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value, expre):
        new_node = Node(value, expre)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def degree(self):
        deg = 0
        if self.head == None:
            print("---------No expression so no way to find degree---------")
        else:
            current_node = self.head
            cnt = 0
            while current_node.next != None:
                if current_node.expre > deg:
                    deg = current_node.expre
                current_node = current_node.next
                cnt += 1
            if current_node.expre > deg:
                deg = current_node.expre
        return cnt + 1

    def Display(self):
        if self.head == None:
            print("---------Nothing to be displayed---------")
        else:
            current_node = self.head
            cnt = 0
            print("Polynomial Expression is:", end = " ")
            while current_node.next != None:
                if current_node.value >= 0 and cnt != 0:
                    print(f"+{current_node.value}*x^{current_node.expre}", end = "")
                elif current_node.value >= 0 and cnt == 0:
                    print(f"{current_node.value}*x^{current_node.expre}", end = "")
                elif current_node.value < 0:
                    print(f"{current_node.value}*x^{current_node.expre}", end = "")
                current_node = current_node.next
                cnt += 1
            if current_node.value >= 0:
                print(f"+{current_node.value}*x^{current_node.expre}") # since while loop termminates and it wont print the data in last node
            else:
                print(f"{current_node.value}*x^{current_node.expre}") # since while loop termminates and it wont print the data in last node

class poly_arith():
    def __init__(self):
        self.head_1 = None
        self.head_2 = None

    # def arith(self, poly_1, n_1, poly_2, n_2, ops):
    #     if self.head_1 == None:
    #         self.head_1 = poly_1
    #     if self.head_2 == None:
    #         self.head_2 = poly_2
    #     curr_1 = self.head_1.head
    #     curr_2 = self.head_2.head
    #     curr = None
    #     cnt = 0
    #     if n_1 >= n_2:
    #         curr = curr_1
    #     elif n_1 < n_2:
    #         curr = curr_2
    #     while curr.next != None:
    #         if curr_1.value >= 0 and cnt != 0 and curr_1.expre == curr_2.expre:
    #             stri = str(eval(f"+{curr_1.value} {ops} {curr_2.value}")) + f" * x^{curr.expre} "
    #             print(stri, end = "")

    #         elif curr_1.value >= 0 and cnt == 0 and curr_1.expre == curr_2.expre:
    #             stri = str(eval(f"{curr_1.value} {ops} {curr_2.value}")) + f" * x^{curr.expre} " 
    #             print(stri, end = "")

    #         elif curr_1.value < 0 and curr_1.expre == curr_2.expre:
    #             stri = str(eval(f"{curr_1.value} {ops} {curr_2.value}")) + f" * x^{curr.expre} " 
    #             print(stri, end = "")
            
    #         cnt += 1
    #         curr_1 = curr_1.next
    #         curr_2 = curr_2.next
    #         curr = curr.next
    #     stri = str(eval(f"{curr_1.value} {ops} {curr_2.value}")) + f" * x^{curr.expre}"
    #     print(stri, end = "")
    

    def arith(self, poly_1, n_1, poly_2, n_2, ops):
        if self.head_1 == None:
            self.head_1 = poly_1
        if self.head_2 == None:
            self.head_2 = poly_2
        curr_1 = self.head_1.head
        curr_2 = self.head_2.head
        curr = None
        cnt = 0
        if n_1 >= n_2:
            curr = curr_1
            while curr.next != None:
                if curr_2 != None and curr_1.value >= 0 and cnt != 0 and curr_1.expre == curr_2.expre:
                    stri = str(eval(f"+{curr_1.value} {ops} {curr_2.value}")) + f"*x^{curr.expre} "
                    # print(stri)
                    cnt += 1
                    curr_1 = curr_1.next
                    curr_2 = curr_2.next
                    curr = curr.next
                    print(stri, end = "")
                
                elif curr_2 == None and curr_1.value >= 0 and cnt != 0:
                    stri = f"{curr_1.value}*x^{curr_1.expre} "
                    print(stri, end = "")
                    # print(stri)
                    cnt += 1
                    curr_1 = curr_1.next
                    curr = curr.next
                
                elif curr_2 != None and curr_1.value >= 0 and cnt != 0 and curr_1.expre > curr_2.expre:
                    stri = f"{curr_1.value}*x^{curr_1.expre} "
                    print(stri, end = "")
                    # print(stri)
                    cnt += 1
                    curr_1 = curr_1.next # 
                    curr = curr.next

                elif curr_1 != None and curr_2.value >= 0 and cnt != 0 and curr_1.expre < curr_2.expre:
                    stri = f"{curr_2.value}*x^{curr_2.expre} "
                    print(stri, end = "")
                    # print(stri)
                    cnt += 1
                    curr_2 = curr_2.next
                    # curr = curr.next


                elif curr_2 != None and curr_1.value >= 0 and cnt == 0 and curr_1.expre == curr_2.expre:
                    stri = str(eval(f"{curr_1.value} {ops} {curr_2.value}")) + f"*x^{curr.expre} " 
                    print(stri, end = "")
                    # print(stri)
                    cnt += 1
                    curr_1 = curr_1.next
                    curr_2 = curr_2.next
                    curr = curr.next


                elif curr_2 != None and curr_1.value >= 0 and cnt == 0 and curr_1.expre > curr_2.expre:
                    stri = f"{curr_1.value}*x^{curr_1.expre} "
                    print(stri, end = "")
                    # print(stri)
                    cnt += 1
                    curr_1 = curr_1.next
                    curr = curr.next


                elif curr_1 != None and curr_2.value >= 0 and cnt == 0 and curr_1.expre < curr_2.expre:
                    stri = f"{curr_2.value}*x^{curr_2.expre} "
                    print(stri, end = "")
                    # print(stri)
                    cnt += 1
                    curr_2 = curr_2.next

                elif curr_2 != None and curr_1.value < 0 and curr_1.expre == curr_2.expre:
                    stri = str(eval(f"{curr_1.value} {ops} {curr_2.value}")) + f"*x^{curr.expre} " 
                    print(stri, end = "")
                    # print(stri)
                    cnt += 1
                    curr_1 = curr_1.next
                    curr_2 = curr_2.next
                    curr = curr.next
            try:
                stri = str(eval(f"{curr_1.value} {ops} {curr_2.value}")) + f"*x^{curr.expre}"
                print(stri, end = "")
            except:
                if curr_1 != None:
                    stri = f"{curr_1.value}*x^{curr.expre}"
                elif curr_2 != None:
                    stri = f"{curr_2.value}*x^{curr.expre}"
                print(stri, end = "")
            
            # print(stri)

        elif n_1 < n_2:
            curr = curr_2
            while curr.next != None:
                if curr_1 != None and curr_1.value >= 0 and cnt != 0 and curr_1.expre == curr_2.expre:
                    stri = str(eval(f"+{curr_1.value} {ops} {curr_2.value}")) + f"*x^{curr.expre} "
                    # print(stri)
                    print(stri, end = "")
                    cnt += 1
                    curr_1 = curr_1.next
                    curr_2 = curr_2.next
                    curr = curr.next
                
                elif curr_1 != None and curr_1.value >= 0 and cnt != 0 and curr_1.expre > curr_2.expre:
                    stri = f"{curr_1.value}*x^{curr_1.expre} "
                    print(stri, end = "")
                    # print(stri)
                    cnt += 1
                    curr_1 = curr_1.next

                elif curr_1 == None and curr_2.value >= 0 and cnt != 0:
                    stri = f"{curr_2.value}*x^{curr_2.expre} "
                    print(stri, end = "")
                    # print(stri)
                    cnt += 1
                    curr_2 = curr_2.next
                    curr = curr.next

                elif curr_2 != None and curr_2.value >= 0 and cnt != 0 and curr_1.expre < curr_2.expre:
                    stri = f"{curr_2.value}*x^{curr_2.expre} "
                    print(stri, end = "")
                    # print(stri)
                    cnt += 1
                    curr_2 = curr_2.next
                    curr = curr.next
                

                elif curr_2 != None and curr_1.value >= 0 and cnt == 0 and curr_1.expre == curr_2.expre:
                    stri = str(eval(f"{curr_1.value} {ops} {curr_2.value}")) + f"*x^{curr.expre} " 
                    print(stri, end = "")
                    # print(stri)

                    cnt += 1
                    curr_1 = curr_1.next
                    curr_2 = curr_2.next
                    curr = curr.next
                
                elif curr_1 != None and curr_1.value >= 0 and cnt == 0 and curr_1.expre > curr_2.expre:
                    stri = f"{curr_1.value}*x^{curr_1.expre} "
                    print(stri, end = "")
                    # print(stri)
                    cnt += 1
                    curr_1 = curr_1.next

                elif curr_2 != None and curr_2.value >= 0 and cnt == 0 and curr_1.expre < curr_2.expre:
                    stri = f"{curr_2.value}*x^{curr_2.expre} "
                    print(stri, end = "")
                    # print(stri)
                    cnt += 1
                    curr_2 = curr_2.next
                    curr = curr.next

                elif curr_1 != None and curr_1.value < 0 and curr_1.expre == curr_2.expre:
                    stri = str(eval(f"{curr_1.value} {ops} {curr_2.value}")) + f"*x^{curr.expre} " 
                    print(stri, end = "")
                    # print(stri)
                    cnt += 1
                    curr_1 = curr_1.next
                    curr_2 = curr_2.next
                    curr = curr.next
                
                
            try:
                stri = str(eval(f"{curr_1.value} {ops} {curr_2.value}")) + f"*x^{curr.expre}"
                print(stri, end = "")
            except:
                if curr_1 != None:
                    stri = f"{curr_1.value}*x^{curr.expre}"
                elif curr_2 != None:
                    stri = f"{curr_2.value}*x^{curr.expre}"
                print(stri, end = "")
            # print(stri)


        

poly_exp_1 = polynomial()
poly_exp_2 = polynomial()
ops = None
cnd = True

print("Enter your polynomial expression:")

while cnd:
    print("Menu (enter number):\n\tEnter [1] to build 1st expression\n\tEnter [2] to build 2nd expression\n\tEnter [0] to stop building the expression")
    query = int(input("\nEnter your option: "))
    if query == 1:
        val = int(input("Enter Value: "))
        powe = int(input("Enter Power: "))
        poly_exp_1.push(val, powe)
    elif query == 2:
        val = int(input("Enter Value: "))
        powe = int(input("Enter Power: "))
        poly_exp_2.push(val, powe)
    elif query == 0:
        print("Your Polynomial Expressions has been stored Successfully")
        ops_query = input("What kind of Arithmetic operation do you want to perform (+, -, *, /)").strip()
        if ops_query == "+" or ops_query == "-" or ops_query == "*" or ops_query == "/":
            ops = ops_query
            cnd = False
        else:
            print("Please enter valid operation (+, -, *, /)")

    else:
        print("Enter a valid char from menu!!")

eps_1 = poly_exp_1.degree()
eps_2 = poly_exp_2.degree()
poly_exp = poly_arith().arith(poly_exp_1, eps_1, poly_exp_2, eps_2, ops)
# poly_exp.Display()