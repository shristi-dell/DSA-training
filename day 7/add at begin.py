# add at beginning
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

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")
obj = DoublyLinkedList()

while True:
    print("\n1. Add at beginning")
    print("2. Append")
    print("3. Display")
    print("4. Exit")

    ch = int(input("Enter choice: "))
    if ch == 1:
        value = int(input("Enter data: "))
        obj.add_begin(value)

    elif ch == 2:
        value = int(input("Enter data: "))
        obj.append(value)

    elif ch == 3:
        obj.display()
    elif ch == 4:
        break