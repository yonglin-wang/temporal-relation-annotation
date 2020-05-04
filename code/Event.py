"""
Author Yonglin
event object for representing a verb
"""

import nltk
# nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn

# valid_pos = {"VB", "VBD", "VBG", "VBN", "VBP", "VBZ"} # for validation if needed

class Event:

    def __init__(self, verb_id, start, text, pos):
        """
        inputs are all text strings
        """
        self.verb_id, self.start, self.text, self.pos = verb_id, int(start), text, pos
        self.synset = self.set_synset(text)
        self.derivational_form = self.set_derivational_form(text)

    def get_verb_id(self):
        return self.verb_id

    def get_start_position(self):
        return int(self.start)

    def get_end_position(self):
        return int(self.start) + len(self.text)

    def get_verb_text(self):
        return self.text

    def get_verb_category(self):
        return self.pos

    def get_synset(self):
        return self.synset

    def get_derivational_form(self):
        return self.derivational_form

    def set_synset(self, word):
        return set(l.name() for syn in wn.synsets(word) for l in syn.lemmas())  # return set() or None if empty?

    def set_derivational_form(self, word):
        lemmatizer = WordNetLemmatizer()
        return lemmatizer.lemmatize(word)


if __name__ == "__main__":

    test_words = {
                    "find",
                    "asefajiog"
                  }  # change this set to see how diff words perform

    for w in test_words:
        e = Event("V3", "2", w, "VBG")
        print("Synsets for word \'%s\': " % e.get_verb_text())
        print(e.get_synset())
        print("Derivational form for word \'%s\': %s" % (e.get_verb_text(), e.get_derivational_form()))