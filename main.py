# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from main_menu import MainMenu
from questons import Questions
from evidence_unique import EvidenceUnique
from test import Test
from result import Result
from answers import Answers
from evidence import Evidence


class MainApp(App):
    def build(self):
        screen_manager = ScreenManager()
        main_menu_screen = MainMenu(name='main_menu')
        questions_screen = Questions(name='questions')
        evidence_unique_screen = EvidenceUnique(name='evidence_unique')
        test_screen = Test(name='test')
        result_screen = Result(name='result')
        answers_screen = Answers(name='answers')
        evidence_screen = Evidence(name='evidence')
        screen_manager.add_widget(main_menu_screen)
        screen_manager.add_widget(questions_screen)
        screen_manager.add_widget(evidence_unique_screen)
        screen_manager.add_widget(test_screen)
        screen_manager.add_widget(result_screen)
        screen_manager.add_widget(answers_screen)
        screen_manager.add_widget(evidence_screen)
        return screen_manager


if __name__ == '__main__':
    MainApp().run()
