from bs4 import BeautifulSoup
import os

testList = ["Foo","Bar","Bump","Bish"]
masterList = [] 
nextList = []
with open(os.getcwd() + "storelist.htm") as fp:
    soup = BeautifulSoup(fp, "html.parser")
    
    
    print("SECTIONS:")
    # for content in soup.find_all("ul", {"id":"grocerySections"}):
    #     if content.text:
    #         print (content.text)
    
    #print("MASTERLIST:")
    for content in soup.find_all("ol", {"id":"masterList"}):
        if content.text:
            masterList = content.text.splitlines()
    
    #print("NEXTVISIT:")
    for content in soup.find_all("ol",{"id":"nextList"}):
        if content.text:
            nextList = content.text.splitlines()

    #print("MISMATCH:")
print(testList)
print(len(masterList))
print(len(nextList))
print(list(set(nextList) - set(masterList)))