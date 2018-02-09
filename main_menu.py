#  -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Label
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty, StringProperty

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
                root.manager.current = 'question_list'

        Button:
            id: start_test
            text: 'start_test'
''')


class MainMenu(Screen):
    pass
