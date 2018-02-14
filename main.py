# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from main_menu import MainMenu
from questons import Questions
from evidence import Evidence
from test import Test


class MainApp(App):
    def build(self):
        screen_manager = ScreenManager()
        main_menu_screen = MainMenu(name='main_menu')
        questions_screen = Questions(name='questions')
        evidence_screen = Evidence(name='evidence')
        test_screen = Test(name='test')
        screen_manager.add_widget(main_menu_screen)
        screen_manager.add_widget(questions_screen)
        screen_manager.add_widget(evidence_screen)
        screen_manager.add_widget(test_screen)
        return screen_manager


if __name__ == '__main__':
    MainApp().run()
