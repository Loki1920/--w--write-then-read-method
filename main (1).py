# 'w+' write the read method
f  = open('s.txt','w+')
print("blink position at beggining:",f.tell())
f.write("lucky")
print("blink position after writing:",f.tell())
d = f.read()
print("after reading:",f.tell())
print("it will not read anything because blink position is at last character:",d)