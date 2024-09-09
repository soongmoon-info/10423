battery_remain = int(input('배터리 잔량을 입력해주세요:'))

if battery_remain < 2:
  print('종료')
elif battery_remain <= 10:
  print('충전해주세요')
elif battery_remain <= 20:
  print('저전력 모드')
else:
  print('정상출력')