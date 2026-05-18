import sys
class GetNode:
    def __init__(self):
        self.data=None
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def append(self):
        pass
    def traverse(self):
        pass

if __name__ == '__main__':
    obj=LinkedList()
    while True:
        print("1.Append")
        print("2.Traverse")
        print("0.Exit")
        n=int(input("select any choice: "))
        if n==1:
            obj.append()
        elif n==2:
            obj.traverse()
        elif n==0:
            sys.exit(0)