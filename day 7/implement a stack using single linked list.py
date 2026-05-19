#implement a stack using singly linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.top = None

    def push(self,data):
        new_node=Node(data)
        new_node.next = self.top
        self.top =new_node
    def pop(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("Deleted:", self.top.data)
            self.top=self.top.next

    def display(self):
        temp=self.top

        if self.top is None:
            print("Stack is empty")
        else:
            while temp:
                print(temp.data)
                temp=temp.next

obj = Stack()

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        data = int(input("Enter data: "))
        obj.push(data)

    elif ch == 2:
        obj.pop()

    elif ch == 3:
        obj.display()

    elif ch == 4:
        break

    else:
        print("Invalid choice")