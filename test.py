# -*- coding: utf-8 -*-

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
import database

Builder.load_string('''
<Test>:

    BoxLayout:
        orientation: 'vertical'
        padding: 8

        Label:
            id: question_num
            text: 'Вопрос x/y'

        Label:
            id: question
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
                id: answer_0
                text_size: self.size
                text: 'answer 0'

            CheckBox:
                group: 'answers'
                on_active:
                    root.answer_num = 1
                active: root.is_checkbox_1_active

            Label:
                id: answer_1
                text_size: self.size
                text: 'answer 1'

            CheckBox:
                group: 'answers'
                on_active:
                    root.answer_num = 2
                active: root.is_checkbox_2_active

            Label:
                id: answer_2
                text_size: self.size
                text: 'answer 2'

            CheckBox:
                group: 'answers'
                on_active:
                    root.answer_num = 3
                active: root.is_checkbox_3_active

            Label:
                id: answer_3
                text_size: self.size
                text: 'answer 3'

        Button:
            id: start_test
            text: 'Ответить'
            on_press: 
                root.confirm_answer()
''')


class Test(Screen):
    answer_num = -1
    question_num = -1
    question = StringProperty()
    is_checkbox_0_active = BooleanProperty(False)
    is_checkbox_1_active = BooleanProperty(False)
    is_checkbox_2_active = BooleanProperty(False)
    is_checkbox_3_active = BooleanProperty(False)

    def on_enter(self):
        self.next_question()

    def confirm_answer(self):
        if self.answer_num > -1:
            self.erase_checkboxes()
            self.next_question()
            print(self.answer_num)
            self.answer_num = -1

    def next_question(self):
        self.question_num += 1
        current_question = database.questions[self.question_num]
        self.question = current_question

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
