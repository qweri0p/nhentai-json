import requests, json, datetime

headers={"Content-Type": "application/json"}

result = requests.get("https://nhentai.net/api/galleries/search?query=pages:>0", headers=headers)
rawResult = result.json()

amountofpages = rawResult["num_pages"]
print(f"There are {amountofpages} pages of manga on nhentai rn")

fulllink = 'https://nhentai.net/api/galleries/search?query=pages:>0&page='

starttime = datetime.datetime.now()
print(f"Starting at: {starttime}")

dirname = "raw"
# I can't be bothered to have the script make the directory
# just `mkdir raw` lmao

running = True

index = 1
while index < int(amountofpages):
    result = requests.get(fulllink + str(index), headers=headers)
    if result.status_code == 200:
        rawResult = result.json()
        print("Downloading: "+result.url)
        with open(dirname+"/"+str(index)+".json", 'w', encoding="utf-8") as f:
            json.dump(rawResult, f, ensure_ascii=False)
    else:
        running = False
    index+=1

endtime = datetime.datetime.now()

print(f"Downloaded all pages\nStarted at: {starttime}\nFinished at: {endtime}")
