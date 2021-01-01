import sys


class Stack:
    def __init__(self):
        self.stk = []

    def push(self, num):
        self.stk.append(num)

    def pop(self):
        if not self.empty():
            print(self.top())
            self.stk.pop()
        else:
            print(-1)

    def size(self):
        return len(self.stk)

    def empty(self):
        return 0 if len(self.stk) > 0 else 1

    def top(self):
        return -1 if self.empty() else self.stk[-1]


n = int(sys.stdin.readline())
stack = Stack()
for i in range(n):
    command = list(sys.stdin.readline().rstrip().split(" "))
    if command[0] == 'push':
        stack.push(int(command[1]))
    elif command[0] == 'pop':
        stack.pop()
    elif command[0] == 'empty':
        print(stack.empty())
    elif command[0] == 'top':
        print(stack.top())
    elif command[0] == 'size':
        print(stack.size())