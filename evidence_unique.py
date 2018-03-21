# -*- coding: utf-8 -*-

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import StringProperty

import globals
from database import database

Builder.load_string('''
<EvidenceUnique>:

    BoxLayout:
        orientation: 'vertical'
        padding:8
        
        ScrollView:
            Label:
                size_hint_y: None
                height: self.texture_size[1]
                text_size: self.width, None
                text: root.evidence_text
            
        Button:
            text: 'Назад'
            on_press: 
                root.manager.current = 'questions'
''')


class EvidenceUnique(Screen):
    evidence_text = StringProperty()

    def on_enter(self):
        self.evidence_text = database[globals.evidence_num]['evidence']
