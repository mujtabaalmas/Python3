##implementing stack using arrays ---------------------
# class Stack:
#   def __init__(self):
#     self.stack = []

#   def push(self, element):
#     self.stack.append(element)

#   def pop(self):
#     if self.isEmpty():
#       return "Stack is empty"
#     return self.stack.pop()

#   def peek(self):
#     if self.isEmpty():
#       return "Stack is empty"
#     return self.stack[-1]

#   def isEmpty(self):
#     return len(self.stack) == 0

#   def size(self):
#     return len(self.stack)

# # Create a stack
# myStack = Stack()

# myStack.push('A')
# myStack.push('B')
# myStack.push('C')

# print("Stack: ", myStack.stack)
# print("Pop: ", myStack.pop())
# print("Stack after Pop: ", myStack.stack)
# print("Peek: ", myStack.peek())
# print("isEmpty: ", myStack.isEmpty())
# print("Size: ", myStack.size())


##implementing stack using linked_list ------------------------------
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
  def __init__(self):
    self.head = None
    self.size = 0

  def push(self, data):
    new_node = Node(data.upper())
    if self.head:
      new_node.next = self.head
    self.head = new_node
    self.size+=1

  def pop(self):
    if self.isEmpty():
      return "Stack is empty"
    popped_node = self.head
    self.head = self.head.next
    self.size -=1
    return popped_node.data

  def peek(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.head.data

  def isEmpty(self):
    return self.size == 0

  def stack_size(self):
    return self.size
  
  def print_stack(self):
    currentnode = self.head
    while currentnode:
      print(currentnode.data, end=' -> ',)
      currentnode = currentnode.next
    print()


myStack = Stack()
##for user inputs
# inputingstack = input("Enter value to push to stack: ")
# myStack.push(inputingstack)
# inputingstack = input("Enter value to push to stack: ")
# myStack.push(inputingstack)
# inputingstack = input("Enter value to push to stack: ")
# myStack.push(inputingstack)

myStack.push('d') #if we enter lower case it will automatically add uppercase letter just simply added the .upper method in push 
myStack.push('S')
myStack.push('a')
myStack.push('M')
print("LinkedList: ", end="")
myStack.print_stack()
print("Peek: ", myStack.peek())
print("Pop: ", myStack.pop())
print("LinkedList after Pop: ", end="")
myStack.print_stack()
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.stack_size())
