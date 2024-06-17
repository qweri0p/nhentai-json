from pathlib import Path
import json
print("Starting...")
files = list(Path("raw").glob("*.json"))
print(f"Found {len(files)} files.")
data = []
for i in files:
    newobj = {}
    with i.open("r", encoding="utf-8") as f:
        oldobj = json.loads(f.read())
    newobj["id"] = oldobj["id"]
    newobj["media_id"] = oldobj["media_id"]
    newobj["title"] = oldobj["title"]
    newobj["upload_date"] = oldobj["upload_date"]
    newobj["num_pages"] = oldobj["num_pages"]
    tags, artists, characters, parody, language, category  = [], [], [], [], [], []
    for tag in oldobj["tags"]:
        if tag["type"] == "tag":
            tags.append(tag["name"])
        elif tag["type"] == "artist":
            artists.append(tag["name"])
        elif tag["type"] == "character":
            characters.append(tag["name"])
        elif tag["type"] == "parody":
            parody.append(tag["name"])
        elif tag["type"] == "language":
            if tag["name"] != 'translated':
                language.append(tag["name"])
        elif tag["type"] == "category":
            category.append(tag["name"])

    newobj["tags"] = tags
    newobj["artist"] = artists
    newobj["characters"] = characters
    newobj["parody"] = parody
    newobj["language"] = language
    newobj["category"] = category

    data.append(newobj)

    if len(data) % 10000 == 0:
        print(f"Processed {len(data)} files...")

print("Writing to 'export.json'.")
with open("export.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)
print("Done!")

# yes, this is bad code
# no, i don't care
#
# running this script will require about 3 gigs of ram lmaooo
