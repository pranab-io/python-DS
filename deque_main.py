# implementation of deque using circular array

class Deque:
    def __init__(self, MAX_SIZE):
        self.MAX_SIZE = MAX_SIZE
        self.deque = [None for i in range(self.MAX_SIZE)]
        self.FRONT = -1
        self.REAR = -1

    def insertfront(self, data):
        if (self.FRONT == (self.REAR + 1) % self.MAX_SIZE):
            print("DEQUE is full ! Cant insert..")
        # else if there is nothing in the queue
        elif self.FRONT == -1 and self.REAR == -1:
            self.FRONT = 0
            self.REAR = 0
            self.deque[self.FRONT] = data
        elif self.FRONT == 0:
            self.FRONT = (self.MAX_SIZE - 1)
            self.deque[self.FRONT] = data
        else:
            self.FRONT = self.FRONT - 1
            self.deque[self.FRONT] = data

    def insertrear(self, data):
        if (self.FRONT == (self.REAR + 1) % self.MAX_SIZE):
            print("DEQUE is full ! Cant insert..")
        # else if there is nothing in the queue
        elif self.FRONT == -1 and self.REAR == -1:
            self.FRONT = 0
            self.REAR = 0
            self.deque[self.REAR] = data
        elif self.REAR == (self.MAX_SIZE - 1):
            self.rear = 0
            self.deque[self.rear] = data
        else:
            self.REAR += 1
            self.deque[self.REAR]

    def getfront(self):
        print(f'The front item is {self.deque[self.FRONT]}')

    def getrear(self):
        print(f'The rear item is {self.deque[self.REAR]}')

    def deletefront(self):
        # IF there is nothing in the queue
        if self.FRONT == -1 and self.REAR == -1:
            print("\nDEQUE IS EMPTY ...", end='\n')

        # if there is only one eleemnt in the queue i.e front==rear
        elif self.FRONT == self.REAR:
            print(f'Dequeued element is {self.deque[self.REAR]}')
            self.deque[self.FRONT] == None
            self.FRONT = -1
            self.REAR = -1

        #  if front == MAX_SIZE - 1
        elif self.FRONT == self.MAX_SIZE-1:
            print(f'Dequeued element is {self.deque[self.FRONT]}')
            self.FRONT = (self.FRONT + 1) % self.MAX_SIZE
        else:
            print(f'Dequeued element is {self.deque[self.FRONT]}')
            self.FRONT += 1

    def deleterear(self):
        if self.FRONT == -1 and self.REAR == -1:
            print("\nDEQUE IS EMPTY ...", end='\n')

        # if there is only one eleemnt in the queue i.e front==rear
        elif self.FRONT == self.REAR:
            print(f'Dequeued element is {self.deque[self.REAR]}')
            self.deque[self.FRONT] == None
            self.FRONT = -1
            self.REAR = -1

        # if rear points to the 0th index element then
        elif self.REAR == 0:
            print(f'Dequeued element is {self.deque[self.REAR]}')
            self.REAR = self.MAX_SIZE - 1

        else:
            print(f'Dequeued element is {self.deque[self.REAR]}')
            self.REAR -= 1

    def display(self):
        """ Whatever the data is between front and rear we will print That """
        i = self.FRONT
        while i != self.REAR:
            print(self.deque[i], end=' ')
            i = (i+1) % self.MAX_SIZE
        print(self.deque[self.REAR])


if __name__ == '__main__':
    d1 = Deque(5)
    choice = 'y'
    choice2 = 0
    while choice == 'y':
        print(
            """                1. insertfront
                2. insertrear
                3. deletefront
                4. deleterear
                5. getfront
                6. getrear
                7. display
                """


        )
        choice2 = input("Enter your choice : ")
        if choice2 == '1':
            data = int(input("enter the data : "))
            d1.insertfront(data)
        elif choice2 == '2':
            data = int(input("enter the data : "))
            d1.insertrear(data)
        elif choice2 == '3':
            d1.deletefront()
        elif choice2 == '4':
            d1.deleterear()
        elif choice2 == '5':
            d1.getfront()
        elif choice2 == '6':
            d1.getrear()
        elif choice2 == '7':
            d1.display()
        else:
            exit()
