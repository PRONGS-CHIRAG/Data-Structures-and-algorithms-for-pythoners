'''
Author : Chirag N Vijay
Linked stack implementation - stack implementation as linked list
'''
class LinkedStack():
    '''Here we are using a user defined class Node which contains element i.e the data of that node and next which is reference to the next Node'''
    class _Node:
        __slots__ = '_element','_next'
        def __init__(self,element,next):
            self._element=element
            self._next=next
    def __init__(self):
        self._head=None
        self._size=0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size==0
    def push(self,e):
        self._head=self._Node(e,self._head)
        self._size+=1
    def display(self):
        ptr = self._head
        while ptr._next !=None:
            print(ptr._element)
            ptr=ptr._next
        print(ptr._element)
    def top(self):
        if self.is_empty():
            print("Stack is empty")
        return self._head._element
    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        answer=self._head._element
        self._head=self._head._next
        self._size -= 1
        return answer
a=LinkedStack()
a.push(4)
a.push(9)
a.push(16)
a.push(25)
#print(len(a))
#print(a.top())
#print(a.pop())
a.display()
