# -*- coding: utf-8 -*-

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import StringProperty

import globals
from database import unique_evidences

Builder.load_string('''
<EvidenceUnique>:
    ScrollView:
        Label:
            padding: [8, 8]
            size_hint_y: None
            height: self.texture_size[1]
            text_size: self.width, None
            text: root.evidence_text

''')


class EvidenceUnique(Screen):
    evidence_text = StringProperty()

    # on_enter, on_pre_leave, on_leave
    def on_enter(self):
        self.evidence_text = unique_evidences[globals.evidence_num]