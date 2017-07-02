from lxml import html, etree
import requests 
from StringIO import StringIO


def __initialize_data():
    url = "https://hotokami.jp/area/tokyo/"
    r = requests.get(url)
    data = r.text
    print data
    return etree.parse(StringIO(data), etree.HTMLParser()) 


def __get_list_of_pages_tokyo():
    tree = __initialize_data() 
    listOfTemples = tree.xpath('//*[@id="content"]/div/section[*]/h3/a')
    for ele in listOfTemples:
        print ele.attrib['href']


def __click_on_temple_pages():
    pass


if __name__ == "__main__":
    __get_list_of_pages_tokyo()
