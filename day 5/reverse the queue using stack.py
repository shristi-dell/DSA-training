# Reverse the queue using stack

import sys

class Queue:
    def __init__(self, capacity=5):
        self.queue = []
        self.rear = -1
        self.front = 0
        self.capacity = capacity

    def isFull(self):
        return self.rear == self.capacity - 1

    def isEmpty(self):
        return self.front > self.rear

    def insert(self, ele):
        if self.isFull():
            print("Queue Overflow")
        else:
            self.queue.append(ele)
            self.rear += 1
            print(f"{ele} inserted into queue")

    def delete(self):
        if self.isEmpty():
            print("Queue Underflow")
            return None
        else:
            ele = self.queue[self.front]
            self.front += 1
            print(f"Deleted element: {ele}")
            return ele

    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        else:
            print(f"Front element: {self.queue[self.front]}")
            return self.queue[self.front]

    def traverse(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            print("Queue elements:", end=" ")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()


class Stack:
    def __init__(self, size):
        self.stack = []
        self.top = -1
        self.capacity = size

    def isFull(self):
        return self.top == self.capacity - 1

    def isEmpty(self):
        return self.top == -1

    def push(self, ele):
        if self.isFull():
            print("Stack Overflow")
        else:
            self.stack.append(ele)
            self.top += 1

    def pop(self):
        if self.isEmpty():
            print("Stack Underflow")
            return None
        else:
            ele = self.stack.pop()
            self.top -= 1
            return ele

    def peek(self):
        if self.isEmpty():
            print("Stack is Empty")
            return None
        else:
            return self.stack[self.top]


if __name__ == '__main__':

    queue_capacity = int(input("Enter queue capacity: "))

    obj1 = Queue(queue_capacity)
    obj2 = Stack(queue_capacity)

    for i in range(queue_capacity):
        ele = int(input("Enter element: "))
        obj1.insert(ele)

    print("\nOriginal Queue:")
    obj1.traverse()

    for i in range(queue_capacity):
        ele = obj1.delete()
        if ele is not None:
            obj2.push(ele)

    for i in range(queue_capacity):
        ele = obj2.pop()
        if ele is not None:
            obj1.insert(ele)

    print("\nReversed Queue:")
    obj1.traverse()

    while True:
        print("\n--- Queue Operations ---")
        print("1. Insert")
        print("2. Delete")
        print("3. Peek")
        print("4. Traverse")
        print("0. Exit")

        current_size = obj1.rear - obj1.front + 1
        if current_size < 0:
            current_size = 0

        print(f"Current queue size: {current_size}/{obj1.capacity}")

        try:
            ch = int(input("Select any choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if ch == 1:
            try:
                element = int(input("Enter element to insert: "))
                obj1.insert(element)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif ch == 2:
            obj1.delete()

        elif ch == 3:
            obj1.peek()

        elif ch == 4:
            obj1.traverse()

        elif ch == 0:
            print("Exiting...")
            sys.exit()

        else:
            print("Invalid Choice")