#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
@version: ??
@usage: 
@author: kHRYSTAL
@license: Apache Licence 
@contact: khrystal0918@gmail.com
@site: https://github.com/kHRYSTAL
@software: PyCharm
@file: PythonEventParser.py
@time: 16/5/24 上午6:37
"""


from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request

def getHtml(url):
    req = request.Request(url)
    #req.add_header('User-Agent',
                  # 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    with request.urlopen(req) as f:
        # print('Status:', f.status, f.reason)
        # for k, v in f.getheaders():
        #     print('%s: %s' % (k, v))
        return f.read().decode('utf-8')


class MyHTMLParser(HTMLParser):
    def __init__(self):
        super(MyHTMLParser, self).__init__()
        self.Events={}
        self._tag=''
        self._counter=0

    def handle_starttag(self, tag, attrs):
        if tag=='h3'and attrs and attrs[0][0]=='class'and  attrs[0][1]=='event-title':
            self._tag='title'
            #print('<%s>' % attrs)
        if tag=='time'and attrs and attrs[0][0]=='datetime':
            self._tag = 'datetime'
            #print('<%s>' % attrs)
        if tag == 'span'and attrs and attrs[0][0]=='class'and  attrs[0][1]=='event-location':
            self._tag = 'location'
            #print('<%s>' % attrs)

    def handle_data(self, data):
        if self._tag=='title':
            self.Events[self._counter]={'title':data.strip("\n")}
        if self._tag=='datetime':
            self.Events[self._counter]['time'] = data.strip("\n")
        if self._tag=='location':
            self.Events[self._counter]['location'] = data.strip("\n")
            self._counter += 1
        self._tag=''

    def printEvents(self):
        for k in self.Events:
            print("title:%s  Time: %s  Loaction:%s" % (
                self.Events[k]['title'], self.Events[k]['time'], self.Events[k]['location']))



if __name__=='__main__':
    parser = MyHTMLParser()
    parser.feed(getHtml('https://www.python.org/events/python-events/'))
    parser.printEvents()




def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass