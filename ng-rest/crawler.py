from bs4 import BeautifulSoup as bs
import requests, os, imp, pdfkit
from googlesearch import search
topic = imp.load_source("topic", "./models/topic.py")
from flask import send_file
import regex as re

#acts as a search engine, returns status code
def searchInternet(query):


    querySize = 4
    rootDir = "data"

    searches = list(search(query,stop=querySize))
    urllist = filterURLS(searches)


    folderPath = "/".join([rootDir, query])
    if not os.path.exists(folderPath):
        os.mkdir(folderPath)

    #converts url to pdf
    for url in urllist:

        filePath = "/".join([rootDir, query, getWebsite(url)]) + ".pdf"
        print(filePath)
        try:
            path_wkthmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
            config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
            pdfkit.from_url(url, filePath, configuration=config)
        except:
            pass


#gets website name
def getWebsite(url):



    url = re.findall('(?<=\.)([^.]+)(?:\.(?:co\.uk|ac\.us|[^.]+(?:$|\n)))',url)


    return ''.join(url)

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

    return urllist




def getFileNames():
    topicList = []
    folderList = os.listdir("data")

    for folder in folderList:
        newTopic = topic.Topic()
        pageList = os.listdir("data/" + folder)
        direc = os.path.join("data/",folder)



        newTopic.setName(folder)



        for page in pageList:
            newTopic.addPage(os.path.abspath(os.path.join(direc,page)))
            topicList.append(newTopic)

    return topicList 

getFileNames()

