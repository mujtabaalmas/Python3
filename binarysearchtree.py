#practicing BST recursive

class BinarySearchTreeNode():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements+= self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
           elements += self.right.in_order_traversal()
        return elements
    
    def find_min(self):
        if self.left:
            return self.left.find_min()
        return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        return self.data

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements
        
    def search(self, val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
        
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.right

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)
            # min_val = self.right.find_min()
            # self.data = min_val
            # self.right = self.right.delete(min_val)

        return self

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root

detaa = [17, 4, 1, 20, 9, 23, 18, 34]
if len(detaa) == 0:
    print("BST is empty !!!")
else:
    buildthetree =  build_tree(detaa)
    try:
        print("In Order Traverversal: ",buildthetree.in_order_traversal())
        print("Pre Order Traverversal: ",buildthetree.pre_order_traversal())
        print("Post Order Traverversal: ",buildthetree.post_order_traversal())
        print("Min in BST: ",buildthetree.find_min())
        print("Max in BST: ",buildthetree.find_max())
        #number= int(input("Enter Number to search BST: "))
        number = 23     
        print(f"Number {number} present in BST:",buildthetree.search(number))
        print(f"Deleting number {number}")
        buildthetree.delete(number)
        print(f"After Deleting: ",buildthetree.in_order_traversal())
        print(f"Number {number} present in BST:",buildthetree.search(number))

    except IndexError or NameError as error:
        print("Erroor: ",error)