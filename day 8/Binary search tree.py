# import sys
# class BinarySearchTree:
#     def insert(self):
#         pass
#     def preorder(self):
#         pass
#     def postorder(self):
#         pass
#     def inorder(self):
#         pass
# if __name__ == '__main__':
#     root = BinarySearchTree()
#     while True:
#         print("1. insert")
#         print("2. preorder")
#         print("3. postorder")
#         print("4. inorder")
#         print("5. exit")
#         n = int(input("select any choice: "))
#         if n == 1:
#             root.insert()
#         elif n == 2:
#             root.preorder()
#         elif n == 3:
#             root.postorder()
#         elif n == 4:
#             root.inorder()
#         elif n == 5:
#             sys.exit()
#         else:
#             print("invalid choice")




import sys
class BST:
    def __init__(self,key=None):
        self.left=None
        self.data=key
        self.rightchild=None
    def insert(self,key):
        if self.data==None:
            self.data=key
            return
        elif self.data==key:
            return
        else:
            if key<self.data:
                if self.leftchild:
                    self.leftchild.insert(key)
                else:
                    self.leftchild=BST(key)
            elif key>self.data:
                if self.rightchild:
                    self.rightchild.insert(key)
                else:
                    self.rightchild=BST(key)
        
    def preorder(self):
        print(self.data,end=" -> ")
        if self.leftchild:
            self.leftchild.preorder()
        if self.rightchild:
            self.rightchild.preorder()  
    def postorder(self):
        pass
    def inorder(self):
        pass
if __name__ == '__main__':
    root=BST()
    print("1. Insert")
    print("2. Preorder")
    print("3. Postorder")
    print("4. Inorder")
    print("0. Exit")
    n=int(input("Select any choice: "))
    if n==1:
        # data=int(input("Enter data: "))
        # root.insert()
        arr=[36,26,46,21,31,11,24,41,56,51,66]
        for i in range(len(arr)):
            root.insert(arr[i])
    elif n==2:
        root.preorder()
    elif n==3:
        root.postorder()
    elif n==4:
        root.inorder()
    elif n==0:
        sys.exit(0)
    else:
        print("Invalid Choice")