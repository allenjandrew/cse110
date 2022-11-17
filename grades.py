grade_percent = float(input('\nPlease enter your grade percentage: '))

grade = 'F'
if grade_percent >= 90:
    grade = 'A'
elif grade_percent >= 80:
    grade = 'B'
elif grade_percent >= 70:
    grade = 'C'
elif grade_percent >= 60:
    grade = 'D'

sign = ''
if grade_percent % 10 >= 7 and grade not in ('A','F'):
    sign = '+'
elif grade_percent % 10 < 3 and grade != 'F':
    sign = '-'

print('\nGrade: ' + grade + sign)

if grade_percent >= 70:
    print('\nNice job! You passed the class!\n')
else:
    print('\nYou didn\'t pass. Try harder next time! You can do it!\n')
