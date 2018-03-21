# -*- coding: utf-8 -*-
from random import randrange

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import StringProperty

Builder.load_string('''
<MainMenu>:

    BoxLayout:
        orientation: 'vertical'
        padding: 8

        Label:
            text: 'best_result: x/y'

        Label:
            text: 'previous_result: x/y'

        Label:
            text_size: self.size
            text: root.knowledge_evidence

        Button:
            text: 'Изучить вопросы'
            on_press: 
                root.manager.current = 'questions'

        Button:
            text: 'Начать тест'
            on_press: 
                root.manager.current = 'test'
''')


class MainMenu(Screen):
    knowledge_evidence = StringProperty()
    knowledge_evidences = [
        '«И говори: “Господь мой, прибавь мне знания”»\n(Та ха 20:114)',
        'Пророк (мир ему и благословение Аллаха) сказал:\n«Достоинство знания выше, '
        'чем достоинство поклонения, а в основе религии лежит благочестие»\n(аль-Хаким, '
        'аль-Баззар)',
        'Посланник Аллаха (да благословит его Аллах и приветствует) сказал:\n«Кто пришёл в мою '
        'мечеть, желая обучиться благому или обучить благому, тот подобен муджахиду на пути '
        'Аллаха»\n(Ахмад, Ибн Маджах)',
        'Посланник Аллаха (мир ему и благословение Аллаха) сказал:\n«Кто пришел в мечеть, '
        'желая обучиться благому или обучить благому, тому запишется награда человека, '
        'совершившего полноценный Хадж»\n(ат-Табарани)',
        'Пророк (мир ему и благословение Аллаха) сказал:\n«Тот, кто вышел на пути поиска знаний, '
        'находится на пути Аллаха, пока не вернется»\n(ат-Тирмизи, ат-Табарани)'
    ]

    def on_enter(self):
        self.knowledge_evidence = self.knowledge_evidences[randrange(len(self.knowledge_evidences))]
