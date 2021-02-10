"""
Author Yonglin Loewi
event object for representing a verb
"""
# import nltk
# nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize 

# valid_pos = {"VB", "VBD", "VBG", "VBN", "VBP", "VBZ"} # for validation if needed

class Event:

    def __init__(self, span, verb, pos, text):
        """
        inputs are all text strings
        """
        self.start, self.verb, self.pos = int(span.split('~')[0]), verb, pos
        self.index = self.set_idex(self.start, text)
        self.synset = self.set_synset(verb)
        self.derivational_form = self.set_derivational_form(verb)

    def get_start_position(self):
        return int(self.start)

    def get_end_position(self):
        return int(self.start) + len(self.text)

    def get_index(self):
        return self.index
    
    def get_verb(self):
        return self.verb

    def get_verb_category(self):
        return self.pos

    def get_synset(self):
        return self.synset

    def get_derivational_form(self):
        return self.derivational_form
    
    def set_idex(self, start, text):
        return len(word_tokenize(text[:start]))

    def set_synset(self, word):
        return set(l.name() for syn in wn.synsets(word) for l in syn.lemmas())  # return set() or None if empty?

    def set_derivational_form(self, word):
        lemmatizer = WordNetLemmatizer()
        return lemmatizer.lemmatize(word)


if __name__ == "__main__":

    test_words = {
                    "said",
                    "he"
                  }  # change this set to see how diff words perform
    text = 'Mr. Loeser said he was helping clients assess the kind of attacks they could expect in a hard-fought campaign.'
    for w in test_words:
        e = Event("11~15", w, "VBG",text)
        print("Synsets for word \'%s\': " % e.get_verb())
        print(e.get_synset())
        print("Derivational form for word \'%s\': %s" % (e.get_verb(), e.get_derivational_form()))