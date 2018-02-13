# -*- coding: utf-8 -*-

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_string('''
<MainMenu>:

    BoxLayout:
        orientation: 'vertical'
        padding: 8

        Label:
            id: best_result
            text: 'best_result: x/y'

        Label:
            id: previous_result
            text: 'previous_result: x/y'

        Label:
            id: knowledge_evidence
            text_size: self.size
            text: 'ayasdah, hadis, ayah, hadis, ayah, hadis, ayah, hadis, ayah, hadis, ayah, hadis, ayah, hadis, ayah, hadis, ayah, hadis, ayah, hadis, ayah, hadis, ayah, hadis, ayah, hadis, ayah, hadis, ayah, hadis, ayah, hadis'

        Button:
            id: learn_questions
            text: 'Изучить вопросы'
            on_press: 
                root.manager.current = 'questions'

        Button:
            id: start_test
            text: 'Начать тест'
            on_press: 
                root.manager.current = 'test'
''')


class MainMenu(Screen):
    pass
