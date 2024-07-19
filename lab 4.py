#Question 1
# Implement Stack Using Pyhton

class Stack:
    def __init__(self):
        self.stack = []
        print("Stack Created")
    
    def push(self, data):
        self.stack.append(data)
        print(data,"Pushed into Stack")
    
    def pop(self):
        if len(self.stack) == 0:
            return "Stack is Empty"
        else:
            print(self.stack[-1],"Popped from Stack")
            return self.stack.pop()
    
    def peek(self):
        if len(self.stack) == 0:
            return "Stack is Empty"
        else:
            print(self.stack[-1] , "is the Top Element")
            return self.stack[-1]
        
    def display(self):
        if len(self.stack) == 0:
            return "Stack is Empty"
        else:
            return self.stack[::-1]
        
        
        
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.pop()
stack.peek()
print(stack.display())

# where self is the instance of the class. It is used to access variables that belongs to the class.
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# means in other words we can say that the variable stack is indirectly used as self.stack
# we use self.stack[-1] to access the last element of the stack because stack is a list and we can access the last element of the list by using -1 index

#Question 2
# Implement Queue using Python

class Queue:
    def __init__(self):
        self.queue = []
        print("Queue Created")
    
    def enqueue(self, data):
        self.queue.append(data)
        print(data,"Enqueued into Queue")
    
    def dequeue(self):
        if len(self.queue) == 0:
            return "Queue is Empty"
        else:
            print(self.queue[0],"Dequeued from Queue")
            return self.queue.pop(0)
    
    def peek(self):
        if len(self.queue) == 0:
            return "Queue is Empty"
        else:
            print(self.queue[0] , "is the Front Element")
            return self.queue[0]
    
    def display(self):
        if len(self.queue) == 0:
            return "Queue is Empty"
        else:
            return self.queue
        
        
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
queue.dequeue()
queue.peek()
queue.enqueue(60)
queue.dequeue()
print(queue.display())


#Question 3
# In computer science, a binary search or half-interval search algorithm finds the position of 
# a target value within a sorted array. The binary search algorithm can be classified as a 
# dichotomies divide-and-conquer search algorithm and executes in logarithmic time.
# eg there are 9 indexes in the list and we want to find the data. There are three resources low, high and mid.
# low = 0, high = 8, mid = (low + high) / 2 = 4. when all the resources are calculated then we compare the data with the mid value.and when all are at the same index then we return the index and that will be the output.

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1

        # x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1


# Test array
arr = [6,12,17,23,38,45,77,84,90]

# Function call
result = binary_search(arr, 45)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")