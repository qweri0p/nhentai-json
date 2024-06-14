import requests, json

headers={"Content-Type": "application/json"}

result = requests.get("https://nhentai.net/api/galleries/search?query=pages:>0", headers=headers)
rawResult = result.json()

amountofpages = rawResult["num_pages"]
print(f"There are {amountofpages} pages of manga on nhentai A.T.M.")

fulllink = "https://nhentai.net/api/galleries/search?query=pages:%3E0?page="

dirname = "raw"

running = True

index = 1
while index < int(amountofpages):
    result = requests.get(f"https://nhentai.net/api/galleries/search?query=pages:>0&page={str(index)}", headers=headers)
    if result.status_code == 200:
        rawResult = result.json()
        js = json.dumps(rawResult, sort_keys=True, indent=4, separators=(',', ': '))
        print("Downloading: "+result.url)
        with open(dirname+"/"+str(index)+".json", 'w', encoding="utf-8") as f:
            json.dump(rawResult, f, ensure_ascii=False, indent=4)
    else:
        running = False
    index+=1

