# def f(x):
#   print(x+2)

# f(10)
# print(10) 

# def temp():
#   print('hi')
  
# temp()

def reNum():
  num1 =10
  num2 = 20
  num3 = 30
  return num1, num2, num3
  
def rePrint(a, b, c):
  for i in range(a, b, c):
    print(i)
    
num1, num2, num3 = reNum()
rePrint(num1, num2, num3)