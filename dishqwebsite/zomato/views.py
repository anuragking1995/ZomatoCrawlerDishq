from django.shortcuts import render
from django.http import HttpResponse
from .models import Restaurants
import json
import requests
from bs4 import BeautifulSoup
# Create your views here.


def dcrawl():
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/61.0.3163.100 Safari/537.36'}
    my_url = "https://www.zomato.com/bangalore/restaurants?page="
    Dict = {}
    lst = []
    for k in range(0, 10):
        response = requests.get(my_url + str(k + 1), headers=headers)
        content = response.content
        page_soup = BeautifulSoup(content, "html.parser")
        containers = page_soup.find_all("article", {"class": "search-result"})
        for i in range(0, len(containers)):
            cont = containers[i].find_all("a", {"class": "result-title hover_feedback zred bold ln24 fontsize0 "})
            cont2 = containers[i].find_all("div", {"class": "ta-right floating search_result_rating col-s-4 clearfix"})
            Dict["name"] = cont[0].text.rstrip()
            Dict["url"] = cont[0]["href"].rstrip()
            Dict["location"] = cont[0]["title"].rstrip()
            Dict["rating"] = cont2[0].div.text.lstrip().rstrip()
            lst.append(Dict)
            Dict = {}

    with open('jsondata.txt', 'w') as outfile:
        json.dump(lst, outfile)
    return lst

def index(request):
    lst = dcrawl()
    return render(request, 'zomato/index.html',{"lst":lst})

