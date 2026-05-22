class Graphs:
    def __init__(self):
        pass
    def addNode(self):
        pass
    def addEdge_Undirected(self):
        pass
    def addEdge_Undirected_Weighted(self):
        pass
    def addEdge_Directed_Weighted(self):
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
            obj.addNode()
        elif n == 2:
            obj.addEdge_Undirected()
        elif n == 3:
            obj.addEdge_Undirected_Weighted()
        elif n == 4:
            obj.addEdge_Directed_Weighted()
        elif n == 5:
            pass
        elif n == 6:
            pass
        elif n == 0:
            print("Exit")
        else:
            print("Invalid Choice")