"""
Author Yonglin
process all .xml data in corpus/, generate a dictionary:
{para_ID: {text: String, pairs: [(v1, v2, rel)]}}

and dump it to data/
"""

import pickle

corpus_dir = "corpus/"
save_dir = "data/corpus_dict.pkl"

if __name__ == "__main__":
    pass