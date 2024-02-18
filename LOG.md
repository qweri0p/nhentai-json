I'm looking for a search query that selects ALL items in nhentai. "pages:>0" works

I think I want to decrease the size of the files. First make them conform to the following json template:

```json
[
    {
        "id": "[number]",
        "media_id": "[lookup ID in image database]",
        "title": {
            "english": "[null or string]",
            "japanese": "[null or string]",
            "pretty": "[null or string]"
        },
        "upload_date": "[unix timestamp]",
        "tags": [
            "[string]",
            "[string]"...
        ],
        "category": "[string]",
        "language": "[string]",
        "artist": "[string]",
        "parody": "[string]",
        "characters": [
            "[null or string]",
            "[null or string]",...
        ],
        "num_pages": "[number]"
    },...
]
```

This is very close to what the nhentai API provides.

My first goal is to make a script that downloads all json objects into a directory. Second goal is to write a parser that makes the data conform to the template above. The template will make it a lot easier to use it in applications.

I'll start with Python.

Commit 3b57edb

Main issue has been resolved. However a few new issues have come up.
- The result is embedded in HTML. I need it in pure JSON
- All cjk characters have been turned into unicode references
Both can easily be done with split() and a function