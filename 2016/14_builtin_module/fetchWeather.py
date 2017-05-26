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
@file: fetchWeather.py
@time: 16/5/24 上午7:11
"""
from datetime import datetime
from pyexpat import ParserCreate

from datetime import timedelta
from urllib import request


class WeatherSaxHandler(object):

    def __init__(self):
        self._weather = {}

    def start_element(self, name, attrs):

        if name == 'yweather:location':
            self._weather['city'] = attrs['city']
            self._weather['country'] = attrs['country']
        elif name == 'yweather:condition':
            self._weather['condition'] = attrs
        elif name == 'yweather:forecast':
            self._weather[attrs['date']] = attrs

    def end_element(self, name):
        pass

    def char_data(self, text):
        pass


def parse_weather(data):

    handler = WeatherSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(data)

    Dweather = {}
    Dweather['today'] = {}
    Dweather['tomorrow'] = {}

    condition = handler._weather['condition']['date'].split(',')[1].strip().split(' ')
    today = condition[0] + ' ' + condition[1] + ' ' + condition[2]
    tomorrow = datetime.strptime(today,'%d %b %Y') + timedelta(days=1)

    Dweather['city'] = handler._weather['city']
    Dweather['country'] = handler._weather['country']
    Dweather['today']['text'] = handler._weather[today]['text']
    Dweather['today']['low'] = handler._weather[today]['low']
    Dweather['today']['high'] = handler._weather[today]['high']

    Dweather['tomorrow']['text'] = handler._weather[tomorrow.strftime('%d %b %Y')]['text']
    Dweather['tomorrow']['low'] = handler._weather[tomorrow.strftime('%d %b %Y')]['low']
    Dweather['tomorrow']['high'] = handler._weather[tomorrow.strftime('%d %b %Y')]['high']

    return Dweather





def fetch_xml(url):
    with request.urlopen(url) as f:
        xmldata = f.read()
    return parse_weather(xmldata.decode('utf-8'))

print(fetch_xml('http://weather.yahooapis.com/forecastrss?u=c&w=2151330'))

def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass