# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
from bs4 import BeautifulSoup
#from pandas import DataFrame

c_name="walmart"
def check_number(c_name):
    phone=[]
    url = "https://www.google.com/search?source=hp&ei=bTDhW_3hBqHOjwSr5qGwDg&q="+c_name+\
    "&oq=&gs_l=psy-ab.1.0.35i39k1l6.0.0.0.3353.2.1.0.0.0.0.0.0..1.0....0...1c..64.psy-ab..1.1.104.6...105.5kPiJ0DrZYM"
    get_html = requests.get(url)
    soup = BeautifulSoup(get_html.content,'html.parser')
    p = soup.find_all('span',{'class':'A1t5ne'})
    for i in p:
        if i.text.startswith("1 "):
            phone.append(i.text)
    return phone

