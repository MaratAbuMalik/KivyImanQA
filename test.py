# -*- coding: utf-8 -*-

from random import randrange

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
from database import database

import globals

Builder.load_string('''
<Test>:

    BoxLayout:
        orientation: 'vertical'
        padding: 8

        Label:
            text: 'Вопрос x/y'

        Label:
            text_size: self.size
            text: root.question

        GridLayout:
            padding: 8
            cols: 2

            CheckBox:
                group: 'answers'
                on_active:
                    root.answer_num = 0
                active: root.is_checkbox_0_active

            Label:
                text_size: self.size
                text: root.answer0

            CheckBox:
                group: 'answers'
                on_active:
                    root.answer_num = 1
                active: root.is_checkbox_1_active

            Label:
                text_size: self.size
                text: root.answer1

            CheckBox:
                group: 'answers'
                on_active:
                    root.answer_num = 2
                active: root.is_checkbox_2_active

            Label:
                text_size: self.size
                text: root.answer2

            CheckBox:
                group: 'answers'
                on_active:
                    root.answer_num = 3
                active: root.is_checkbox_3_active

            Label:
                text_size: self.size
                text: root.answer3

        Button:
            text: 'Ответить'
            on_press: 
                root.confirm_answer()
''')


class Test(Screen):
    is_checkbox_0_active = BooleanProperty(False)
    is_checkbox_1_active = BooleanProperty(False)
    is_checkbox_2_active = BooleanProperty(False)
    is_checkbox_3_active = BooleanProperty(False)
    question = StringProperty()
    answer0 = StringProperty()
    answer1 = StringProperty()
    answer2 = StringProperty()
    answer3 = StringProperty()

    def on_enter(self):
        globals.test_answers = []
        globals.test_questions = self.get_test_questions()
        self.erase_data()
        self.next_question()

    def get_test_questions(self):
        edges = [0]
        questions = []
        for i in range(1, globals.num_questions):
            edges.append(edges[i - 1] + len(database) // globals.num_questions)
        edges.append(len(database))

        for i in range(globals.num_questions):
            questions.append(randrange(edges[i], edges[i+1]))

        return questions

    def erase_data(self):
        self.answer_num = -1
        self.question_num = -1
        self.order = []

    def next_question(self):
        self.question_num += 1
        self.question = database[globals.test_questions[self.question_num]]['question']
        self.order = self.new_answers_order()
        self.fill_answers()

    def new_answers_order(self):
        order = list(range(globals.num_answers))
        for i in range(10):
            x = randrange(globals.num_answers)
            y = randrange(globals.num_answers)
            order[y], order[x] = order[x], order[y]
        print(order)
        return order

    def fill_answers(self):
        self.answer0 = database[globals.test_questions[self.question_num]]['answers'][self.order[0]]
        self.answer1 = database[globals.test_questions[self.question_num]]['answers'][self.order[1]]
        self.answer2 = database[globals.test_questions[self.question_num]]['answers'][self.order[2]]
        self.answer3 = database[globals.test_questions[self.question_num]]['answers'][self.order[3]]

    def confirm_answer(self):
        if self.answer_num > -1:
            self.erase_checkboxes()
            globals.test_answers.append({'question_num': globals.test_questions[
                self.question_num], 'answer_num': self.order[self.answer_num]})
            print(globals.test_answers)
            self.answer_num = -1
            if self.question_num == globals.num_questions - 1:
                self.manager.current = 'result'
                return
            self.next_question()

    # TODO: refactor erase_checkboxes
    def erase_checkboxes(self):
        if self.answer_num == 0:
            self.is_checkbox_0_active = not self.is_checkbox_0_active
            self.is_checkbox_0_active = not self.is_checkbox_0_active
        if self.answer_num == 1:
            self.is_checkbox_1_active = not self.is_checkbox_1_active
            self.is_checkbox_1_active = not self.is_checkbox_1_active
        if self.answer_num == 2:
            self.is_checkbox_2_active = not self.is_checkbox_2_active
            self.is_checkbox_2_active = not self.is_checkbox_2_active
        if self.answer_num == 3:
            self.is_checkbox_3_active = not self.is_checkbox_3_active
            self.is_checkbox_3_active = not self.is_checkbox_3_active
