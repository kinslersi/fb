import requests
import json
import jieba

access_token="EAAwNJviWDcEBAMFZCFSkZB6VwSV2luD6rr1tcF7o6oCYoqwXMNO9MOl9ODnGiEQ3JzEdvSESHsOgLhGwJnsXpGl1viCs4JamP2VLuVRPfMTZC8UZAXX1lB75lGsnukk4frnSMOu1CO8XuqNPJAAB4FzVcdHmhXV48kKa1bSZCPS9DHJmEd3QupxrZCxZBfUYxETL1VZAG3hkk1ZAQE7B82N8bRGCRureMCPxhXzIupROGi22OeY11YwfR"
url="https://graph.facebook.com/v15.0/me/posts?access_token="
full_url=url+access_token

res=requests.get(full_url)
js=json.loads(res.text)
corpus=[]
def get_message():
    if "error" in js.keys():
        print("you need to change access_token")
    else:
        for i in range(len(js["data"])):
            try:
                message=js["data"][i]['message']
                corpus.append(jieba.lcut(message))
            except KeyError:
                continue
get_message()
def nextpage_url():
    url=js['paging']['next']
    return url

# get data 
while True:
    try:
        res=requests.get(nextpage_url())
        js=json.loads(res.text)
        get_message()
    except KeyError:
        break

# count words
ele={}
for i in corpus:
    for word in i:
        if word not in ele:
            ele[word]=1
        ele[word]+=1

# sorted
data=ele.items()
sort=sorted(data,key=lambda data:data[1],reverse=True)
for i in sort:
    print(i[0],i[1])
