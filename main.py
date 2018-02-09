#  -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from main_menu import MainMenu
from queston_list import QuestionList
from evidence import Evidence


class MainApp(App):
    def build(self):
        screen_manager = ScreenManager()
        main_menu_screen = MainMenu(name='main_menu')
        question_list_screen = QuestionList(name='question_list', screen_manager=screen_manager)
        evidence_screen = Evidence(name='evidence')
        screen_manager.add_widget(main_menu_screen)
        screen_manager.add_widget(question_list_screen)
        screen_manager.add_widget(evidence_screen)
        return screen_manager


if __name__ == '__main__':
    MainApp().run()
