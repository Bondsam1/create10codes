#生成10位券碼，包括大寫字母和數字
import random
li=[]
s=[]
doc=open('out.txt','w')
for o in range(10):
  for i in range(9):
    li.append(chr(49+i))
  for j in range(26):
    li.append(chr(65+j))
  for x in range(10):
    s.append(random.choice(li))
  s.append('\n')
  st=''.join(s)
print(st,file=doc)
doc.close()
