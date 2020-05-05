"""
Author Loewi, Yonglin
extract 6 features from a given text string and two verbs
"""
# columns = ["article", "paragraph", "text", "E_id", "fromID", "fromText", "toID", "toText", "relationship",
#           "fromSpan", "fromVerb", "fromPOS", "toSpan", "toVerb", "toPOS"]
import pandas as pd
from nltk.tokenize import word_tokenize 
from nltk import pos_tag
from Event import Event
import collections
import numpy as np
# Event(span, verb, pos, text)
TAGS_INDEX = collections.defaultdict(int)
TAGS = ['CC', 'CD', 'DT', 'EX', 'FW', 'IN', 'JJ', 'JJR', 'JJS', 'LS', 'MD', 'NN', 'NNS', 'NNP', 'NNPS', 'PDT', 'POS', 'PRP', 'PRP$', 'RB', 'RBR', 'RBS', 'RP', 'TO', 'UH', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WDT', 'WP', 'WP$', 'WRB']
for i, tag in enumerate(TAGS):
    TAGS_INDEX[tag] = i
TAGS_LEN = len(TAGS)
MODALS_INDEX = collections.defaultdict(int)
MODALS = ['will', 'would', 'can', 'could', 'may', 'might']
for i, modal in enumerate(MODALS):
    MODALS_INDEX[modal] = i
MODALS_LEN = len(MODALS)
TEMPS_INDEX = collections.defaultdict(int)
TEMPS = ['before', 'after', 'since']
for i, temp in enumerate(TEMPS):
    TEMPS_INDEX[temp] = i
TEMPS_LEN = len(TEMPS)

def extract_pos_tag(text, e1, e2):
    return e1.get_verb_category(), e2.get_verb_category()
    
def extract_context_pos_tag(text, e1, e2):
    """
    return count vector of a list of part-of-speech (POS) tags from each individual verb and from its neighboring three words.
    """
    tokens = word_tokenize(text)
    tagged_words = pos_tag(tokens)
    idx1, idx2 = e1.get_index(), e2.get_index()
    before_1, after_1, before_2, after_2 = [], [], [], []
    for idx in [idx1, idx2]:
        tags_before = tagged_words[idx-1 if idx-1 >=0 else 0 : idx]
        tags_after = tagged_words[idx+1 : idx+2 if idx+2<len(tokens) else len(tokens)]
        if idx == idx1:
            before_1 = [tag for _, tag in tags_before][0] if [tag for _, tag in tags_before] else '<S>'# tags before the verb
            after_1 = [tag for _, tag in tags_after][0] # tags after the verb
        else:
            before_2 = [tag for _, tag in tags_before][0]# tags before the verb
            after_2 = [tag for _, tag in tags_after][0]# tags after the verb    

    
    return before_1, after_1, before_2, after_2

def extract_str_distance(text, e1, e2):
    """
    return an int of the distance between them in terms of the number of tokens.
    """
    return e2.get_index() - e1.get_index()

def extract_modal_verbs(text, e1, e2):
    """
    return count of the modal verbs between the event mention (i.e., will, would, can, could, may and might).
    """
    count=0
    modals = set(MODALS)
    tokens = word_tokenize(text)
    intervals = tokens[e1.get_index()+1: e2.get_index()]
    for word in intervals:
        if word in modals:
            count+=1
    return count

def extract_temp_connectives(text, e1, e2):
    """
    return count vector of a list of temporal connectives between the event mentions (e.g., before, after and since)
    """
    tmp = []
    temps = set(TEMPS)
    tokens = word_tokenize(text)
    intervals = tokens[e1.get_index()+1: e2.get_index()]
    for word in intervals:
        if word in temps:
            tmp.append(word)
            
    res = np.zeros((1,TEMPS_LEN))
    counter = collections.Counter(tmp)
    for t in tmp:
        idx = TEMPS_INDEX[t]
        res[0, idx] = counter[t]
    before, after, since = res[0][0], res[0][1], res[0][2]
    return before, after, since

def have_common_syn(e1, e2):
    """
    return either 0 or 1 of whether the two verbs have a common synonym from their synsets in WordNet (Fellbaum, 1998)
    """
    syns1, syns2 = e1.get_synset(), e2.get_synset()
    return 0 if not len(syns1.intersection(syns2)) else 1

def have_common_der_form(e1, e2):
    """
    return either 0 or 1 of whether the input event mentions have a common derivational form derived from WordNet.
    """
    derv1, derv2 = e1.get_derivational_form(), e2.get_derivational_form()
    return 1 if derv1 == derv2 else 0

if __name__ == "__main__":

    data = pd.read_csv('./data/gold_standard.csv')
    print(len(data))
    df = pd.DataFrame(data, columns= ['text',"fromSpan","fromVerb", "fromPOS", "toSpan", "toVerb","toPOS"])
    row = 75
    text = df.loc[row,'text']
    e1 = Event(df.loc[row,'fromSpan'], df.loc[row,'fromVerb'], df.loc[row,'fromPOS'], text)
    e2 = Event(df.loc[row,'toSpan'], df.loc[row,'toVerb'], df.loc[row,'toPOS'], text)
    print(extract_pos_tag(text, e1, e2))
    print(have_common_der_form(e1, e2))