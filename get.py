import requests

headers={"Content-Type": "application/json"}

sessionSetup = requests.post("http://localhost:8191/v1", headers=headers, json={"cmd": "sessions.create"})
sessionRawData = sessionSetup.json()
print(sessionRawData["message"])

sessionId = sessionRawData["session"]

result = requests.post("http://localhost:8191/v1", headers=headers, json={"cmd": "request.get", "url": "https://nhentai.net/api/galleries/search?query=pages:>0", "session": sessionId})
rawResult = result.json()

print(rawResult["solution"]["response"])

sessionDestroy = requests.post("http://localhost:8191/v1", headers=headers, json={"cmd": "sessions.destroy", "session": sessionId})
sessionDestroyRaw = sessionDestroy.json()
print(sessionDestroyRaw["message"])


# fulllink = "https://nhentai.net/api/galleries/search?query=pages:%3E0?page="

# dirname = "raw"

# running = True

# index = 1
# while running:
#     r = requests.get(fulllink + str(index))
#     if r.status_code == 200:
#         print("Downloading: "+r.url)
#         with open(dirname+"/"+str(index)+".json", 'wb') as f:
#             f.write(r.content)
#     else:
#         running = False
#     index+=1