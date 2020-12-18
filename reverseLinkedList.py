# -*- coding: utf-8 -*-
"""
LinkedList class with .reverse() method.
I wrote this class without consulting any references to practice a common coding interview skill,
the ability to reverse a linked list.

Created on Thu Dec 17 15:12:53 2020

@author: MKhour
"""


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self): # a __str__() method will be helpful for testing the reversal
        returnVal = "{}".format(self.value)
        if self.next != None:
            returnVal = returnVal + ", " + self.next.__str__()
        return returnVal # in base case, it just returns this node's value as a string
        
    
    """
    At the end of this method, 'head' will reference the beginning of the linked list (the first node).
    The linked list will be reversed. Note: the original list is NOT preserved, so the result of this
    operation should be stored.
    """    
    def reverse(self):
        lastNode, head = self.reverseHelper()
        lastNode.next = None #ties up loose ends
        return head
            
    """
    The recursive helper method to reverse the list. Uses a tuple to keep track of the head of the list 
    while also iterating through all the nodes, reversing the .next assignments.
    """        
    def reverseHelper(self): #trying a recursive method
        if self.next != None: #if not at the final node (recursive case)
            previousNode, head = self.next.reverseHelper() #recursive call to get the previous node and the head of the list
            previousNode.next = self
            return self, head #using a tuple return type to track the nodes as we go and pass along 'head'
        else: #base case
           head = self
           return self, head #the head of the list is this node
            
       
if __name__ == '__main__': #test the methods
    
    #make the list:
    testList = LinkedList(4)
    nodeThree = LinkedList(3)
    nodeTwo = LinkedList(2)
    nodeOne = LinkedList(1)
    nodeZero = LinkedList(0)

    testList.next = nodeThree
    nodeThree.next = nodeTwo
    nodeTwo.next = nodeOne
    nodeOne.next = nodeZero

    #test the reversal:
    print("original list: {}".format(testList))
    testList = testList.reverse()
    print("reversed list: {}".format(testList))
    testList = testList.reverse()
    print("reverse again: {}".format(testList))