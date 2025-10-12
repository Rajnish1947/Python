class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.top=None

        self.lenth=0
    def Push(self,x):
        self.lenth+=1
        if self.top is None:
            self.top=Node(x) 
        else:
            newNode=Node(x)
            newNode.next=self.top 
            self.top=newNode
    def pop(self):
         
         
         if self.top is None:
             return -1
         self.lenth-=1
         
         x=self.top.data
         self.top=self.top.next
         return  x  
    def getTop(self):

        if self.top is None:
             return -1
        return self.top.data  
    def Size(self):
        if self.top==None:
             return -1
        return self.lenth
    
stack=Stack()   
stack.Push(5) 
stack.Push(4) 
stack.Push(3) 
stack.Push(1) 

print(stack.Size())
print(stack.pop())
print(stack.getTop())
