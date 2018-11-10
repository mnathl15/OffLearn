from bs4 import BeautifulSoup as bSoup
import requests

#takes in a link, downloads the page, locates all the links, and returns the link and page
def parser(url):

    foundLinks = set()

    html = requests.get(url)
    page = bSoup(html.content, 'html5lib')

    links = page.find_all('a')

    for element in links:

        try:
            pageLink = element["href"]
            foundLinks.add(pageLink)

        except KeyError:
            pass

    return foundLinks,page

def getHost(url):

    host = ""

    splitLink = url.split(".")
    for i in range(1,len(splitLink)):
        host += splitLink[i] + "."

    return host[:-2]

#starting link
websiteLink = "http://www.ece.udel.edu/"
host = getHost(websiteLink)

queue = set()       #Every link we discover gets placed in here
visited = set()     #Only visited links go in here
pages = set()       #the raw html of every webpage goes here
unique = set()      #the links of each unique webpage
      


queue.add(websiteLink)

#Run until all links have been processed
while len(queue) != 0:

    link = queue.pop()

    # verify the link has not yet been visited
    if link not in visited:

        try:

            # see if the link is an extension
            if link[:4] != "http":

                # parse page and add new links to the queue
                locatedLinks,webPage = parser( websiteLink + link)
                queue = queue.union(locatedLinks)

                # add link to visited
                visited.add(link)
                print(len(visited), websiteLink+link)

                # check to see if page is unique
                if webPage not in pages:
                    pages.add(webPage)
                    unique.add(websiteLink+link)

            # see if the link is a sub domain i.e. cvorg.ece.udel 
            elif link.find(host) != -1:

                # parse page and add new links to the queue
                locatedLinks,webPage = parser(link)
                queue = queue.union(locatedLinks)

                # add link to visited
                visited.add(link)
                print(len(visited), link)

                # check to see if page is unique
                if webPage not in pages:
                    pages.add(webPage)
                    unique.add(link)

        # check for recursion error
        except Exception as e:
            pass

file = open("link.txt","w")
for link in unique:
    file.write(link + "\n")
file.close()

print("DONE")