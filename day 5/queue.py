# Queue

import sys
class queue:
  def __init__(self, capacity=5):
    self.queue = []
    self.rear = -1
    self.front = 0
    self.capacity = capacity

  def isFull(self):
    if self.rear == self.capacity - 1:
      return True
    else:
      return False

  def insert(self, ele):
      if self.isFull():
          print("Queue Overflow")
      else:
          self.queue.append(ele)
          self.rear += 1
          print(f"{ele} inserted into queue")


  def peek(self):
    if self.isEmpty():
        print("Queue is empty, no element to peek.")
        return None
    else:
        print(f"Top element: {self.queue[self.front]}")
        return self.queue[self.front]

  def delete(self):
      if self.isEmpty():
          print("Queue Underflow")
      else:
          ele = self.queue[self.front]
          self.front += 1
          print(f"Deleted element: {ele}")
          return ele

  def traverse(self):
      if self.isEmpty():
          print("Queue is Empty")
      else:
          print("Queue elements:", end=" ")
          for i in range(self.front, self.rear + 1):
              print(self.queue[i], end=" ")
          print()

  def isEmpty(self):
    if self.front > self.rear:
      return True
    else:
      return False

if __name__ == '__main__':
    Queue_capacity = int(input("Enter queue capacity: "))
    obj = queue(Queue_capacity)

    while True:
        print("\n--- Queue Operations ---")
        print("1. Insert")
        print("2. Delete")
        print("3. Peek")
        print("4. Traverse")
        print("0. Exit")

        current_size = obj.rear - obj.front + 1
        if current_size < 0:
            current_size = 0
        print(f"Current queue size: {current_size}/{obj.capacity}")

        try:
            ch = int(input("Select any choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if ch == 1:
            try:
                element = int(input("Enter element to insert: "))
                obj.insert(element)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif ch == 2:
            obj.delete()

        elif ch == 3:
            obj.peek()

        elif ch == 4:
            obj.traverse()

        elif ch == 0:
            print("Exiting...")
            sys.exit()

        else:
            print("Invalid Choice")