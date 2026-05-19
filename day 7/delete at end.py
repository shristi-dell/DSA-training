class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add_begin(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp

    def delete_end(self):
        if self.head is None:
            print("List is empty")

        elif self.head.next is None:
            self.head = None

        else:
            temp = self.head
            while temp.next:
                temp = temp.next

            temp.prev.next = None

    def display(self):
        temp = self.head

        if self.head is None:
            print("List is empty")

        else:
            while temp:
                print(temp.data, end=" <-> ")
                temp = temp.next
            print("None")


obj = DoublyLinkedList()

while True:
    print("\n1. Add at beginning")
    print("2. Add at end")
    print("3. Delete at end")
    print("4. Display")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        data = int(input("Enter data: "))
        obj.add_begin(data)

    elif ch == 2:
        data = int(input("Enter data: "))
        obj.add_end(data)

    elif ch == 3:
        obj.delete_end()

    elif ch == 4:
        obj.display()

    elif ch == 5:
        break

    else:
        print("Invalid choice")