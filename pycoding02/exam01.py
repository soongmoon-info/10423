sum = float(input('수학점수 입력하세요:')) + float(input('국어점수 입력하세요:')) + float(input('정보점수 입력하세요:'))
average = sum /3
print('총합:', sum)
print('평균점수:',int(sum/ 3))
if average >= 90:
  print('A')
elif average >= 80:
  print('B')
else:
  print('C')
