#!/usr/bin/env python
# -*- coding: utf-8 -*-


from lxml import html, etree
import requests 
from StringIO import StringIO
import json
from itertools import chain


def get_url_main_site():
    return "https://hotokami.jp"


def __load_url(url):
    r = requests.get(url)
    data = r.text
    return etree.parse(StringIO(data), etree.HTMLParser()) 


def __initialize_data():
    url = "https://hotokami.jp/area/tokyo/"
    return __load_url(url) 


def __get_list_of_pages_tokyo():
    tree = __initialize_data() 
    listOfTemples = tree.xpath('//*[@id="content"]/div/section[*]/h3/a')
    arrayOfData = []
    keyOfData = []
    i = 0
    for ele in listOfTemples:
        keyOfData.append("shrine"+str(i))
        beforeToPrint = __click_on_temple_pages(ele.attrib['href'])
        arrayOfData.append(repr_dict(beforeToPrint))
        i = i + 1 
    readyToPrint = make_dic(keyOfData, arrayOfData) 
    print_data_to_file(readyToPrint)
    
    
def print_data_to_file(readyToPrint):
    f1=open('./infoFile', 'w+')
    f1.write(json.dumps(readyToPrint))
    f1.write('\n')  
    f1.close()


def __click_on_temple_pages(partial): 
    tree =  __load_url(get_url_main_site() + partial)
    listOfSpe = __get_list_of_specialties(tree)
    listOfinfo =__get_address_information(tree)
    return(dict(chain(listOfSpe.items(), listOfinfo.items())))


def __get_list_of_specialties(tree):
    rawListOfSpecialties = tree.xpath('//*[@id="content"]/div/div[1]/ul/li[*]/a/span/text()')
    listOfData = []
    keyOfData = []
    i = 0
    for ele in rawListOfSpecialties:
        keyOfData.append("Specialties"+str(i))
        listOfData.append(ele)
        i = i + 1 
    totalValue = make_dic(keyOfData, listOfData) 
    return totalValue 


def make_dic(keys, values):
    return dict((zip(keys, values)))


def __get_address_information(tree):
    rawBlockData = tree.xpath('//*[@id="content"]/div/section[5]/table')
    keys = []
    values = []
    i = 0
    for nodes in rawBlockData:
        for node in nodes:
            keys.append("info"+str(i))
            values.append(node[1].text)
            i = i + 1
    totalValue = make_dic(keys, values) 
    return totalValue 


def repr_dict(d):
        return '{%s}' % ',\n'.join('"%s": "%s"' % pair for pair in d.iteritems())


if __name__ == "__main__":
    __get_list_of_pages_tokyo()
