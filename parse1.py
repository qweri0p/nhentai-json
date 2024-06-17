from pathlib import Path
import json
print("Starting...")
files = list(Path("raw").glob("*.json"))
print(f"Found {len(files)} files.")
data = []
for i in files:
    with i.open(mode="r", encoding="utf-8") as f:
        jsonobj = json.loads(f.read())
        data.append(jsonobj)
        if len(data) % 10000 == 0:
            print(f"Processed {len(data)} files...")
print("Writing to 'export.json'.")
with open("export.json", "r", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)
print("Done!")

# This is way too memory hungry
# We don't need all data
# Let's first just remove all page data
# That should help A LOT
