class Node:
  def __init__(self,info,next=None):
    self.info=info
    self.next=next
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0  # number of nodes in my LL

    def addToTail(self, info):  # O(1)
        n = Node(info)
        if self.size == 0:  # LL is empty
            self.head = n
            self.tail = n
            self.size += 1
        else:
            self.tail.next = n
            self.tail = n
            self.size += 1

    def deleteHead(self):  # O(1)

        if self.size == 0:
            return None
        if self.size == 1:
            temp = self.head.info
            self.head = None
            self.tail = None
            self.size = 0
            return temp

        temp = self.head.info
        self.head = self.head.next
        self.size -= 1
        return temp


class Queue:
    def __init__(self):
        self.elements = LinkedList()

    def isEmpty(self):
        return self.elements.size == 0  # returns True if the LinkedList of the queue is empty, False otherwise

    def enqueue(self, item):
        self.elements.addToTail(item)

    def dequeue(self):
        return self.elements.deleteHead()


class Stack:
    def __init__(self):
        self.elements = []

    def push(self, item):
        self.elements.append(item)

    def isEmpty(self):
        return len(self.elements) == 0

    def pop(self):
        if len(self.elements) == 0:
            return None
        return self.elements.pop()


# Stacks and Queues
def is_Palindrome(input_str): #O(n)
    reversed_str = ''  # Empty string to add the symbols to
    edited_input_str = input_str.replace(" ", "").replace("'", "").replace(",", "").lower()  # Remove spaces, commas, and apostrophe and make all characters lower case
    S = Stack()
    for char in edited_input_str:  # Push characters to the stack #O(n) where n is the length of the input string
        S.push(char)

    while not S.isEmpty():  # Pop the characters from the stack #
        reversed_str += S.pop()

    if reversed_str == edited_input_str:  # Because stacks work as "last in first out" this line will show if the string is a palindrome or not
        return True
    else:
        return False


def is_balanced (expression):#O(n) where n is the length of the experssion
    stack = Stack()

    for char in expression:#O(n) where n is the length of the experssion
        if char in '([{':
            stack.push(char)
        elif char in ')]}':
            if stack.isEmpty():
                return False  # Closing symbol and no other symbols remaining(no opening symbol for it)
            top = stack.pop()
            if (char == ')' and top != '(') or \
                    (char == ']' and top != '[') or \
                    (char == '}' and top != '{'):
                return False  # Mismatched opening and closing symbols

    return stack.isEmpty()  # The expression is balanced if the stack is empty at the end(all opening symbols are popped and the function didn't return false yet)

# Queues
def car_wash(): #O(n) where n is how much we have in the queue
    Q = Queue()
    print("We just opened the car wash!")
    empty_waiting_list = False
    while not empty_waiting_list: 
        option = ''
        empty_waiting_list = False
        while option.lower() != 'add' and option.lower() != 'remove': # when no input is enterned it will just repeat 
            option = input('Do you want to add or remove a car: ')
        if option == 'add':
            make = input('Please input the make of the car: ')
            color = input('Please input the color of the car: ')
            plate_number = int(input('Please input the plate number of the car: '))
            car = [make, color, plate_number] #List created wuth car info 
            Q.enqueue(car)# add them into Q  which is the the Queue
            print('Your car is added to the waiting list')
        else:
            if Q.isEmpty(): #in case th user press remove at the firs time they tuen on the program 
                empty_waiting_list = True
                print('There are no cars to remove')
            else:
                removed_car = Q.dequeue() 
                print(f'The {removed_car[1]} {removed_car[0]} with car plate number: {removed_car[2]}, is done.') #print the detailes of the car 
                if Q.isEmpty(): #turn of the program when no car are in queue
                    empty_waiting_list = True
                    print('There are no cars left in the queue, the program will close.')

# Stack
def decoding_message(message): #O(n) whene n in teh len of the message
    decoded_message = ''
    S = Stack()
    count = 0
    for char in message: #to go over evey CHARACTER IN THE STRING #O(n) whene n in teh len of the message
        if char != '*': # to save all non star values into the stack 
            S.push(char)
        else:
            decoded_message += S.pop() #to push when the star begin the stacked into decoded message
            while not S.isEmpty(): # when the stars are done and we still have values in stack it will pop them to the decoded message to print them 
                decoded_message += S.pop()
        count += 1
    print(decoded_message)

# First Question Example
input_str = "Madam, in Eden, I'm Adam"
result = is_Palindrome(input_str)
print(f"'{input_str}' is palindrome: {result}")

# Second Question Example
expression = "([Hello)]"
result = is_balanced(expression)
print(f"'{expression}' is balanced: {result}")
# Car Wash Run
car_wash()
# Decoding Message
decoding_message('SIVLE ****** DAED TNSI ***')