import time


f=open('content.txt', 'a+')
f.write('virginia1333')
print('write end')
f.close()

f=open('content.txt', 'a+')
txt=f.readlines()
print('txt is----', txt)