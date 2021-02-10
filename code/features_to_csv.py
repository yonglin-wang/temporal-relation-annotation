"""
Author Loewi
call features extraction functions on word pairs, vectorize features, and save extracted features to csv
"""
import feature_extraction as fx
import pandas as pd
from Event import Event


def extract_all_features(text, e1, e2):
    return fx.extract_pos_tag(text, e1, e2),\
           fx.extract_context_pos_tag(text, e1, e2),\
           fx.extract_str_distance(text, e1, e2),\
           fx.extract_modal_verbs(text, e1, e2),\
           fx.extract_temp_connectives(text, e1, e2),\
           fx.have_common_syn(e1, e2),\
           fx.have_common_der_form(e1, e2)



if __name__ == "__main__":
    data = pd.read_csv('./data/gold_standard.csv')
    df = pd.DataFrame(data, columns= ["text","fromSpan","fromVerb", "fromPOS", "toSpan", "toVerb","toPOS","relationship"])
 
    pos1_list, pos2_list, dis_list, mod_list, syn_list, derv_list = [], [], [], [], [], []
    before_1_list, after_1_list, before_2_list, after_2_list = [], [], [], [] 
    temp_before_list, temp_after_list, temp_since_list = [],[],[]
    rela_list = []

    for row in range(len(data)):
        print(row)
        text = df.loc[row,'text']
        e1 = Event(df.loc[row,'fromSpan'], df.loc[row,'fromVerb'], df.loc[row,'fromPOS'], text)
        e2 = Event(df.loc[row,'toSpan'], df.loc[row,'toVerb'], df.loc[row,'toPOS'], text)
        (pos1, pos2), (b1,a1,b2,a2), dis, mod, (b,a,s), syn, derv = extract_all_features(text, e1, e2)
        pos1_list.append(pos1)
        pos2_list.append(pos2)
        before_1_list.append(b1)
        after_1_list.append(a1)
        before_2_list.append(b2)
        after_2_list.append(a2)
        dis_list.append(dis)
        mod_list.append(mod)
        temp_before_list.append(b)
        temp_after_list.append(a)
        temp_since_list.append(s)
        syn_list.append(syn)
        derv_list.append(derv)
        rela_list.append(df.loc[row,'relationship'])
        
    df = pd.DataFrame({'POS1':pos1_list,
                       'POS2':pos2_list,
                       'BEFORE_1':before_1_list,
                       'AFTER_1':after_1_list,
                       'BEFORE_2':before_2_list,
                       'AFTER_2':after_2_list,
                       'DISTANCE':dis_list,
                       'MODAL':mod_list,
                       'TEMP_BEFORE':temp_before_list,
                       'TEMP_AFTER':temp_after_list,
                       'TEMP_SINCE':temp_since_list,
                       'SYN':syn_list,
                       'DERIVATION':derv_list,
                       'RELATION':rela_list
                       })
    df.to_csv('features.csv', index=False)
