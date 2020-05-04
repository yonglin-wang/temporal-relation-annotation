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

TAGS = ['CC', 'CD', 'DT', 'EX', 'FW', 'IN', 'JJ', 'JJR', 'JJS', 'LS', 'MD', 'NN', 'NNS', 'NNP', 'NNPS', 'PDT', 'POS', 'PRP', 'PRP$', 'RB', 'RBR', 'RBS', 'RP', 'TO', 'UH', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WDT', 'WP', 'WP$', 'WRB']
MODALS = ['will', 'would', 'can', 'could', 'may', 'might']
TEMPS = ['before', 'after', 'since']

def extract_pos_tag(text, e1, e2):
    """
    return a list of part-of-speech (POS) tags from each individual verb and from its neighboring three words.
    """
    tokens = word_tokenize(text)
    tagged_words = pos_tag(tokens)
    idx1, idx2 = e1.get_index(), e2.get_index()
    pos_list = []
    for idx in [idx1, idx2]:
        tags_before = tagged_words[idx-3 if idx-3 >=0 else 0 : idx]
        tags_after = tagged_words[idx+1 : idx+4 if idx+4<len(tokens) else len(tokens)]
        pos_list.extend([tag for _, tag in tags_before]) # tags before the verb
        pos_list.extend([tag for _, tag in tags_after]) # tags after the verb
    return pos_list

def extract_str_distance(text, e1, e2):
    """
    return an int of the distance between them in terms of the number of tokens.
    """
    return e2.get_index() - e1.get_index()

def extract_modal_verbs(text, e1, e2):
    """
    return a list of the modal verbs between the event mention (i.e., will, would, can, could, may and might).
    """
    res = []
    modals = set(MODALS)
    tokens = word_tokenize(text)
    intervals = tokens[e1.get_index()+1: e2.get_index()]
    for word in intervals:
        if word in modals:
            res.append(word)
    return res

def extract_temp_connectives(text, e1, e2):
    """
    return a list of temporal connectives between the event mentions (e.g., before, after and since)
    """
    res = []
    temps = set(TEMPS)
    tokens = word_tokenize(text)
    intervals = tokens[e1.get_index()+1: e2.get_index()]
    for word in intervals:
        if word in temps:
            res.append(word)
    return res

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
    df = pd.DataFrame(data, columns= ['text',"fromSpan","fromVerb", "fromPOS", "toSpan", "toVerb","toPOS"])
    row = 75
    text = df.loc[row,'text']
    e1 = Event(df.loc[row,'fromSpan'], df.loc[row,'fromVerb'], df.loc[row,'fromPOS'], text)
    e2 = Event(df.loc[row,'toSpan'], df.loc[row,'toVerb'], df.loc[row,'toPOS'], text)
    print(extract_pos_tag(text, e1, e2))
    print(have_common_der_form(e1, e2))