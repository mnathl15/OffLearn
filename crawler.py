


from bs4 import BeautifulSoup as bs
import requests






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









search("einstein")


def getFileNames():
    return "None"

def getFile(filename):
    return "<p> Horray!! </p>"

# from googlesearch import search 

# for url in search('Civil War', stop=5):
#     print(url)

