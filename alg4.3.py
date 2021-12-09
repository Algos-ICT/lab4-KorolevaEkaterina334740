def is_correct_brackets(text):
    if '()' in text or '[]' in text:
        text = text.replace('()', '')
        text = text.replace('[]', '')
        return 'YES '
    else:
        return 'NO '


inp = open('input.txt')
out = open('output.txt', 'w')
n = int(inp.readline())


for i in range(n):
    command = inp.readline()
    out.write(str(is_correct_brackets(command)))


inp.close()
out.close()


'''
5
()()
([])
([)]
((]]
)(
'''