import json
import requests
from bs4 import BeautifulSoup

import re
#import urllib.request

#Used headers/agent as the request timed out and asking for agent. Using following code you can fake the agent.
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/61.0.3163.100 Safari/537.36'}
my_url = "https://www.zomato.com/bangalore/restaurants?page="
Dict = {}
lst = []
'''here we are giving the value 20 for crawling just 20 pages as crawling it takes other option was we could have gone by 
threading that we could have crawled all pages easilt
  '''
for k in range(0, 20):
    response = requests.get(my_url + str(k+1), headers=headers)
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





