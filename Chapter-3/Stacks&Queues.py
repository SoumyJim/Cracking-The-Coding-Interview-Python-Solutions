__author__ = 'Jim'

#Stacks.py

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self,e):
        return self.items.append(e) #appended to the last item. So FIFO

    def pop(self):
        return self.items.pop() #pop removes the last item.

    def size(self):
        return len(self.items)

    def peek(self):
        return None if self.is_empty() else self.items[-1]

    def __len__(self):
        return len(self.items)

    def __str__(self):
        new_str = ''
        for e in self.items:
            new_str = new_str + str(e) + ','
        return new_str

#Queue.py

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.insert(0,item) #inserts items to the first position. FILO

    def dequeue(self):
        self.items.pop() #removes the last item, first item which came into the queue

    def size(self):
        return len(self.items)


#Describe how you could use a single array to implement three stacks.

class SingleStackArray:
    def __init__(self,size=10,number=3):
        self.size = size
        self.number = number
        self.array = [None] * self.size * self.number
        self.pointer = [-1] * self.number

    def stacktop(self,stacknum):
        return self.size * stacknum +self.pointer[stacknum]


    def push(self,stacknum,value):
        if self.pointer[stacknum] +1 >= self.size:
            print "No sufficient space"
        else:
            self.pointer[stacknum] += 1
            self.array[self.stacktop(stacknum)] = value

    def pop(self,stacknum):
        if self.pointer[stacknum] -1 < 0:
            print "No elements to pop"
        else:
            data = self.array[self.stacktop(stacknum)]
            self.array[self.stacktop(stacknum)] = None
            self.pointer[stacknum] -= 1
            return data

    def peek(self,stacknum):
        if self.pointer[stacknum] -1 <0:
            print "Empty array"
        else:
            return self.array[self.stacktop(stacknum)]

    def is_empty(self,stacknum):
        return self.pointer[stacknum] == -1

s = SingleStackArray()
s.push(2,11)
s.push(2,17)
print(s.peek(2))
print(s.is_empty(1))

#stack having min element.
#-1 access the last element of the list

class StackWithMin:
    def __init__(self):
        self.stack = []
        self.min=[]

    def push(self,value):
        self.stack.append(value)
        if len(self.min)==0 or value <= self.min[-1]:
            self.min.append(value)

    def pop(self):
        if len(self.stack) == 0:
            return None
        data = self.stack.pop()
        if data == self.min[-1]:
            self.min.pop()
        return data

    def get_min(self):
        if len(self.min) == 0:
            return None
        return self.min[-1]

    def __str__(self):
        return self.items


from random import randrange
Stack1 = StackWithMin()
for i in range(15):
    data = randrange(1,100)
    Stack1.push(data)

for i in range(15):
    str(Stack1.pop())
    str(Stack1.get_min())

#Set of Stacks

class SetOfStacks:

    def __init__(self,capacity):
        self.capacity = capacity
        self.stack = []

    def push(self,value):
        if len(self.stack) == 0 or len(self.stack[-1])==self.capacity:
            self.stack.append([])
        self.stack[-1].append(value)

    def pop(self):
        if len(self.stack)==0:
            return None
        data = self.stack[-1].pop()
        return data

    def popAt(self,index):
        if index < 1 or index > len(self.stack) or len(self.stack[index-1]) == 0:
            return None
        else:
            return self.stack[index-1].pop()

def test():
    setofstacks = SetOfStacks(8)
    for i in range(24):
        setofstacks.push(i)
        print i,

    for i in range(5):
        print "Poped"+str(setofstacks.pop())

    print "Test for popAt"
    for i in range(5):
        for i in range(3):
            print "Poped"+str(setofstacks.popAt(i+1))


if __name__ == "__main__":
    test()


#Moving disks

class Hanoi:
    def __init__(self,size):
        self.towers = [[], [], []]
        self.size = size
        self.towers[0] = [x for x in range(size, 0, -1)]

    def play_hanoi(self):
        self.print_towers()
        self.move_disk(self.size,1,2,3)
        self.print_towers()

    def move_disk(self, size, fr, helper, to):
        if size == 1:
            data = self.towers[fr-1].pop()
            self.towers[to-1].append(data)
            print "Disk", data, ": Tower", fr, "->", to
        else:
            self.move_disk(size - 1, fr, to, helper)
            self.move_disk(1, fr, helper, to)
            self.move_disk(size - 1, helper, fr, to)

    def print_towers(self):
        for i in self.towers:
            print i


h = Hanoi(3)
h.play_hanoi()

#My Queue class:

class MyQueue:

    def __init__(self):
        self.stackOldest = Stack()
        self.stackNewest = Stack()

    def push(self,value):
        self.stackNewest.push(value)

    def pop(self):
        if len(self.stackOldest) == 0:
            self.moveToOldest()
        return self.stackOldest.pop()

    def moveToOldest(self):
        while(len(self.stackNewest)):
            self.stackOldest.push(self.stackNewest.pop())


queue = MyQueue()
for i in range(1,5):
    queue.push(i)
    print "Enqueued",i
    queue.push(i*2)
    print "Enqueued", i*2
    data = queue.pop()
    print "Dequeued", data


#sort the stack in ascending order
def sortedStack(s):
    sorted_stack = Stack()
    while not s.is_empty():
        data = s.pop()
        while not sorted_stack.is_empty() and sorted_stack.peek() > data:
            s.push(sorted_stack.pop())
        sorted_stack.push(data)
    print str(sorted_stack)

stacksort = Stack()
stacksort.push(7)
stacksort.push(5)
stacksort.push(9)
stacksort.push(4)
stacksort.push(2)
sortedStack(stacksort)