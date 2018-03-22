# -*- coding: utf-8 -*-

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import StringProperty

import globals

Builder.load_string('''
<Result>:

    BoxLayout:
        orientation: 'vertical'
        padding: 8

        Label:
            text: root.mark_text

        Button:
            text: 'Главное меню'
            on_press: 
                root.manager.current = 'main_menu'

        Button:
            text: 'Мои ответы'
            on_press: 
                root.manager.current = 'answers'
''')


class Result(Screen):
    mark_text = StringProperty()

    def on_enter(self):
        mark = 0
        for i in globals.test_answers:
            if not i['answer_num']:
                mark += 1
        self.mark_text = 'Ваша оценка: {0}/{1}'.format(mark, globals.num_questions)

