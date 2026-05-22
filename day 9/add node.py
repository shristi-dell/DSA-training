class Graphs:

    def __init__(self):
        self.nodes = []
        self.graph = []
        self.nodeCount = 0

    def addNode(self, v):

        if v in self.nodes:
            print(v, "is already present in graph")

        else:
            self.nodeCount += 1
            self.nodes.append(v)

            for x in self.graph:
                x.append(0)

            temp = []

            for x in range(self.nodeCount):
                temp.append(0)

            self.graph.append(temp)

            print(v, "is added")

    def addEdge_Undirected(self):

        v1 = input("Enter first node: ")
        v2 = input("Enter second node: ")

        if v1 not in self.nodes:
            print(v1, "not present")

        elif v2 not in self.nodes:
            print(v2, "not present")

        else:
            index1 = self.nodes.index(v1)
            index2 = self.nodes.index(v2)

            self.graph[index1][index2] = 1
            self.graph[index2][index1] = 1

            print("Edge added between", v1, "and", v2)

    def addEdge_Undirected_Weighted(self):
        pass

    def addEdge_Directed_Weighted(self):
        pass

    def printgraph(self):

        print("   ", end="")

        for node in self.nodes:
            print(node, end=" ")

        print()

        for i in range(self.nodeCount):

            print(self.nodes[i], end="  ")

            for j in range(self.nodeCount):
                print(self.graph[i][j], end=" ")

            print()

    def deletegraph(self):
        pass


if __name__ == "__main__":

    obj = Graphs()

    while True:

        print("\n1. Add Node")
        print("2. Add Edge Undirected")
        print("3. Add Edge Undirected Weighted")
        print("4. Add Edge Directed Weighted")
        print("5. Print Graph")
        print("6. Delete Operation")
        print("0. Exit\n")

        n = int(input("Enter any choice: "))

        if n == 1:

            v = input("Enter node: ")
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