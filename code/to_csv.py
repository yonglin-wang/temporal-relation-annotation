"""
Fiona
"""
import os
from collections import defaultdict
import csv
import numpy as np

CLASSES = {"before": 0, "after": 1, "simultaneous": 2, 'vague': 3}

def to_csv(input):
    """
    from xml file to csv file
    :param input:
    :return:
    """

    # columns = ["article", "paragraph", "text", "E_id", "fromID", "fromText", "toID", "toText", "relationship",
    #           "fromSpan", "fromVerb", "fromPOS", "toSpan", "toVerb", "toPOS"]
    writelines = []
    for root, dirs, files in os.walk(input):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, "r") as f:
                line = f.readline()
                verbs = defaultdict(list)
                while line:
                    if line.startswith("<TEXT>"):
                        text = line.replace("<TEXT><![CDATA[", "").replace("]]></TEXT>", "")
                    if line.startswith("<VERB"):
                        line = line.replace("<VERB ", "").replace(" />", "").strip()
                        pairs = line.split()
                        id = pairs[0].split("=")[1].replace("\"", "")
                        for pair in pairs[1:]:
                            words = pair.split("=")
                            verbs[id].append(words[1].replace("\"", ""))
                    if line.startswith("<EVENT"):
                        writeline = [root, file, text]
                        line = line.replace("<EVENT_ORDER ", "").replace("/>", "").strip()
                        pairs = line.split()
                        if len(pairs) != 6:
                            continue
                        for pair in pairs:
                            words = pair.split("=")
                            writeline.append(words[1].replace("\"", ""))
                        if writeline[4] in verbs:
                            for item in verbs[writeline[4]]:
                                writeline.append(item)
                        else:
                            writeline.extend([" "]*3)
                        if writeline[6] in verbs:
                            for item in verbs[writeline[6]]:
                                writeline.append(item)
                        else:
                            writeline.extend([" "]*3)
                        writelines.append(writeline)
                    line = f.readline()
                # print(verbs)
    # print(verb_dict)
    with open(input+".csv", "w") as f:
        writer = csv.writer(f)
        # writer.writerow(columns)
        for line in writelines:
            writer.writerow(line)

    return input+".csv"

def compare(file1, file2):
    """
    compare the different annotation relationships between file1 and file2
    :param file1:
    :param file2:
    :return:
    """
    dict1 = toDict(file1)
    dict2 = toDict(file2)
    same = []
    diff = []
    result = np.zeros((4, 4))
    for para, e_ids in dict1.items():
        for e_id, data in e_ids.items():
            relation1 = data[8]
            relation2 = dict2[para][e_id][8]
            if relation1 == " " or relation2 == " ":
                continue
            if relation1 != relation2:
                data.append(relation2)
                diff.append(data)
            else:
                same.append(data)
            result[CLASSES[relation1]][CLASSES[relation2]] += 1

    with open("same.csv", "w") as f:
        writer = csv.writer(f)
        for line in same:
            writer.writerow(line)

    with open("diff.csv", "w") as f:
        writer = csv.writer(f)
        for line in diff:
            writer.writerow(line)

    return result

def toDict(file):
    """
    from csv to Dict
    :param file1:
    :return:
    """
    article = defaultdict(dict)
    with open(file, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            article[row[1]][row[3]] = row
    return article


if __name__ == "__main__":
    file1 = to_csv("Jeff_YFLNYT_001")
    file2 = to_csv("Jonne_YFLNYT_001")
    print(compare(file1, file2))