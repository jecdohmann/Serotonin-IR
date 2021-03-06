#!/usr/bin/env python
# coding: utf-8

# In[1]:


from os import listdir
from os.path import isfile, join
import codecs
from file_types import ParseObject
import pickle as pkl
import time
from extraction import extract_topics, extract_species, extract_regions, extract_raw_text_methods, \
    extract_year, extract_methods, extract_receptor


def open_unicode_file(name):
    f = codecs.open(name, encoding='utf-8', mode='r').read()
    return f


def create_objs():
    count = 0
    mypath = "../data/subfiles"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    timers = [0] * 9
    for fname in onlyfiles:
        count += 1
        if count % 10 == 0:
            print(str(count) + " " + str(timers))
            timers = [0] * 9
        loaded_file = open_unicode_file(mypath + "/" + fname)

        try:
            parse = ParseObject()
            t0 = time.time()
            parse.topics = extract_topics(loaded_file)
            t1 = time.time()
            timers[0] += t1 - t0
            parse.species = extract_species(loaded_file)
            t2 = time.time()
            timers[1] += t2 - t1
            parse.regions = extract_regions(loaded_file)
            t3 = time.time()
            timers[2] += t3 - t2
            parse.raw_text_methods = extract_raw_text_methods(loaded_file)
            t4 = time.time()
            timers[3] += t4 - t3
            parse.year = extract_year(loaded_file)
            t5 = time.time()
            timers[4] += t5 - t4
            parse.methods = extract_methods(loaded_file)
            t6 = time.time()
            timers[5] += t6 - t5
            parse.receptors = extract_receptor(loaded_file)
            t7 = time.time()
            timers[6] += t7 - t6
            pkl.dump(parse, open("../data/pkls/" + fname.replace(".txt", ".p"), "wb"))
            t8 = time.time()
            timers[7] += t8 - t7
        except:
            print(fname)


def print_csv():
    count = 0
    mypath = "../data/pkls"
    csv = open("../results_test.csv", "w+")
    csv.write("Year,Receptor,Species,Methods,Raw_Text_Methods,Brain_Regions,Topic_Spec\n")

    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    for fname in onlyfiles:
        count += 1
        if count % 100 == 0:
            print(count)
        obj = pkl.load(open(mypath + "/" + fname, 'rb'))

        obj.species = remove_commas(obj.species)
        obj.raw_text_methods = remove_commas(obj.raw_text_methods)
        obj.regions = remove_commas(obj.regions)
        obj.topics = remove_commas(obj.topics)

        line = ""
        line += obj.year + ","
        line += ';'.join([x for x, y, z in obj.receptors]) + ","
        line += ';'.join(obj.species) + ","
        line += ';'.join(obj.methods) + ","
        line += ';'.join(obj.raw_text_methods) + ","
        line += ';'.join(obj.regions) + ","
        line += ';'.join(obj.topics) + ",\n"
        csv.write(line)


def remove_commas(st):
    new_st = set()
    for element in st:
        new_str = ''
        for char in element:
            if char == ',':
                char = ''
            new_str += char
        new_st.add(new_str)
    return new_st


def create_parse(ld):
    parse = ParseObject()
    parse.receptors = remove_commas(parse_receptors(ld))

    parse.topics = remove_commas(extract_topics(ld))

    parse.species = remove_commas(extract_species(ld))

    parse.regions = remove_commas(extract_regions(ld))

    parse.raw_text_methods = remove_commas(extract_raw_text_methods(ld))

    parse.year = remove_commas(extract_year(ld))

    parse.methods = remove_commas(extract_methods(ld))

    return parse


def parse_receptors(ld):
    return extract_receptor(ld, True)


if __name__ == "__main__":
    # create_objs()
    print_csv()
