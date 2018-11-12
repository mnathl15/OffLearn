from bs4 import BeautifulSoup as bs
import requests, os, imp, pdfkit
from googlesearch import search
from topic import Topic
from flask import send_file
import regex as re

rootDir = "../data"

#makes sure there are no repeat websites
def filterURLS(urllist):

    filteredList = []
    filteredUrls = []
    for url in urllist:
        webDomain = getWebsite(url)

        if webDomain not in filteredList and webDomain != "":
            filteredList.append(webDomain)
            filteredUrls.append(url)

    return filteredUrls

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
        newTopic = Topic()
        pageList = os.listdir(rootDir + "/" + folder)
        newTopic.setName(folder)

        for page in pageList:
            newTopic.addPage(folder + "/" + page)

        topicList.append(newTopic)

    

    return topicList 
    