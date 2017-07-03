from lxml import html, etree
import requests 
from StringIO import StringIO
import json


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
    for ele in listOfTemples:
        __click_on_temple_pages(ele.attrib['href'])


def __click_on_temple_pages(partial):
    tree =  __load_url(get_url_main_site() + partial)
    __get_list_of_specialties(tree)
    __get_address_information(tree)


def __get_list_of_specialties(tree):
    rawListOfSpecialties = tree.xpath('//*[@id="content"]/div/div[1]/ul/li[*]/a/span/text()')
    listOfData = []
    keyOfData = [] 
    for ele in rawListOfSpecialties:
        keyOfData.append("Specialties")
        listOfData.append(ele)
    totalValue = make_dic(keyOfData, listOfData) 
    print(repr_dict(totalValue)) 
    return totalValue 


def make_dic(keys, values):
    return dict((zip(keys, values)))


def __get_address_information(tree):
    rawBlockData = tree.xpath('//*[@id="content"]/div/section[5]/table')
    keys = []
    values = []
    for nodes in rawBlockData:
        for node in nodes:
            keys.append(node[0].text)
            values.append(node[1].text)
    totalValue = make_dic(keys, values) 
    print(repr_dict(totalValue))
    return totalValue 


def repr_dict(d):
        return '{%s}' % ',\n'.join("'%s': '%s'" % pair for pair in d.iteritems())


if __name__ == "__main__":
    __get_list_of_pages_tokyo()
