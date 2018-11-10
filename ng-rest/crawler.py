from bs4 import BeautifulSoup as bs
import requests, os, imp, pdfkit
from googlesearch import search
topic = imp.load_source("topic", "./models/topic.py")
from flask import send_file

#acts as a search engine, returns status code
def searchInternet(query):
    querySize = 3
    rootDir = "data"
    urlList = list(next(search(query, stop=5)) for _ in range(querySize))
    
    folderPath = "/".join([rootDir, query])
    if not os.path.exists(folderPath):
        os.mkdir(folderPath)


    for url in urlList:

        filePath = "/".join([rootDir, query, getWebsite(url)]) + ".pdf" 
        path_wkthmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
        pdfkit.from_url(url, filePath, configuration=config)

def getWebsite(url):
    preIndex = url.index(".")+1
    url = url[preIndex:]
    postIndex = url.index(".")
    return url[:postIndex].capitalize()

def getFileNames():
    topicList = []
    folderList = os.listdir("data")
    for folder in folderList:
        newTopic = topic.Topic()
        pageList = os.listdir("data/" + folder)
        newTopic.setName(folder)
        for page in pageList:
            page = os.path.abspath(page)
            newTopic.addPage(os.path.abspath(page))
        topicList.append(newTopic)
        print(newTopic)
    return topicList 

getFileNames()

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