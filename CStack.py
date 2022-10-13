class CStack:
    def __init__(self, size = 3):
        self.stack = []
        self.size = size
    def __str__(self, size = 3):
        return str(self.stack)
    def push(self, data):
        if len(self.stack) < self.size:
            self.stack.append(data)
        else:
            print("stack is full!")
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            print("empty stack")
if __name__ =="__main__":
    stack = CStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack)
    print("pop", stack.pop())
    print(stack)