class Graphs:

    def __init__(self):
      self.nodes=[]
      self.graph=[]
      self.nodeCount=0

    def addNode(self,v):
      if v in self.nodes:
        print(v,"is already present in graph")
      else:
        self.nodeCount+=1
        self.nodes.append(v)

        for x in self.graph:
          x.append(0)

        temp=[]
        for x in range(self.nodeCount):
          temp.append(0)

        self.graph.append(temp)
        print(v,"is added")

    def addEdge_Undirected(self):
        pass

    def addEdge_Undirected_Weighted(self):
        pass

    def addEdge_Directed_Weighted(self):
        pass

    def printgraph(self):
      print("   ",end="")
      for node in self.nodes:
        print(node,end=" ")
      print()

      for i in range(self.nodeCount):
        print(self.nodes[i],end="  ")
        for j in range(self.nodeCount):
          print(self.graph[i][j],end=" ")
        print()

    def deletegraph(self):
      pass
if __name__ == "__main__":
    obj = Graphs()
    while True:

        print("1. (Insertion) add a node using adjacency matrix representation")
        print("2. (Insertion) add a edge using adjacency matrix representation")
        print("3. (Insertion) add a edge undirected weighted graph")
        print("4. (Insertion) add a edge directed weighted graph")
        print("5. Print Graph")
        print("6. Delete Operation")
        print("0. Exit\n")

        n = int(input("Enter any choice: "))

        if n == 1:
            v=input("Enter node: ")
            obj.addNode(v)

        elif n == 2:
            obj.addEdge_Undirected()
        elif n == 3:
            obj.addEdge_Undirected_Weighted()
        elif n == 4:
            obj.addEdge_Directed_Weighted()
        elif n == 5:
            obj.printgraph()
        elif n == 6:
            pass
        elif n == 0:
            print("Exit")
            break

        else:
            print("Invalid Choice")