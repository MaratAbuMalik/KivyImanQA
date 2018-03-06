# -*- coding: utf-8 -*-

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

import globals
from database import test_database

Builder.load_string('''
#:import ListItemButton kivy.uix.listview.ListItemButton
#:import ListAdapter kivy.adapters.listadapter.ListAdapter
    
<Answers>:
    pos_hint: {'center_x': .5, 'center_y': .5}
    do_default_tab: False

    BoxLayout:
        id: box_layout_id
        orientation: 'vertical'
        ListView:
            text_size: self.size
            id: list_view_id
            width: 20
            height: 100
            adapter:
                ListAdapter(
                cls=ListItemButton,
                data=[])
        Button:
            text: 'Назад'
            on_press: 
                root.manager.current = 'result'
''')


class Answers(Screen):
    def on_enter(self):
        self.ids['list_view_id'].adapter.data = []
        self.ids['list_view_id'].adapter.bind(on_selection_change=self.click)
        for i in range(globals.questions_num):
            # answer = test_database[globals.test_answers[i]['question_num']]['answers'][
            # globals.test_answers[i]['answer_num']]
            if not globals.test_answers[i]['answer_num']:
                prefix = '+ '
                # postfix = '\nВаш ответ (правильный): ' + '\n' + answer
            else:
                prefix = '- '
                # postfix = '\nВаш ответ (неправильный): ' + '\n' + answer
            self.add(prefix + str(i + 1) + '. ' + test_database[globals.test_answers[i][
                'question_num']]['question'])

    def add(self, text):
        self.ids['list_view_id'].adapter.data.append(text)

    def click(self, *args):
        # для нормальной работы кнопки назад на экране доводов
        try:
            text = str(args[0].selection[0])
            pos1 = text.find('text=') + 7
            pos2 = text.find('.', pos1)
            globals.evidence_num = globals.test_answers[int(text[pos1:pos2]) - 1]['question_num']
            print(globals.evidence_num)
            self.manager.current = 'evidence'
        except:
            pass

