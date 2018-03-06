# -*- coding: utf-8 -*-

import xlrd

test_database = []
unique_questions = [0]


def parce_questions():
    questions = []
    right_answers = []
    wrong_answers = []
    evidences = []

    rb = xlrd.open_workbook('QA.xlsx')
    sheet = rb.sheet_by_index(0)
    for rownum in range(sheet.nrows):
        row = sheet.row_values(rownum)
        test_unit = dict()
        test_unit['answers'] = []
        for i in range(len(row)):
            if i == 0:
                questions.append(row[i])
                test_unit['question'] = row[i]
            if i == 1:
                right_answers.append(row[i])
                test_unit['answers'].append(row[i])
            if i == 2 or i == 3 or i == 4:
                wrong_answers.append(row[i])
                test_unit['answers'].append(row[i])
            if i == 5:
                evidences.append(row[i])
                test_unit['evidence'] = row[i]
        test_database.append(test_unit)

    if len(questions) != len(right_answers) and 3 * len(questions) != len(wrong_answers) and len(questions) != len(evidences) :
        print("array lengths are not equial")
        raise SystemExit

    if '' in questions or '' in right_answers or '' in wrong_answers or '' in evidences:
        print("empty element")
        raise SystemExit

    for i in range(1, len(questions)):
        if questions[i] != questions[i - 1]:
            unique_questions.append(i)


parce_questions()

if __name__ == '__main__':
    print('Вопросы:')
    for i in test_database:
        print(i['question'])
        print(i['answers'])
        print(i['evidence'])
        print()

    print('Уникальные вопросы:')
    for i in unique_questions:
        print(i)
