__author__ = 'Jim'
from random import randint

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node

        else:
            self.tail.next = node
            self.tail = node

    def __str__(self):
        if self.head != None:
            index = self.head
            nodestore = [str(index.value)]

            while index.next != None:
                index = index.next
                nodestore.append(str(index.value))

            return "LinkedList [ "+" -> ".join(nodestore)+" ]"
        return "[]"

    def removeNode(self,n):
        curr_val = self.head
        if curr_val == n:
            self.head = self.head.next
        while(curr_val.next!=None):
            if curr_val.next.val == n:
                curr_val.next = curr_val.next.next
                break
            else:
                curr_val = curr_val.next


#Write code to remove duplicates from an unsorted linked list.

    def deleteDups(self):
        curr = self.head
        while curr!= None:
            runner = curr
            while runner.next != None:
                if runner.next.value == curr.value:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            curr = curr.next

#Implement an algorithm to find the nth to last element of a singly linked list

    def nthtoLast(self,n):
        count = 0
        p2 = self.head
        for i in range(n-1):
            if p2.next != None:
                p2 = p2.next

        nodestore = ''
        new_head = p2
        while p2.next != None:
            count += 1
            p2 = p2.next
            nodestore += str(p2) + '->'
        return nodestore

#Implement an algorithm to delete a node in the middle of a single linked list, given only access to that node.

    def deletespecific(self,node):
        if node.next != None:
            node.next = node.next.next
            node.value = node.next.value
        else:
            node.value = None

#Add tow nodes

def add_two_nodes(L1,L2):
    p1 = L1.head
    p2 = L2.head
    carry = 0
    linkedlist_sum = LinkedList()
    while(p1!=None) or (p2!=None) or (carry !=0):
        dig_sum = carry
        if p1!=None:
            dig_sum += p1.value
            p1 = p1.next
        if p2!=None:
            dig_sum += p2.value
            p2 = p2.next
        linkedlist_sum.addNode(dig_sum%10)
        carry = dig_sum/10
    return linkedlist_sum

#Circular Linked List

def randomLinkedList(length, min, max):
    linkedlist = LinkedList()
    for i in range(length):
        value = randint(min, max)
        linkedlist.addNode(value)
    return linkedlist

L1 = randomLinkedList(9, 3, 7)
L2 = randomLinkedList(9, 3, 7)
L1.nthtoLast(3)
node = L1.head.next.next
L1.deletespecific(node)
print(L1)
print(L2)
add_two_nodes(L1,L2)




