# -*- coding: utf-8 -*-
student_scores = input("Input a list of student scores: ").split()

for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
  if student_scores[n] >= student_scores[0]:
      student_scores[0] = student_scores[n]
print(student_scores)

highest_score = str(student_scores[0])

print("The highest score in the class is: " + highest_score)