
def binary(j:int):
  num = ""
  while True:
    if j % 2 ==0:
      num = '0' + num 
      j = j//2
    else:
      num =  '1'+ num 
      j = j//2
    if j == 0:
      num = int(num)
      return num
print(binary(10))