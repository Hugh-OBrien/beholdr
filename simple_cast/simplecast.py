import xml.etree.ElementTree as ET
import requests
import json
from os import path, chdir
#from openpyxl import Workbook
#from openpyxl.writer.excel import save_virtual_workbook

APIKEY = "sc_JDJfR4EUt0UOFPwbkU6tMw"
CASTID = "1105"

def get():
    junk =  requests.get("https://api.simplecast.com/v1/podcasts.json",auth=(APIKEY,''))
    decode = json.loads(junk.text)

    eyed = decode[0]['id']

    episodes = requests.get("https://api.simplecast.com/v1/podcasts/"+str(eyed)+"/episodes.json",auth=(APIKEY,''))
    decode = json.loads(episodes.text)

    ep = decode[5]
    print ep['title']
    epID = ep['id']
    print epID
    url = "https://api.simplecast.com/v1/podcasts/"+str(eyed)+\
                         "/statistics/episode.json?episode_id=" +\
                         str(epID) + "&timeframe=all"
    stats = requests.get(url,auth=(APIKEY,''))
    print stats.text

    url = "https://api.simplecast.com/v1/podcasts/"+str(eyed)+\
                         "/statistics/overall.json"
    stats = requests.get(url,auth=(APIKEY,''))
    print stats.text

def daySummary(dateStart, dateEnd):
    """
    returns a dictionary in the form {'episode title' : listens}
    takes a given start and end date

    Recommended to not set large spans per call since each request to Simplecast
    had a tendency to return a server error if the return was too large
    """

    baseUrl = "https://api.simplecast.com/v1/podcasts/"+CASTID+\
                         "/statistics/episode.json?episode_id="
    timeframe = "&timeframe=custom&start_date="+dateStart+\
                "&end_date="+dateEnd
    
    #get episode ids
    resp= requests.get("https://api.simplecast.com/v1/podcasts/"+\
                       CASTID+"/episodes.json",auth=(APIKEY,''))
    episodes = json.loads(resp.text)
    epDic = {}
    total = 0
    count = 0
    for e in episodes:
        eyeD = str(e['id'])
        title = e['title']
        data = json.loads(requests.get(baseUrl+eyeD+timeframe,auth=(APIKEY,'')).text)
        listens = data['total_listens']
        dic = {}
        if(listens != 0):
            print title + ": " + str(listens)
            dic['title'] = listens
            count += 1
            total += listens

    dic['total_listens'] = total
    dic['num_episodes'] = count
    print "Total Listens: " + str(total) + " from " + str(count) + " episodes"
    return dic


daySummary("2016-05-22","2016-06-11")



