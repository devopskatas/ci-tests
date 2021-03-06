"""This module does blah blah."""
import codecs
import os
from html.parser import HTMLParser
from bs4 import BeautifulSoup

class SortTester(HTMLParser):
    """Iterates through all tags, parses the Next Visit list"""
    def handle_starttag(self, tag, attrs):
        # for attr in attrs:
        #     if attr[1].startswith('sectionList'):
        #         tagclass = attr[1].split()
        #         if len(tagclass) > 1:
        #             print("Start tag:", tag)
        #             print("     attr:", tagclass[1])
        for attr in attrs:
            
            if attr[1] == 'nextList':
                SortTester.parsingNextList = not SortTester.parsingNextList

            if attr[1] == 'masterList':
                SortTester.parsingMasterList = not SortTester.parsingMasterList

    def handle_endtag(self, tag):
        self.parsingNextList = not self.parsingNextList
        self.parsingMasterList = not self.parsingMasterList

    def handle_data(self, data):
        #print(data)
        if self.parsingNextList:
            print(data)

        if self.parsingMasterList:
            print(data)

    # def test_sorted(self, grocerytypeList):
    #     """Tests the list parsed from the HTML file for correct sorting"""
    #     return False

    def open_file(self):
        """FOO"""
        htmlfile = codecs.open(os.getcwd() + "\web-storelist-k7\storelist.htm", 'r', 'utf-8')
        print(htmlfile.read())
    
    def parseFile(self):
        """FOO"""

    parsingNextList = False
    parsingMasterList = False

sorter = SortTester()
htmlfile = codecs.open(os.getcwd() + "\web-storelist-k7\storelist.htm", 'r', 'utf-8')
sorter.feed(htmlfile.read())