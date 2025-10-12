class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.length=0
    #add the element push
    def enqueue(self,x) :
        self.length+=1

        newNode=Node(x)
        if self.front is None:
            self.front=newNode
            self.rear=newNode
        else:
            self.rear.next=newNode
            self.rear=newNode      
        # delete the element pop
    def dequeue(self):
            self.length-=1
            if self.front is None:
             
             return -1   
            x=self.front.data
            self.front=self.front.next
            if self.front is None:
                self.rear=None
            return x  
    def getfront(self):
           if self.front is None:
             
             return -1  
           return self.front.data
    def Size(self):
         if self.front is None:
             
             return -1 
         return self.length
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.dequeue())  # 10 first elemnt delete hoga
print(q.getfront()) # pahle elemnt return karega
print(q.Size()) #number of element return karega
