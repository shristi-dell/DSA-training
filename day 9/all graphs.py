# class Graphs:

#     def __init__(self):
#       self.nodes=[]
#       self.graph=[]
#       self.nodeCount=0

#     def addNode(self,v):
#       if v in self.nodes:
#         print(v,"is already present in graph")
#       else:
#         self.nodeCount+=1
#         self.nodes.append(v)

#         for x in self.graph:
#           x.append(0)

#         temp=[]
#         for x in range(self.nodeCount):
#           temp.append(0)

#         self.graph.append(temp)
#         print(v,"is added")

#     def addEdge_Undirected(self):

#         v1=input("Enter first node: ")
#         v2=input("Enter second node: ")
#         if v1 not in self.nodes:
#           print(v1,"is not present in graph")
#           return
#         if v2 not in self.nodes:
#           print(v2,"is not present in graph")
#           return
#         index1=self.nodes.index(v1)
#         index2=self.nodes.index(v2)
#         self.graph[index1][index2]=1
#         self.graph[index2][index1]=1

#     def addEdge_Undirected_Weighted(self):
#         v1=input("Enter first node: ")
#         v2=input("Enter second node: ")
#         w=int(input("Enter weight: "))

#         if v1 not in self.nodes:
#           print(v1,"is not present in graph")
#           return

#         if v2 not in self.nodes:
#           print(v2,"is not present in graph")
#           return
#         index1=self.nodes.index(v1)
#         index2=self.nodes.index(v2)

#         self.graph[index1][index2]=1
#         self.graph[index2][index1]=1

#     def addEdge_Directed_Weighted(self):
#         v1=input("Enter source node: ")
#         v2=input("Enter destination node: ")
#         w=int(input("Enter weight: "))

#         if v1 not in self.nodes:
#           print(v1,"is not present in graph")
#           return

#         if v2 not in self.nodes:
#           print(v2,"is not present in graph")
#           return
#         index1=self.nodes.index(v1)
#         index2=self.nodes.index(v2)

#         self.graph[index1][index2]=w

#     def printgraph(self):

#       print("   ",end="")
#       for node in self.nodes:
#         print(node,end=" ")
#       print()
#       for i in range(self.nodeCount):
#         print(self.nodes[i],end="  ")
#         for j in range(self.nodeCount):
#           print(self.graph[i][j],end=" ")
#         print()

#     def deletegraph(self):

#       self.nodes=[]
#       self.graph=[]
#       self.nodeCount=0

#       print("Graph Deleted")

# if __name__ == "__main__":

#     obj = Graphs()

#     while True:

#         print("1. (Insertion) add a node using adjacency matrix representation")
#         print("2. (Insertion) add a edge using adjacency matrix representation")
#         print("3. (Insertion) add a edge undirected weighted graph")
#         print("4. (Insertion) add a edge directed weighted graph")
#         print("5. Print Graph")
#         print("6. Delete Operation")
#         print("0. Exit\n")

#         n = int(input("Enter any choice: "))
#         if n == 1:
#             v=input("Enter node: ")
#             obj.addNode(v)
#         elif n == 2:
#             obj.addEdge_Undirected()
#         elif n == 3:
#             obj.addEdge_Undirected_Weighted()
#         elif n == 4:
#             obj.addEdge_Directed_Weighted()
#         elif n == 5:
#             obj.printgraph()
#         elif n == 6:
#             obj.deletegraph()
#         elif n == 0:
#             print("Exit")
#             break
#         else:
#             print("Invalid Choice")




#GRAPH
import sys
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

    def addEdge_Undirected_unweighted(self, v1,v2):
        if v1 not in self.nodes:
            print(v1, "not present")
            return
        if v2 not in self.nodes:
            print(v2, "not present")
            return
        index1=self.nodes.index(v1)
        index2=self.nodes.index(v2)
        self.graph[index1][index2]=1
        self.graph[index2][index1]=1
            

    def addEdge_Undirected_Weighted(self, v1, v2, weight):
        if v1 not in self.nodes:
            return
        if  v2 not in self.nodes:
            print(v2, "not present")
            return 
        index1=self.nodes.index(v1)
        index2=self.nodes.index(v2)
        
        self.graph[index1][index2]= weight
        self.graph[index2][index1]= weight
        

    def addEdge_Directed_Weighted(self, v1,v2, weight ):
        if v1 not in self.nodes:
            print(v1, "not present")
            return
        if v2 not in self.nodes:
            print(v2, "not present ")
            return
        
        index1=self.nodes.index(v1)
        index2=self.nodes.index(v2)
        
        self.graph[index1][index2]= weight
        self.graph[index2][index1]= weight

    

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
       if v not in self.nodes:
           print(v, "not present") 
       else:
           nodeCount-=1
           index1=self.nodes.index(v)
           self.nodes.pop(index1)
           self.graph.pop(index1)
           for x in self.graph:
               x.pop(index1)
           print(v, "is deleted")    
               
      


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
           v1 = input("Enter vertex 1 = ")
           v2 = input("Enter vertex 2 = ")
           weight=input("enter vertex = ")
           obj.addEdge_Undirected_unweighted(v1,v2, weight)

        elif n == 3:
           v1 = input("Enter vertex 1 = ")
           v2 = input("Enter vertex 2 = ")
           weight=input("enter vertex = ")
           obj.addEdge_Undirected_Weighted()

        elif n == 4:
           v1 = input("Enter vertex 1 = ")
           v2 = input("Enter vertex 2 = ")
           weight=input("enter vertex = ")
           obj.addEdge_Directed_Weighted()
        elif n == 5:
            obj.printgraph()
        elif n == 6:
            obj.deletegraph()
        elif n == 0:
            print("Exit")
            break