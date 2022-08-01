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
    def from_here(self, val):
        def inorder(root_custom):
            inorder(root_custom.left)
            print(inorder(root_custom.value))
            inorder(root_custom.right)
        rt = self.root
        
        req = None
        while True:
            rt_val = rt.value
            req = rt
            print(val, rt_val, req)
            if rt != None and rt_val > val:
                rt = rt.right
                #print(rt.right.value)
            elif rt != None and rt_val < val:
                rt = rt.left
            elif rt_val == val:
                req = rt
                break
        print("The following are the nodes thqat can be visited")
        inorder(req)
        #print(inorder(rt))


tree = Tree()
cnd = True
print("1.add\n2.from here\n3.Exit")
while cnd:
    query = int(input("Enter option: "))
    if query == 1:
        tree.append_tree()
    elif query == 2:
        tree.from_here(int(input("Enter value to check from: ")))
    elif query == 3:
        cnd = False
    else:
        print("Wrong Option")
