import requests
import re

SEARCH=r"<h2.*>Description</h2>(.*)<h2.*(Progrès</a>(.*)</span>)?Achèvement</a>(.*)</span>"

SEARCHWOWHEAD=r"<h2.*>Description</h2>(.*?)<h2.*?>Progrès.*?none\">(.*?)</div>.*Achèvement.*?none\">(.*?)</div>"

URL1="https://fr.classic.wowhead.com/quest="
URL2="https://wotlkdb.com/?quest="
INVALID_QUEST_MSG=r"n'existe pas"


questList=['12','18','3101','783','3']

for quest in questList[0]:
    page=requests.get(URL1+quest)
    
    text= page.text

    print(re.match(SEARCHWOWHEAD, text))
    #print(page.text)


