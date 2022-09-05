result = ''
with open('temp.txt') as f:
    for line in f.readlines():
        c = chr(int(line))
        result += c

print(result)
