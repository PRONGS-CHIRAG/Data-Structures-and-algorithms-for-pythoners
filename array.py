"""
Author - Chirag N Vijay
"""

#array introduction
#array is implemented as a module in python .
#Functions-
"""array(datatype,valueslist)
   append(value)
   insert(position,value)
   pop(value)
   remove(value)- removes first occurence of value
   index(value) - returns index of first occurence of value
   reverse()
   typecode-returns the datatype by which it was initialized
   itemsize-size of single array element in bytes
   buffer_info()- address and no of elements of the array
   count(value)- counts occurences of value
   extend(array)- append array to the original array
   fromlist(list) - appends from list
   tolist() - converts to list
   """
import array

a= array.array('i',[1,2,3,4])
print("array is ")
for i in a:
    print(i)
print()
a.append(8)
print('array after appending 8 is')
for i in a:
    print(i)
print()
a.insert(0,89)
print('array after insertion of 89 at 2 is')
for i in a:
    print(i)
a.pop(4)
print('array after popping 4 is ')
for i in a:
    print(i)
a.append(3)
a.append(3)
print('array is ')
for i in a:
    print(i)
a.remove(3)
print('array after removing 3 is ')
for i in a:
    print(i)
print('array after reversing is ')
a.reverse()
for i in a:
    print(i)
print("index of 8 is " + str(a.index(8)))
print("The datatype of array elements are "+ a.typecode)
print("the itemsize is" + str(a.itemsize))
print(str(a.buffer_info()))
print("count of 3 is " + str(a.count(3)))
a.extend([5,6,7])
for i in a:
    print(i)
b=[6,8,9,0]
a.fromlist(b)
print("after appending from list")
for i in a:
    print(i)
print(a.tolist())


"""
Array Rotation - rotating an array by d spaces
method 1 -
      Store first d elements in a tempp Array
      Append it to end of rest of elements
      time complexity- O(n)
method 2 -
       Rotate one by one
       time complexity - O(n*d)
method 3 -
       create sets equal to number of gcd of n and d and shift elements across sets
       time complexity - O(n)
method 4 -
       divide array to 2 parts a and b
       find (areverse)b
       find (areverse)(breverse)
       find reverse of (areverse)(breverse)"""
#method 2
def LeftRotate(arr,d,n):
    for i in range(d):
        LeftRotateOne(arr,n)
def LeftRotateOne(arr,n):
    temp = arr[0]
    for i  in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1]=temp
arr = [3,4,5,6,7,1,2]
LeftRotate(arr,2,7)
for i in arr:
    print(i)
#method 1
a=[3,4,5,6,7,1,2]
d=2
b = a[:d]
c= a[d:]
c.extend(b)
print(c)
#method 3
def LeftRotateM(arr,d,n):
    a=gcd(d,n)
    for i in range(a):
        temp = arr[i]
        j = i
        while 1:
            k = j + d
            if k >= n:
                k -= n
            if k == i:
                break
            arr[j]=arr[k]
            j=k
        arr[j]=temp
def gcd(d,n):
    if n == 0:
        return d
    else:
        return gcd(n,d%n)
b=[3,4,5,6,7,1,2]
LeftRotateM(b,2,7)
for i in b:
    print(i)
#method 4
print("reversing")
def reverseArray(arr,start,end):
    while(start<end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end]=temp
        start += 1
        end -= 1
def LeftRotateR(arr,d):
    n=len(arr)
    reverseArray(arr,0,d-1)
    reverseArray(arr,d,n-1)
    reverseArray(arr,0,n-1)
a=[3,4,5,6,7,1,2]
LeftRotateR(a,2)
for i in a:
    print(i)
