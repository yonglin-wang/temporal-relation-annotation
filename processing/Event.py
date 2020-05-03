"""
Author Yonglin
event object for representing a verb
"""

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet 

class Event:

    def __init__(self, xml_entry):
        """
        assume xml_entry has the format of
        id="V1" spans="7~14" text="reached" category="VBN"
        """
        self.verb_id, self.start, self.text, self.pos = self.get_id_start_text_cat(xml_entry)
        self.synset = None
        self.derivational_form = None

    

    def get_id_start_text_cat(self, xml_entry):
        pass

    def get_verb_id(self):
        return self.verb_id

    def get_start_position(self):
        return self.start

    def get_verb_text(self):
        return self.text

    def get_verb_category(self):
        return self.pos

    def get_synset(self):
        # TODO get synset from self.text
        return self.synset

    def get_derivational_form(self):
        # TODO get der form from self.text
        return self.derivational_form

    def set_synset(self):
        self.synset = set(l.name() for syn in wordnet.synsets(word) for l in syn.lemmas())

    def set_derivational_form(self, word):
        lemmatizer = WordNetLemmatizer()
        self.derivational_form = lemmatizer.lemmatize(word)

