"""
it is an implementation of the linked list 
"""


class LL:

    class Node:

        # constructor of the Node
        def __init__(self, data):
            self.data = data
            # self.next will point to the next node in the list
            self.next = None

    # constructor of the LL class
    def __init__(self):
        # self.HEAD will be the head pointer of the linked list and it will initially 0
        self.HEAD = None
        # tail of the linked list
        self.TAIL = None

    # adding a new node to the list
    def addnode(self, data):
        newnode = self.Node(data)
        if self.HEAD == None:
            self.HEAD = newnode
            self.TAIL = newnode
        else:
            self.TAIL.next = newnode
            self.TAIL = newnode

    # deleting a new node from the list
    def deletenode(self, node_number):
        # whichever node the self.HEAD will point will be the 1st node of the list
        """so if you enter node_number as 1 then the first node will be deleted
            ant the 2nd node will become the first node of the linked list
        """
        count = 1
        temp = self.HEAD
        previous_node = self.HEAD

        # if node_number is not in the length of the list
        if (node_number < 1) and (node_number > len(self)):
            print("OUT OF RANGE ERROR")
        # if node_number is 1 , it will be the first node then
        if node_number == 1:
            temp = self.HEAD
            self.HEAD = self.HEAD.next

        while count != node_number:
            previous_node = temp
            temp = temp.next
            count += 1

        # if the node is the last node the we have to update the self.TAIL
        if temp == self.TAIL:
            self.TAIL = previous_node

        # Now delete the selected node
        previous_node.next = temp.next

    # adding a node at n-th poition of the list

    def addnode_nth(self, position, data):
        newnode = self.Node(data)

        count = 1
        """
        if position is 1 then it will be the Head node of the list ,
        similarly if position is 2 it will be the 2nd node of the list and the newnly added node
        should be at 2nd position
        """
        temp = self.HEAD
        previous_node = self.HEAD
        if count != position-1:
            temp = temp.next
            count += 1

        newnode.next = temp.next
        temp.next = newnode

    # display the linked list from head to tail
    def display(self):
        temp = self.HEAD
        while temp != None:
            if temp.next != None:
                print(temp.data, end=' -- ')
            else:
                print(temp.data)
            temp = temp.next

    def __len__(self):
        length = 0
        temp = self.HEAD
        while temp != None:
            temp = temp.next
            length += 1

        return length


if __name__ == '__main__':
    l1 = LL()
    continue_choose = 'y'

    message = """
                LINKED LIST IMPLEMENTATION
                Choose from the options below -->>
                1/ Add a node
                2/ delete a node
                3/ Add a node at n-th position
                4/ Display the entire list
                5/ Length of the list
                """

    while continue_choose == 'y':
        print(message)
        choose = int(input(" Enter your choice from above :: "))
        if choose == 1:
            data = int(input("enter the data for the newnode :: "))
            l1.addnode(data)

        elif choose == 2:
            node_number = int(
                input("Enter the Number of node you want to delete ::"))

            l1.deletenode(node_number)
        elif choose == 3:
            data = int(
                input("enter the data to be inserted in the new node :: "))
            position = int(
                input("enter the position at which you want to insert the newnode :: "))
            l1.addnode_nth(position, data)
        elif choose == 4:
            l1.display()
        elif choose == 5:
            print(f"There are {len(l1)} Nodes are available in the list")
        else:
            print("Wrong input ?! ")

        continue_choose = input("Do you want to continue (y/n) :: ")
