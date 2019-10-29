import requests
import re

SEARCH=r"<h2.*>Description</h2>(.*)<h2.*(Progrès</a>(.*)</span>)?Achèvement</a>(.*)</span>"

SEARCHWOWHEAD=r"<h2.*>Description</h2>(.*?)<h2.*?>Progrès.*?none\">(.*?)</div>.*Achèvement.*?none\">(.*?)</div>"

START_DESC='Description</h2>'
END_DESC='<h2'

START_PROG='Progrès</a></h2>'
END_PROG='</div>'

START_ACHIEVE='Achèvement</a></h2>'
END_ACHIEVE='</div>'

URL1="https://fr.classic.wowhead.com/quest="
URL2="https://wotlkdb.com/?quest="
INVALID_QUEST_MSG=r"n'existe pas"

#Need to add a way to get the full list of quest
#probably the best is to read the db itself.
questList=['12','18','3101','783','3']
page={}

#first let's code something that gets results
#will add some testing to prevent errors later
for quest in questList:
    page[quest]={'text':requests.get(URL1+quest).text}

    temp=page[quest]['text']

    res1=temp.find(START_DESC)
    res2=temp.find(END_DESC,res1)
    page[quest]['Description']=temp[res1+len(START_DESC)+1:res2].strip('\n')

    res1=temp.find(START_PROG)
    res2=temp.find(END_DESC,res1)
    temp2=temp[res1+len(START_PROG)+1:res2]

    res1=temp2.find('>')
    res2=temp2.find(END_PROG,res1)
    page[quest]['Progrès']=temp2[res1+1:res2].strip('\n')

    res1=temp.find(START_ACHIEVE)
    res2=temp.find(END_ACHIEVE,res1)
    temp2=temp[res1+len(START_ACHIEVE)+1:res2]

    res1=temp2.find('>')
    res2=temp2.find(END_ACHIEVE,res1)
    page[quest]['Achèvement']=temp2[res1+1:res2].strip('\n')
