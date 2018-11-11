from bs4 import BeautifulSoup as bs
import requests, os, imp, pdfkit
from googlesearch import search
topic = imp.load_source("topic", "./models/topic.py")
from flask import send_file
import regex as re

rootDir = "../data"

#makes sure there are no repeat websites
def filterURLS(urllist):
    occur_url={}
    for url in urllist:
        webDomain = getWebsite(url)

        try:
            occur_url[webDomain]  = occur_url[webDomain] + 1
        except:
            occur_url[webDomain] = 0



        if(occur_url[webDomain] > 1):
            urllist.remove(url)

        if webDomain == "":
            urllist.remove(url)

    return urllist

#acts as a search engine, returns status code
def searchInternet(query):
    querySize = 4

    searches = list(search(query,stop=querySize))[:querySize]
    urllist = filterURLS(searches)

    folderPath = "/".join([rootDir, query])
    if not os.path.exists(folderPath):
        os.mkdir(folderPath)

    #converts url to pdf
    for url in urllist:

        filePath = "/".join([rootDir, query, getWebsite(url)]) + ".pdf"
        try:
            path_wkthmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
            config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
            pdfkit.from_url(url, filePath, configuration=config)
        except:
            pass

#gets website name
def getWebsite(url):
    url = re.findall('(?<=\.)([^.]+)(?:\.(?:co\.uk|ac\.us|[^.]+(?:$|\n)))',url)
    return ''.join(url).capitalize()


def getFileNames():
    topicList = []
    folderList = os.listdir(rootDir)

    for folder in folderList:
        newTopic = topic.Topic()
        pageList = os.listdir(rootDir + "/" + folder)
        newTopic.setName(folder)

        for page in pageList:
            newTopic.addPage(folder + "/" + page)

        topicList.append(newTopic)

    

    return topicList 

# searchInternet("Android vs iOS")

