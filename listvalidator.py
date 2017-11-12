from bs4 import BeautifulSoup
import os

with open(os.getcwd() + "\web-storelist-k7\storelist.htm") as fp:
    soup = BeautifulSoup(fp, "html.parser")
    
    print("SECTIONS:")
    for content in soup.find_all("ul", {"id":"grocerySections"}):
        if content.text:
            print (content.text)
    
    print("MASTERLIST:")
    for content in soup.find_all("ol", {"id":"masterList"}):
        if content.text:
            print(content.text)
    
    print("NEXTVISIT:")
    for content in soup.find_all("ol",{"id":"nextList"}):
        if content.text:
            print(content.text)