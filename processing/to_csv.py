'''
Fiona
'''
import os
from collections import defaultdict
import csv

def to_csv(input):
    """
    from xml file to csv file
    :param input:
    :return:
    """

    # columns = ["article", "paragraph", "text", "E_id", "fromID", "fromText", "toID", "toText", "relationship",
    #           "fromSpan", "fromVerb", "fromPOS", "toSpan", "toVerb", "toPOS"]
    verb_dict = defaultdict(list)  # key: verbId; value: list [ span, text, category]
    writelines = []
    for root, dirs, files in os.walk(input):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, "r") as f:
                line = f.readline()
                while line:
                    if line.startswith("<TEXT>"):
                        text = line.replace("<TEXT><![CDATA[", "").replace("]]></TEXT>", "")
                    if line.startswith("<VERB"):
                        line = line.replace("<VERB ", "").replace(" />", "")
                        pairs = line.split()
                        id = pairs[0].split("=")[1]
                        for pair in pairs[1:]:
                            words = pair.split("=")
                            verb_dict[id].append(words[1].replace("\"", ""))
                    if line.startswith("<EVENT"):
                        writeline = [root, file, text]
                        line = line.replace("<EVENT_ORDER ", "").replace(" />", "")
                        pairs = line.split()
                        for pair in pairs:
                            words = pair.split("=")
                            writeline.append(words[1].replace("\"", ""))
                        for item in verb_dict[writeline[4]]:
                            writeline.append(item)
                        for item in verb_dict[writeline[6]]:
                            writeline.append(item)
                        writelines.append(writeline)
                    line = f.readline()

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
    same = "same.csv"
    diff = "diff.csv"

    for para, e_id in dict1:
        relation = e_id

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
