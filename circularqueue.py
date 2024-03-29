'''
Topic : Circular Queue
Author : Chirag N Vijay'''
class CircularQueue:
    class _Node:
        __slots__ = '_element','_next'
        def __init__(self,element,next):
            self._element=element
            self._next=next
    def __init__(self):
        self._tail=None
        self._size=0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size==0
    def first(self):
        if self.is_empty():
            print('queue is empty')
        head = self._tail._next
        return head._element
    def deque(self):
        if self.is_empty():
            print('queue is empty')
        old_head = self._tail._next
        if self._size==1:
            self._tail=None
        else:
            self._tail._next=old_head._next
        self._size -= 1
        return old_head._element
    def enqueue(self,e):
        newest=self._Node(e,None)
        if self.is_empty():
            newest._next=newest
        else:
            newest._next=self._tail._next
            self._tail._next=newest
        self._tail=newest
        self._size +=1
    def rotate(self):
        if self._size>0:
            self._tail=self._tail._next
    def display(self):
        ptr=self._tail
        while ptr._next != self._tail:
            print(ptr._element)
            ptr=ptr._next
        print(ptr._element)
a= CircularQueue()
a.enqueue(1)
a.enqueue(2)
a.enqueue(3)
a.enqueue(4)
a.display()
a.deque()
a.deque()
#a.display()
