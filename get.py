import requests, json, datetime, time

headers={"Content-Type": "application/json"}

#fulllink = 'https://nhentai.net/api/galleries/search?query=pages:>0&page='
fulllink = 'https://nhentai.net/api/gallery/'

starttime = datetime.datetime.now()
print(f"Starting at: {starttime}")

dirname = "raw"
# I can't be bothered to have the script make the directory
# just `mkdir raw` lmao

index = 514586
while index > 0:
    try:
        result = requests.get(fulllink + str(index), headers=headers)
        if result.status_code == 200:
            rawResult = result.json()
            print("Downloading: "+result.url)
            with open(dirname+"/"+str(index)+".json", 'w', encoding="utf-8") as f:
                json.dump(rawResult, f, ensure_ascii=False)
        elif result.status_code == 429:
            print("Rate limited!\nTrying again.")
            time.sleep(0.1)
            index+=1
    except:
        index+=1
    index-=1

endtime = datetime.datetime.now()

print(f"Downloaded all mangas\nStarted at: {starttime}\nFinished at: {endtime}")
