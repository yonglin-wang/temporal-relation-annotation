"""
Author Loewi, Yonglin
extract 6 features from a given text string and two verbs
"""



def extract_pos_tag(text, e1, e2):
    """
    return a list of part-of-speech (POS) tags from each individual verb and from its neighboring three words.
    """
    pass

def extract_str_distance(text, e1, e2):
    """
    return an int of the distance between them in terms of the number of tokens.
    """
    pass

def extract_modal_verbs(text, e1, e2):
    """
    return a list of the modal verbs between the event mention (i.e., will, would, can, could, may and might).
    """
    pass

def extract_temp_connectives(text, e1, e2):
    """
    return a list of temporal connectives between the event mentions (e.g., before, after and since)
    """
    pass

def have_common_syn(e1, e2):
    """
    return a boolean of whether the two verbs have a common synonym from their synsets in WordNet (Fellbaum, 1998)
    """
    pass

def have_common_der_form(e1, e2):
    """
    return a boolean of whether the input event mentions have a common derivational form derived from WordNet.
    """
    pass

if __name__ == "__main__":
    pass