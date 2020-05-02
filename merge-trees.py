import pandas as pd
import cssselect
import click
import lxml.etree as etree
import pickle
import sys

def construct_df(event_order_attribs, cols):
    values = {c: [] for c in cols}
    for eoa in event_order_attribs:
        for c in cols:
            values[c].append(eoa.get(c, ""))
    df = pd.DataFrame(values)
    return df
def get_tree(path):
    with open(path, 'r') as f: tree_str = f.read()

    tree = etree.fromstring(bytes(tree_str, 
                                  encoding='utf-8'))

    return tree

def get_event_orders(tree):
    eos = tree.cssselect("EVENT_ORDER")
    return [eo.attrib for eo in eos]

def get_relationship(joined_df, eid):
    return joined_df.set_index('id')\
                    .loc[eid]\
                    .relationship


@click.command()
@click.option('--unannotated-xml-path', required=True)
@click.option('--annotated-xml-path', required=True)
@click.option('--output-path', required=False)
def main(unannotated_xml_path, annotated_xml_path, output_path):

    unannotated_tree = get_tree(unannotated_xml_path)
    annotated_tree = get_tree(annotated_xml_path)

    unannotated_event_orders = get_event_orders(unannotated_tree)
    annotated_event_orders = get_event_orders(annotated_tree)

    cols = ['id', 'fromID', 'fromText', 'toID', 'toText', 'relationship']
    unannotated_df = construct_df(unannotated_event_orders, cols)
    annotated_df = construct_df(annotated_event_orders, cols)

    ix_cols = ['id', 'fromID', 'fromText', 'toID', 'toText']
    joined = unannotated_df.drop('relationship', 1)\
                        .merge(annotated_df, on=ix_cols)
    
    for ueo in unannotated_event_orders:
        r = get_relationship(joined, ueo['id'])
        ueo['relationship'] = r
    
    # maybe the tree is annotated
    unannotated_tree\
            .getroottree()\
            .write(output_path, 
                   pretty_print=True)

if __name__ == '__main__':
    main()
