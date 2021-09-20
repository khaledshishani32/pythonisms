from functools import wraps
from time import sleep

def decorate_null(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        return_val = func(*args, **kwargs)

        decorator = f'The LinkedList Representation is : {return_val} + NULL'

        return decorator

    return wrapper

def decorate_index(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        return_val = func(*args, **kwargs)

        decorator = f'The index of item wanted is : {return_val}'

        return decorator

    return wrapper

def decorate_len(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        return_val = func(*args, **kwargs)

        decorator = f'The length linked list is  : {return_val}'

        return decorator

    return wrapper

class Node: 
    def __init__(self,value =''):
        self.value = value
        self.next= None 

    def __str__(self):
        return str(self.value)


    # def __add___(self , other):
    #     return Node(*(x+y for x,y in zip(self.value , other.value)))





class LinkedList():
    
    def __init__(self):
        self.head = None

    all_values = 0
   
    def insert(self,value):

        node = Node(value)
        
        
        if self.head:
            node.next = self.head
        
        
        self.head = node

        

    def __iter__(self):

        current = self.head

        while current : 
           yield current.value 
           current = current.next
           
           
    @decorate_len
    def __len__(self):
        return len(list(iter(self)))

    @decorate_null   
    def __str__(self):
       
        string = ""
        for value in self:
            string = string + f"{ {value} } -> "
        
        return string
        
    @decorate_index
    def __getitem__(self, idx):
   
        if idx < 0:
           raise IndexError

        for i, elemant in enumerate(self):
            if i == idx:
               return elemant
        
        raise IndexError





if __name__ == '__main__' :
    num_one=LinkedList()
    num_one.insert(1)
    num_one.insert(2)
    num_one.insert(3)
    print(num_one)





 