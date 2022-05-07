f = open('text.txt', 'r')
print(f.read())
f.close()

f = open('text.txt', 'w')
f.write('222')
f.close()

f = open('text.txt', 'r')
print(f.read())
f.close()