# linked List 

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
      while ptr.next != None:
        ptr = ptr.next
      ptr.next = node
      print("Data added = ", data)


  def traverse(self):
    if self.head == None:
      print("List is empty")
    
    else:
      ptr = self.head
      while ptr != None:
        print(ptr.data, "-> ", end = "")
        ptr = ptr.next


  def addBegin(self):
    if self.head is None:
      print("List is empty")

    else:
      ptr = self.head
      data = int(input("Enter data"))
      node = Getnode()
      node.data = data
      node.next = ptr
      self.head = node
      print("Data added at beginning = ", data)   




  def delete(self):
    pass

if __name__ == '__main__':
  obj = LinkedList()

  while True:
    print("\n1 for append")
    print("2 for traverse")
    print("3 Add at begin")
    print("4 for delete")
    print("5 for exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
      obj.append()

    if choice == 2:
      obj.traverse()

    if choice == 3:
      obj.addBegin()

    if choice == 5:
      break