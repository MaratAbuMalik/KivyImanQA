from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

import globals
from imanqa_database import unique_questions

Builder.load_string('''
#:import ListItemButton kivy.uix.listview.ListItemButton
#:import ListAdapter kivy.adapters.listadapter.ListAdapter

<QuestionList>:
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


class QuestionList(Screen):
    def __init__(self, **kwargs):
        self.screen_manager = kwargs['screen_manager']
        del kwargs['screen_manager']
        super(QuestionList, self).__init__(**kwargs)

        self.ids['list_view_id'].adapter.bind(on_selection_change=self.click)
        for i in range(len(unique_questions)):
            self.add(str(i + 1) + '. ' + unique_questions[i])

    def add(self, text):
        self.ids['list_view_id'].adapter.data.append(text)

    def click(self, *args):
        text = str(args[0].selection[0])
        pos1 = text.find('text=') + 5
        pos2 = text.find('.', pos1)
        globals.MY_NUMBER = int(text[pos1:pos2]) - 1
        self.screen_manager.current = 'evidence'
