math = float(input('수학점수 입력하세요:'))
korean =  float(input('국어점수 입력하세요:'))
information =  float(input('정보점수 입력하세요:'))
sum = math + korean + information
average = sum /3
print('총합:', sum)
print('평균점수:',int(sum/ 3))
if math < 30 or korean < 30 or information < 30:
  print('F')
elif average >= 90:
  print('A')
elif average >= 80:
  print('B')
else:
  print('C')