# append() ->           insert()
# deleteAtBegin()->     delete()
# traverse()->
# ---------------------
# peekfront()-> front.data
# peekrear()-> rear.data
# front=head
# rear=newNode

import sys

class GetNode:
    def __init__(self):
        self.data = None
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    # Insert (Enqueue)
    def insert(self):
        data = int(input("Enter the no: "))
        newnode = GetNode()
        newnode.data = data

        if self.head is None:
            self.head = newnode
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = newnode

        print(data, "is inserted")

    # Delete (Dequeue)
    def delete(self):
        if self.head is None:
            print("Queue is empty")
        else:
            ptr = self.head
            self.head = ptr.next
            print(ptr.data, "is deleted")

    # Traverse
    def traverse(self):
        if self.head is None:
            print("Queue is empty")
        else:
            ptr = self.head
            while ptr is not None:
                print(ptr.data, "->", end=" ")
                ptr = ptr.next
            print("None")

if __name__ == '__main__':
    obj = LinkedList()
    while True:
        print("\n1). Insert")
        print("2). Delete")
        print("3). Traverse")
        print("4). Exit")

        n = int(input("Select any choice: "))

        if n == 1:
            obj.insert()

        elif n == 2:
            obj.delete()

        elif n == 3:
            obj.traverse()

        elif n == 4:
            sys.exit(0)

        else:
            print("Invalid choice")