#To create the linked list I created a class "node" as linked list is nothing but a chain of nodes
class Node:
    #creating a constructor for node values
    def __init__(self, data):
        self.data = data #node carries only data
        self.next = None #and the reference/address for the next node value
#creating a class "LinkedList" to connect all the nodes
class LinkedList:
    def __init__(self):
        self.head = None #initially the list head will have no value
    #creating a method for printing the list values
    def printList(self):
        temp = self.head #giving self.head a smaller name by putting it into a variable
        #using while loop as we know the condition for stopping the iteration
        while(temp):
            print(temp.data)#printing the value of the head
            temp = temp.next#temp will now hold the next head value
if __name__ == '__main__':
    llist = LinkedList() #creating a variable that inherits the class "LinkedList"
    # feeding input as a value for the list head
    llist.head = Node(3)#llist.head inherits the class "Node" and "1" is the data for the node
    #feeding more data via class "Node"
    second = Node(4)
    third = Node(9)

    #feeding next address which will be the head now
    llist.head.next = second
    #reference for the next value
    second.next = third

    #printing the whole list
    llist.printList()
