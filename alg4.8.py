def reverse_polish(data):
    stack = []
    for i in data:
        if i in '+*-':
            b = stack.pop()
            print('b = ', b)
            a = stack.pop()
            print('a = ', a)
            result = str(a)+i+str(b)
            print('result = ', result)
            stack.append(eval(result))
        else:
            stack.append(int(i))
            print('i = ', i)
    return stack


def output_w(data_):
    text = ' '.join(map(str, data_))
    with open('output.txt', 'w') as f:
        f.write(str(text))


inp = open('input.txt')
out = open('output.txt', 'w')
input_data = inp.readlines()[1].split()


stack = reverse_polish(input_data)
output_w(stack)


'''7
8 9 + 1 7 - *'''