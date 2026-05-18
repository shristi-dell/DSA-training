## Add at between
import sys

class GetNode:
    def __init__(self):
        self.data = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self):
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

        print(data, "is added")

    def add_begin(self):
        data = int(input("Enter the no: "))
        newnode = GetNode()
        newnode.data = data

        if self.head is None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode

        print(data, "is added at begin")

    def add_between(self):
        data = int(input("Enter the no: "))
        key = int(input("Enter data after inserted: "))

        newnode = GetNode()
        newnode.data = data

        if self.head is None:
            self.head = newnode

        else:
            ptr = self.head

            while ptr is not None:

                if ptr.data == key:
                    newnode.next = ptr.next
                    ptr.next = newnode
                    print(data, "is added")
                    return

                ptr = ptr.next

            print("Key not found")

    def traverse(self):
        if self.head is None:
            print("Linked List not present")
        else:
            ptr = self.head
            while ptr is not None:
                print(ptr.data, "->", end=" ")
                ptr = ptr.next
            print("None")


if __name__ == '__main__':
    obj = LinkedList()

    while True:
        print("\n1). Append")
        print("2). Traverse")
        print("3). Add at Begin")
        print("4). Add at Between")
        print("5). Exit")

        n = int(input("select any choice: "))

        if n == 1:
            obj.append()

        elif n == 2:
            obj.traverse()

        elif n == 3:
            obj.add_begin()

        elif n == 4:
            obj.add_between()

        elif n == 5:
            sys.exit(0)

        else:
            print("Invalid choice")