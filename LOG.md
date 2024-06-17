# Log
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

## Commit 3b57edb

Main issue has been resolved. However a few new issues have come up.  
- The result is embedded in HTML. I need it in pure JSON
- All cjk characters have been turned into unicode references
Both can easily be done with split() and a function  

I'm currently retreiving all json files for later use. This will take some time...  

Next day:  
This shit doesn't work at all. I got like 400 files deep and then it broke:(  
I have two options:
- Press on and do this mess, which will be very annoying and very hard to update.
- Fork the nhentai-api npm package to make it work with FlareSolverr. This will make it dependent on a seperate program.
- Give up. nhentai sucks!

## Commit 4711407

ok for some reason nhentai disabled the cloudflare protection  
(fuck cloudflare)  
rewrote the script to work without flaresolverr  
now just let it gather data  
and then modify that data into one or more compact json files  
easy!  

i just started the scraping process  
i should do this with a vpn  
fuck it  
if i get ip blocked i'll just use a vpn  

the data from this scrape will not be complete  
when a new manga is uploaded, all others get moved up by one  
if this happens between me starting the scrape and it finishing (lol)  
it will skip both the one that got added  
there will also be a duplicate across two files  

### Update
I ran into 2 issues
1. Connection reset by peer
2. If a manga has been deleted off nhentai, the api can't get the data from the page the manga was o

the first issue is easily fixed with a try catch block  
the second issue is a bit harder  

my current idea is to have it query all 6-digit codes  
and store all in json  
this would accidentally fix the issue described above (line 70)  
however, this would take WAY longer  
as for now I have 167 megabytes of json  
I NEED MORE!  

i'll do this later  

i should be quick, idk when they're gonna enable cloudflare again (or something similar)  

results of failed dumping are in the "failed" branch  

## Commit 4913c9d

rewrote the script to fetch json for every 'gallery'  
seems to be working flawlessly  
i'm getting http code 429 (too many requests)  
but it doesn't seem to matter?  
i'm now convinced this isn't an issue since nhentai IS rate limiting me  
however it is not enough to cause a timeout  
so it should be 100% ok  

## Commit 370fc03

turns out, rate limiting DOES make the script skip  
fixed it  

i've realized that this way of scraping is very easy to maintain  
in the script you just move the index variable up and the 0 in the while condition up to the last recorded gallery  
might even be able to automate it in github actions  
i should've started with this approach to begin with  

## Commit 0ddf395

raw dump is done!
either i do a json, or i do a sqlite database  
hmmm  
lemme think about this  

## Commit 5cde280

chatgippity wrote me a script to check missing numbers  
all appears to be correct  
the check.py script returns a list of id's  
all of them appear to have been deleted  
i'll turn it into a proper script later (argparse, path instead of os)

## Commit 2dbeac4

uploaded 2 raw parsers.  
both will scan the 'raw' directory and link stuff into one file  
the exported file from parser2.py is still massive  
next up, database for easier querying  
mysql or sqlite??!?!?  
i'm gonna start with sqlite cuz it's easier to export
