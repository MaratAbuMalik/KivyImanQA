# -*- coding: utf-8 -*-

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

import globals
from database import database, unique_questions

Builder.load_string('''
#:import ListItemButton kivy.uix.listview.ListItemButton
#:import ListAdapter kivy.adapters.listadapter.ListAdapter

<Questions>:
    pos_hint: {'center_x': .5, 'center_y': .5}
    do_default_tab: False

    BoxLayout:
        id: box_layout_id
        orientation: 'vertical'
        ListView:
            text_size: self.width, None
            id: list_view_id
            adapter:
                ListAdapter(
                data=[], 
                cls=ListItemButton)
''')


class Questions(Screen):
    def on_enter(self):
        self.ids['list_view_id'].adapter.bind(on_selection_change=self.click)
        for i in range(len(unique_questions)):
            self.add(str(i + 1) + '. ' + database[unique_questions[i]]['question'])

    def add(self, text):
        self.ids['list_view_id'].adapter.data.append(text)

    def click(self, *args):
        text = str(args[0].selection[0])
        pos1 = text.find('text=') + 5
        pos2 = text.find('.', pos1)
        globals.evidence_num = unique_questions[int(text[pos1:pos2]) - 1]
        self.manager.current = 'evidence_unique'
