class Stack:
    def __init__(self):
        self.data = []
    def pop(self):
        if len(self.data) == 0:
            print("The Stack is Empty!")
        else:
            return self.data.pop(-1)            
    def push(self, d):
        self.data.append(d)
    def size(self):
        return len(self.data)

class MyQueue():
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()
    def push(self, d):
        if self.s1.size() == 0:
            self.s1.push(d)
        else:
            self.s2.push(d)
        print(self.s1.data, self.s2.data)
    def pop(self):
        print(self.s1.pop())
        if self.s1.size() == 0:
            print("reverse")
            for _ in range(self.s2.size()):
                self.s1.push(self.s2.pop())

if __name__ == '__main__':
    q = MyQueue()
    q.push(1)
    q.push(4)
    q.push(3)
    q.pop()
    q.pop()
    q.pop()
    q.pop()
        