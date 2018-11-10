from bs4 import BeautifulSoup as bs
import requests, os, imp, requests
from googlesearch import search
topic = imp.load_source("topic", "./models/topic.py")

#acts as a search engine, returns status code
def searchInternet(query):
    querySize = 3
    rootDir = "templates"
    urlList = list(next(search(query, stop=5)) for _ in range(querySize))
    
    folderPath = "/".join([rootDir, query])
    if not os.path.exists(folderPath):
        os.mkdir(folderPath)

    # print(urlList)

    for url in urlList:

        if "youtube" not in url:
            
            rawHtml = str(requests.get(url).text.encode("utf-8"))
            filePath = "/".join([rootDir, query, getWebsite(url)]) + ".html" 
            file = open(filePath, "w")
            file.write(rawHtml)
            file.close()

def getWebsite(url):
    preIndex = url.index(".")+1
    url = url[preIndex:]
    postIndex = url.index(".")
    return url[:postIndex].capitalize()

# searchInternet("Halloween")

def getFile(filename):
    return "<p> Horray!! </p>"

def getFileNames():
    topicList = []
    folderList = os.listdir("templates")
    for folder in folderList:
        newTopic = topic.Topic()
        pageList = os.listdir("templates/" + folder)
        newTopic.setName(folder)
        for page in pageList:
            newTopic.addPage(page)
        topicList.append(newTopic)
        print(newTopic)
    return topicList 



# html = requests.get("https://www.bing.com/search?q= " + text)
# page = bs(html.content,'html.parser')
# links = page.find_all('a')
# valid_links=[]
# link_number = 0
# for link in links:
#     try:
#         if(requests.get(link['href']).status_code==200):
#             print(link['href'])
#     except:
#         pass