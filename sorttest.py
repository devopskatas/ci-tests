"""This module does blah blah."""
import codecs
import os
from html.parser import HTMLParser


class SortTester(HTMLParser):
    """Iterates through all tags, parses the Next Visit list"""
    def handle_starttag(self, tag, attrs):
        
        for attr in attrs:
            if attr[1].startswith('sectionList'):
                tagclass = attr[1].split()
                if len(tagclass) > 1:
                    print("Start tag:", tag)
                    print("     attr:", tagclass[1])

    def test_sorted(self, grocerytypeList):
        """Tests the list parsed from the HTML file for correct sorting"""
        return False

    def open_file(self):
        """FOO"""
        htmlfile = codecs.open(os.getcwd() + "\web-storelist-k7\storelist.htm", 'r', 'utf-8')


        print(htmlfile.read())
    
    def parseFile(self):
        """FOO"""


sorter = SortTester()
htmlfile = codecs.open(os.getcwd() + "\web-storelist-k7\storelist.htm", 'r', 'utf-8')
sorter.feed(htmlfile.read())