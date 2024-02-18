import requests, json

headers={"Content-Type": "application/json"}

sessionSetup = requests.post("http://localhost:8191/v1", headers=headers, json={"cmd": "sessions.create"})
sessionRawData = sessionSetup.json()
print(sessionRawData["message"])

sessionId = sessionRawData["session"]

result = requests.post("http://localhost:8191/v1", headers=headers, json={"cmd": "request.get", "url": "https://nhentai.net/api/galleries/search?query=pages:>0", "session": sessionId})
rawResult = result.json()



resultString = rawResult["solution"]["response"]
json_string = resultString[131:-20]
json_data = json.loads(json_string)
amountofpages = json_data["num_pages"]

fulllink = "https://nhentai.net/api/galleries/search?query=pages:%3E0?page="

dirname = "raw"

running = True

index = 1
while index < int(amountofpages):
    result = requests.post("http://localhost:8191/v1", headers=headers, json={"cmd": "request.get", "url": "https://nhentai.net/api/galleries/search?query=pages:>0&page="+str(index), "session": sessionId})
    if result.status_code == 200:
        rawResult = result.json()

        resultString = rawResult["solution"]["response"]
        json_string = resultString[131:-20]
        print("Downloading: "+result.url)
        with open(dirname+"/"+str(index)+".json", 'wb') as f:
            f.write(bytes(json_string.encode('utf8')))
    else:
        running = False
    index+=1

sessionDestroy = requests.post("http://localhost:8191/v1", headers=headers, json={"cmd": "sessions.destroy", "session": sessionId})
sessionDestroyRaw = sessionDestroy.json()
print(sessionDestroyRaw["message"])