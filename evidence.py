#  -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Label
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty, StringProperty

import globals
from imanqa_database import unique_evidences

Builder.load_string('''
<Evidence>:
    ScrollView:
        Label:
            padding: [8, 8]
            size_hint_y: None
            height: self.texture_size[1]
            text_size: self.width, None
            text: root.evidence_text

''')


class Evidence(Screen):
    evidence_text = StringProperty()

    # on_enter, on_pre_leave, on_leave
    def on_enter(self):
        self.evidence_text = unique_evidences[globals.MY_NUMBER]
