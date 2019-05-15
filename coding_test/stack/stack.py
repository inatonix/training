class Stack:
    def __init__(self, data):
        self.data = data
    def pop(self):
        if len(self.data) == 0:
            print("The Stack is Empty!")
        else:
            return self.data.pop(-1)            
    def push(self, d):
        self.data.append(d)

class Queue:
    def __init__(self, data):
        self.data = data
    def pop(self):
        if len(self.data) == 0:
            print("The Stack is Empty!")
        else:
            return self.data.pop(0)
    def push(self, d):
        self.data.append(d)



if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(4)
    s.push(3)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    s.pop()