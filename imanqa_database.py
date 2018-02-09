# -*- coding: utf-8 -*-

import xlrd

questions = []
right_answers = []
wrong_answers = []
evidences = []
unique_questions = []
unique_evidences = []

rb = xlrd.open_workbook('QA.xlsx')
sheet = rb.sheet_by_index(0)
for rownum in range(sheet.nrows):
    row = sheet.row_values(rownum)
    for i in range(len(row)):
        if i == 0:
            questions.append(row[i])
        if i == 1:
            right_answers.append(row[i])
        if i == 2 or i == 3 or i == 4:
            wrong_answers.append(row[i])
        if i == 5:
            evidences.append(row[i])

if len(questions) != len(right_answers) and 3 * len(questions) != len(wrong_answers) and len(questions) != len(evidences) :
    print("array lengths are not equial")
    raise SystemExit

if '' in questions or '' in right_answers or '' in wrong_answers or '' in evidences:
    print("empty element")
    raise SystemExit

for i in range(len(questions)):
    if i == 0:
        unique_questions.append(questions[i])
        unique_evidences.append(evidences[i])
    else:
        if questions[i] != questions[i - 1]:
            unique_questions.append(questions[i])
            unique_evidences.append(evidences[i])

if __name__ == '__main__':
    print('Вопросы:')
    for i in questions:
        print(i)
    else:
        print()

    print('Правильные ответы:')
    for i in right_answers:
        print(i)
    else:
        print()

    print('Неправильные ответы:')
    for i in wrong_answers:
        print(i)
    else:
        print()

    print('Доводы:')
    for i in evidences:
        print(i)
    else:
        print()

    print('Уникальные вопросы:')
    for i in unique_questions:
        print(i)
    else:
        print()

    print('Ответы на уникальные вопросы:')
    for i in unique_evidences:
        print(i)
    else:
        print()
