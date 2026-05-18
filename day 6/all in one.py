class Getnode:
    def __init__(self):
        self.data = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self):
        data = int(input("Enter the data: "))

        node = Getnode()
        node.data = data
        node.next = None

        if self.head is None:
            self.head = node
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = node

        print("Data added =", data)


    def traverse(self):
        if self.head is None:
            print("List is empty")
        else:
            ptr = self.head
            while ptr is not None:
                print(ptr.data, "->", end=" ")
                ptr = ptr.next
            print("None")


    def addBegin(self):
        data = int(input("Enter data: "))

        node = Getnode()
        node.data = data
        node.next = self.head
        self.head = node

        print("Data added at beginning =", data)


    def atBitween(self):
        if self.head is None:
            print("List is empty")
            
        data = int(input("Enter data: "))
        key = int(input("Enter key: "))

        ptr = self.head

        while ptr is not None:
            if ptr.data == key:
                break
            ptr = ptr.next

        if ptr is None:
            print("Key not found")
        else:    
          node = Getnode()
          node.data = data
          ptr1 = ptr.next
          node.next = ptr1
          ptr.next = node

          print("Data added at between =", data)


    def deleteAtBegin(self):
        if self.head is None:
            print("List is empty")

        else:
            ptr = self.head
            ptr1 = ptr.next
            ptr.next = None
            head = ptr1
            print("Data deleted at beginning")


    def delete(self):
      pass


if __name__ == '__main__':
    obj = LinkedList()

    while True:
        print("\n1. Append")
        print("2. Traverse")
        print("3. Add at Beginning")
        print("4. Add at Random Location")
        print("5. Delete at beginning")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            obj.append()

        elif choice == 2:
            obj.traverse()

        elif choice == 3:
            obj.addBegin()

        elif choice == 4:
            obj.atBitween()

        elif choice == 5:
          obj.deleteAtBegin()

        elif choice == 6:
            break