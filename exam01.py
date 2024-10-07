student = [['강호명','10100',36.6,67.1,55.4,'none'],   # [이름, 학번, 수학점수, 국어점수, 정보점수, 빈공간(삭제 필요)]
          ['이규래','10400',96.1,'none',75.2,87.3]]    # [이름, 학번, 수학점수, 빈공간(삭제 필요), 국어점수, 정보점수]

for i in range(len(student)):
  student[i].remove("none")
  a= student[i][2] + student[i][3] + student[i][4]
  student[i].append(a)
  student[i].append(a/3)
  if a/3 >= 90:
    student.insert(student[i][2], 'A')
  elif a/3 >= 80:
    student.insert(student[i][2], 'B')
  elif a/3 >= 70:
    student.insert(student[i][2], 'C')
  else:
    student.insert(student[i][2], 'D')
print(student)