import sys
class GetNode:
    def __init__(self):
        self.data=None
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def append(self):
        data=int(input("enter data"))
        newNode=GetNode()
        newNode.data=data
        if self.head==None:
            self.hesd=newNode
        else:
            ptr=self.head
            while ptr.next!=None:
                ptr=ptr.next
            ptr.next=newNode
            print(data,"is added")
    def traverse(self):
        if self.head==None:
            print("linked list not present")
        else:
            ptr=self.head
            while ptr!=None:
                print(ptr.data," ->",end="")
                ptr=ptr.next


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