#!/usr/bin/env python
# coding: utf-8
import inflect
import re
import codecs

source_file = "../data/5-Serotonin2020.txt"


def open_unicode_file(name):
    f =  codecs.open(name, encoding='utf-8', mode='r').read()
    return f.split("\n")


def get_regex(name):
    py_name = name.split("/")[-1].replace(".txt", ".py")
    py_file = codecs.open(py_name, encoding='utf-8', mode='w')
    f = open_unicode_file(name)
    p = inflect.engine()
    counter = 0
    ptrns = set()
    py_file.write("#!/usr/bin/python\n# -*- coding: utf-8 -*-\n")
    varname ="pats=["
    for l in f:
        pattern = "ur\"(?i)" + r"\b"
        wrds = re.compile("-|\s").split(l)
        pattern += "(-|\s+)?".join(list(map(lambda x : "(" + p.plural(x.lower()) + "|" + x.lower() + ")", wrds))) + r"\b" + "\""
        pat = create_umlaut_variants(pattern)
        if len(pat) <= 15 or pat in ptrns:
            continue   
        ptrns.add(pat)
        varname += pat + ",\n"
        counter+=1
    varname = varname[:-2] + "]"
    py_file.write(varname)
    py_file.close()


umlautDictionary = {
                    u'ä': u'(ä|ae|[a-z])',
                    u'ö': u'(ö|oe|[a-z])',
                    u'ü': u'(ü|ue|[a-z])'
                    }


def create_umlaut_variants(pattern):
    for k,v in umlautDictionary.iteritems():

        pattern = pattern.replace(k,v)
    return pattern


def match(s, compiled):
    matches = []
    i = 0
    for comp in compiled:
        i += 1
        if(comp.search(s)):
            matches.append((i, comp.pattern))
    return matches


def get_all_species():
    data = codecs.open(source_file, encoding='utf-8', mode='r')
    f = codecs.open("regex_data/RegexTextFiles/species.txt", encoding='utf-8', mode='w')
    compiled = list(map(lambda x : re.compile(x), animals.pats))
    count = 0
    for l in data:
        res = match(l,compiled)
        count += 1
        if count % 100 == 0:
            print(count)
        if len(res) > 0:
            f.write("\n".join(list(map(lambda x : str(x), res))) + "\n")


def get_all_regions():
    data = codecs.open(source_file, encoding='utf-8', mode='r')
    f = codecs.open("regex_data/RegexTextFiles/regions.txt", encoding='utf-8', mode='w')
    compiled = list(map(lambda x : re.compile(x), br.pats))
    count = 0
    found = set()
    for l in data:
        res = match(l,compiled)
        count += 1
        if count % 100 == 0:
            print(count)
        if len(res) > 0:
            ls = list(map(lambda x : str(x), res))
            for st in ls:
                found.add(st)
    for s in found:
        f.write(s + "\n")


def get_files(name):
    py_name = name.split("/")[-1].replace(".txt", ".py")
    py_file = codecs.open(py_name, encoding='utf-8', mode='w')
    f = open_unicode_file(name)
    
    p1 = re.compile(u'α')
    pattern = re.compile('[^a-zA-Z0-9\s?]+')
    counter = 0
    ptrns = set()
    py_file.write("#!/usr/bin/python\n# -*- coding: utf-8 -*-\n")
    varname =r"strs=["
    for l in f:
        st = "ur\"" + r"\b"
        st += pattern.sub('', p1.sub('a',l).replace("-", r" ?")).strip()
        if len(st) <= 5 or st in ptrns:
            continue
        ptrns.add(st)
        varname += st + "\",\n"
        counter+=1
    varname = varname[:-2] + "]"
    py_file.write(varname.lower())
    py_file.close()


def main():
    import os
    print(os.chdir('regex_data'))
    get_files("RawTextFiles/Methods.txt")
    get_files("RawTextFiles/Serotonin_Topics.txt")
    get_files("RawTextFiles/Species.txt")
    get_files("RawTextFiles/Brain_Regions.txt")
    get_regex("RawTextFiles/Species.txt")
    get_regex("RawTextFiles/Brain_Regions.txt")


if __name__ == "__main__":
    main()

