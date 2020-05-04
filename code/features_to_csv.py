"""
Author Loewi
call features extraction functions on word pairs, vectorize features, and save extracted features to csv
"""
import feature_extraction as fx
import pandas as pd
from Event import Event


def extract_all_features(text, e1, e2):
    return fx.extract_pos_tag(text, e1, e2),\
           fx.extract_str_distance(text, e1, e2),\
           fx.extract_modal_verbs(text, e1, e2),\
           fx.extract_temp_connectives(text, e1, e2),\
           fx.have_common_syn(e1, e2),\
           fx.have_common_der_form(e1, e2)



if __name__ == "__main__":
    data = pd.read_csv('./data/gold_standard.csv')
    df = pd.DataFrame(data, columns= ["text","fromSpan","fromVerb", "fromPOS", "toSpan", "toVerb","toPOS","relationship"])
 
    pos_list, dis_list, mod_list, temp_list, syn_list, derv_list = [], [], [], [], [], []
    rela_list = []

    for row in range(len(data)):
        print(row)
        text = df.loc[row,'text']
        e1 = Event(df.loc[row,'fromSpan'], df.loc[row,'fromVerb'], df.loc[row,'fromPOS'], text)
        e2 = Event(df.loc[row,'toSpan'], df.loc[row,'toVerb'], df.loc[row,'toPOS'], text)
        pos, dis, mod, temp, syn, derv = extract_all_features(text, e1, e2)
        pos_list.append(pos)
        dis_list.append(dis)
        mod_list.append(mod)
        temp_list.append(temp)
        syn_list.append(syn)
        derv_list.append(derv)
        rela_list.append(df.loc[row,'relationship'])
        
    df = pd.DataFrame({'POS':pos_list,
                       'DISTANCE':dis_list,
                       'MODAL':mod_list,
                       'TEMP':temp_list,
                       'SYN':syn_list,
                       'DERIVATION':derv_list,
                       'RELATION': rela_list
                       })
    df.to_csv('features.csv', index=False)
