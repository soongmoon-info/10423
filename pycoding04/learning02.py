a = ['사과', '배', '샤인머', '수박', '딸기']

for i in a:
  if i =='샤인머':
    continue
  print(i)
  

b= [5, 4, 3, 2, 1]  
for index, value in enumerate(b):
  print(index, value)
  
for i in range(2, 10):
  print(i, '단')
  for j in range(1,10):
    print(i,'*',j,"=",j*i)
    
a = [['사과', 1200], ['배', 0], ['샤인머', 12000]]

for i1, v1 in enumerate(a):
  for i2, v2 in enumerate(v1):
    if v2 == 0:
      a[i1][1] = 100
    