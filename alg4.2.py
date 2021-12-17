from collections import deque


dq = deque()
answer = []


inp = open('input.txt')
out = open('output.txt', 'w')
n = int(inp.readline())


for i in range(n):
    command = inp.readline()
    if command[0] != "-":
        command = int(command[1:])
        dq.append(command)
    else:
        answer.append(dq.popleft())


out.write(str(answer))
print(answer)


inp.close()
out.close()


'''
4
+1
+10
-
-
'''