# pahle node create karte hai

class Node:

    def __init__(self,data): #__init__ is a constructor in Python classes. It is automatically
                            # called when we create an object of the class. It initializes the object with values."
        self.data=data #"self represents the current object. It allows us to store data inside the object and access it later. For example,
                         #self.data stores the value of the node, and self.next points to the next node."
        self.next=Node

        # data → which stores the value
        #next which stores a reference (or address) of the next node."