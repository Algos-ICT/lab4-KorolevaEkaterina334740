class Stack:
    def __init__(self):
        self.stack = []
        self.max = None

    def pop(self):
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop()
        if len(self.stack) == 0:
            self.max = None
        elif removed == self.max:
            self.max = self.stack[0]
            for value in self.stack:
                if value > self.max:
                    self.max = value
        return removed

    def push(self, item):
        self.stack.append(item)
        if len(self.stack) == 1 or item > self.max:
            self.max = item

    def max_in_Stack(self):
        return self.max


s = Stack()
inp = open('input.txt')
out = open('output.txt', 'w')
n = int(inp.readline())


for i in range(n):
    command = inp.readline().split()
    if command[0] == 'pop':
        s.pop()
    elif command[0] == 'push':
        s.push(int(command[1]))
    else:
        print(s.max_in_Stack())
        out.write(str(s.max_in_Stack()))


inp.close()
out.close()


'''5
push 2
push 1
max
pop
max'''


'''5
push 1
push 2
max
pop
max'''


'''3
push 1
push 7
pop'''


'''10
push 2
push 3
push 9
push 7
push 2
max
max
max
pop
max'''


'''6
push 7
push 1
push 7
max
pop
max'''