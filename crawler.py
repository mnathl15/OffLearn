from bs4 import BeautifulSoup as bs
import requests, os, imp
topic = imp.load_source("topic", "./models/topic.py")

#acts as a search engine, returns status code
def search(text):
    html = requests.get("https://www.bing.com/search?q= " + text)
    page = bs(html.content,'html.parser')
    links = page.find_all('a')
    valid_links=[]
    link_number = 0
    for link in links:
        try:
            if(requests.get(link['href']).status_code==200):
                print(link['href'])
        except:
            pass
    print(links)

def getFile(filename):
    return "<p> Horray!! </p>"

def getFileNames():
    topicList = []
    folderList = os.listdir("data")
    for folder in folderList:
        newTopic = Topic()
        pageList = os.listdir("data/" + folder)
        newTopic.setName(folder)
        for page in pageList:
            newTopic.addPage(page)
        topicList.append(newTopic)
    return topicList

# from googlesearch import search 

# for url in search('Civil War', stop=5):
#     print(url)

