from bs4 import BeautifulSoup as bs
import requests, os, imp, pdfkit
from googlesearch import search
topic = imp.load_source("topic", "./models/topic.py")
from flask import send_file
import regex as re

#acts as a search engine, returns status code
def searchInternet(query):


    querySize = 10
    rootDir = "data"



    searches = list(search(query,stop=querySize))



    filterURLS(searches)


    folderPath = "/".join([rootDir, query])


    if not os.path.exists(folderPath):
        os.mkdir(folderPath)

    #converts url to pdf
    for url in searches:

        filePath = "/".join([rootDir, query, getWebsite(url)]) + ".pdf" 
        path_wkthmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
        pdfkit.from_url(url, filePath, configuration=config)

#gets website name
def getWebsite(url):



    url = re.findall('(?<=\.)([^.]+)(?:\.(?:co\.uk|ac\.us|[^.]+(?:$|\n)))',url)



    return url

#makes sure there are no repeat websites
def filterURLS(urllist):
    occur_url={}
    for url in urllist:
        webDomain = ''.join(getWebsite(url))
        print(webDomain)
        try:
            occur_url[webDomain]  = occur_url[webDomain] + 1
        except:
            occur_url[webDomain] = 0



        if(occur_url[webDomain] > 1):
            urllist.remove(url)


    print(urllist)




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