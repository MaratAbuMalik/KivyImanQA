# -*- coding: utf-8 -*-

import pickle

with open('imanqa_database.pickle', 'rb') as f:
    database = pickle.load(f)
    unique_questions = pickle.load(f)
