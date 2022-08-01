__author__ = "Vishnu"

class Node:
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None

    def add(self, val):
        self.value = val

class Tree:
    def __init__(self):
        self.root = None

    def append_tree(self):
        if self.root == None:
            new = Node()
            val = int(input("Enter Value: "))
            new.value = val
            self.root = new
            print(new, new.left, new.right, new.value)
        elif self.root != None:
            new = Node()
            val = int(input("Enter Value: "))
            new.add(val)
            rt = self.root
            while True:
                rt_val = rt.value
                print(rt, rt_val)
                if rt_val >= val:
                    if rt.right == None:
                        rt.right = new
                        break
                    elif rt.right != None:
                        rt = rt.right
                elif rt_val < val:
                    if rt.left == None:
                        
                        rt.left = new
                        print(rt.left)
                        break
                    elif rt.left != None:
                        rt = rt.left
    def find_ele(self, val):
        rt = self.root
        req = None
        while True:
            try:
                rt_val = rt.value
                req = rt
            except:
                print(f"Value {val} dosent exists")
                break
            print(val, rt_val, req)
            if rt != None and rt_val > val:
                rt = rt.right
            elif rt != None and rt_val < val:
                rt = rt.left
            elif rt_val == val:
                req = rt
                print("Value Exists")
                break
        # else:
        #     print("Value dosent exists")


tree = Tree()
cnd = True
print("1.Add\n2.Value Exists\n3.Exit")
while cnd:
    try:
        query = int(input("Enter option: "))
    except:
        print("No input or invalid input!")
    if query == 1:
        tree.append_tree()
    elif query == 2:
        tree.find_ele(int(input("Check if value exists: ")))
    elif query == 3:
        print("Terminating...")
        cnd = False
    else:
        print("Wrong Option")