'''
Linked queue
Author : Chirag N Vijay
'''
class LinkedQueue:
    class _Node:
        __slots__ = '_element','_next'
        def __init__(self,element,next):
            self._element=element
            self._next=next
    def __init__(self):
        self._head=None
        self._tail=None
        self._size=0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size==0
    def first(self):
        if self.is_empty():
            print("Queue is empty")
        return self._head._element
    def deque(self):
        if self.is_empty():
            print("queue is empty")
        answer=self._head._element
        self._head=self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail=None
        return answer
    def enqueue(self,e):
        newest=self._Node(e,None)
        if self.is_empty():
            self._head=newest;
        else:
            self._tail._next=newest
        self._tail=newest
        self._size +=1
    def display(self):
        ptr=self._head
        while ptr._next != None:
            print(ptr._element)
            ptr=ptr._next
        print(ptr._element)
a= LinkedQueue()
a.enqueue(1)
a.enqueue(2)
a.enqueue(3)
a.enqueue(4)
a.display()
a.deque()
a.deque()
a.display()
