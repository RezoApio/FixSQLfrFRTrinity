import requests
from argparse import ArgumentParser

 #Change the name to the correct variable
 #test formattage PEP8

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("-u", "--user", help="Define the user to connect to the TC database. default=trinity", default="trinity")
    parser.add_argument("-p", "--password", help="Define the password for the user connecting to the TC database. default=trinity", default="trinity")
    parser.add_argument("-f", "--file", help="The name of the file used by the program. Depends on the Action variable. default=traduction.csv", default="traduction.csv")
    parser.add_argument("-a", "--action",  help="generate: Creates a csv file with the translation from the WOW Head site. makesql: Generates the SQL file from a csv file (giving the opportunity to proofread before submitting. oneshot: generates directly the SQL from the WOW Head translation. default=generate",default="generate",choices=["makesql","generate", "oneshot"])
    return parser.parse_args()


def miseEnForme(text:str) -> str:
    formatted=(text.replace('&lt;nom&gt;','$N') #Parse le nom 
                   .replace('toto','tata') #Remplace toto en tata
                   .replace('ahah','ohoh')) #Remplace ahah par ohoh

    return formatted

arguments = parse_args()

BOM='\ufeff'

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
    if res1:
        res2=temp.find(END_DESC,res1)
        page[quest]['Description']=temp[res1+len(START_DESC)+1:res2].strip('\n')

        res1=temp.find(START_PROG)
        if res1:
            res2=temp.find(END_DESC,res1)
            temp2=temp[res1+len(START_PROG)+1:res2]

            res1=temp2.find('>')
            res2=temp2.find(END_PROG,res1)
            page[quest]['Progress']=temp2[res1+1:res2].strip('\n')
        else:
            page[quest]['Progress']='N/A'

        res1=temp.find(START_ACHIEVE)
        if res1:
            res2=temp.find(END_ACHIEVE,res1)
            temp2=temp[res1+len(START_ACHIEVE)+1:res2]

            res1=temp2.find('>')
            res2=temp2.find(END_ACHIEVE,res1)
            page[quest]['Achievement']=temp2[res1+1:res2].strip('\n')
        else:
            page[quest]['Achievement']='N/A'
    else:
        page[quest]['Description']='N/A'

if arguments.action in ['generate', 'oneshot']:
    output_list = ['Quest#;Description;Progress;Achievement']
    for quest, trad in page.items():
        output_list.append(';'.join([quest, trad['Description'], trad['Progress'], trad['Achievement']]))

    sortie = open(arguments.file, "w", enconding='utf-8')
    sortie.write(BOM+'\n'.join(output_list))
    sortie.close()


    https://wotlk.evowow.com/