class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

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

    def add_between(self, key, data):
        temp = self.head

        while temp:
            if temp.data == key:
                new_node = Node(data)

                new_node.next = temp.next
                new_node.prev = temp

                if temp.next:
                    temp.next.prev = new_node

                temp.next = new_node
                return
            temp = temp.next
        print("Value not found")
    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")
obj = DoublyLinkedList()

while True:
    print("\n1. Add at end")
    print("2. Add in between")
    print("3. Display")
    print("4. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        data = int(input("Enter data: "))
        obj.add_end(data)

    elif ch == 2:
        key = int(input("Insert after: "))
        data = int(input("Enter new data: "))
        obj.add_between(key, data)
    elif ch == 3:
        obj.display()

    elif ch == 4:
        break