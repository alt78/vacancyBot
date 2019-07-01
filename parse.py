from urllib import request
from bs4 import BeautifulSoup
import re


def get_vacany(urlList):
    vacancyList = []
    for url in urlList:
        html = request.urlopen(url)
        bsObj = BeautifulSoup(html, 'html.parser')
        vacancyListBs = bsObj.findAll('a', class_='bloko-link HH-LinkModifier')
        for vacancy in vacancyListBs:
            a = vacancy.get_text()
            result = re.search('(j*unior)|(м*ладший)|(с*тажер)', a)
            result1 = re.search('(p*ython)|(w*eb)|(d*jango)|(d*ata)', a)
            if (result and result1) is not None:
                vacancyList.append({'tittle':a,
                           'href':vacancy['href']})
    return vacancyList



def get_url_list():
    url='https://hh.ru/search/vacancy?text=Python+&only_with_salary=false&clusters=true&area=1530&enable_snippets=true&salary='
    url1List=[]
    html=request.urlopen(url)
    bsObj=BeautifulSoup(html,'html.parser')
    urlCount=bsObj.findAll('a', class_='bloko-button HH-Pager-Control')[-1]['data-page']
    url2=bsObj.findAll('a', class_='bloko-button HH-Pager-Control')[-1]['href']
    for i in range(int(urlCount)+1):
        url1='https://hh.ru/'+str(url2[:-1])+str(i)
        url1List.append(url1)
    return url1List
try:
    a=get_url_list()
    b=get_vacany(a)
    print(b)

except:
    b=['https://hh.ru/search/vacancy?text=Python+&only_with_salary=false&clusters=true&area=1530&enable_snippets=true&salary=']
    b=get_vacany(b)
    print(b)