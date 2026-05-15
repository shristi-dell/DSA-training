import sys
class stacks:
    def __init__(self):
        self.stack=[]
    def push(self):
        self.stack.append(int(input("enter element")))
    def pop(self):
        if len(self.stack)==0:
            print("stack empty")
        else:
            print(self.stack.pop())
    def traverse(self):
        print(*self.stack)
    def peek(self):
        if len(self.stack)==0:
            print("stack empty")
        else:
            print(self.stack[-1])

if __name__=='__main__':
    obj=stacks()
    while True:
        print("1.push\n2.pop\n3.peek\n4.traverse\n0.exit")
        ch=int(input("select any choice"))
        if ch==1:
            obj.push()
        elif ch==2:
            obj.pop()
        elif ch==3:
            obj.peek()
        elif ch==4:
            obj.traverse()
        elif ch==0:
            sys.exit()