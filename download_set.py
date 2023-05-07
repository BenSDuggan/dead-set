# Download the set data needed by the model given the set.fm slug
# Example `python download_set.py grateful-dead`


import json
import os
import requests
from pathlib import Path
import sys
import time
import urllib


api_url = "https://api.relisten.net/api/v2/"
slug = sys.argv[1]

print("Downloading sets for slug: " + slug)

# Save location
parent_dir = "%s" % slug
try:
    os.mkdir(parent_dir)
except:
    pass

songs_file = Path(parent_dir) / ("%s_songs.json" % slug)
years_file = Path(parent_dir) / ("%s_years.json" % slug)
shows_dir = Path(parent_dir) / "shows"

try:
    os.mkdir(shows_dir)
except:
    pass
    
years = []
shows_dict = {}
combined_table = []



# Download songs
print("Downloading songs")
req_url = urllib.parse.urljoin(api_url, "artists/%s/songs"%slug)
r = requests.get (req_url)

parsed = json.loads(r.text)
print(len(parsed))

with open(songs_file, 'w') as f:
    json.dump(parsed, f, indent=4)



# Download years
print("Downloading years")
req_url = urllib.parse.urljoin(api_url, "artists/%s/years"%slug)
r = requests.get (req_url)

parsed = json.loads(r.text)
print(len(parsed))

with open(years_file, 'w') as f:
    json.dump(parsed, f, indent=4)

for c in parsed:
    years.append(int(c["year"]))



# Get show information, broken up by year
print("Downloading sets by year")

start = time.time()
last_time = start
for y in years:
    print("%d: " % y, end="")
    req_url = urllib.parse.urljoin(api_url, "artists/%s/years/%d"%(slug, y))
    r = requests.get (req_url)
    if r.status_code != 200:
        print("Error getting data for year: %d" % y)
    
    year = json.loads(r.text)
    shows = year
    
    for s in range(0, len(year["shows"])):
        req_url = urllib.parse.urljoin(api_url, "artists/%s/years/%d/%s"%(slug, y, year["shows"][s]["display_date"]))
        r = requests.get (req_url)
        if r.status_code != 200:
            print("Error getting data for year: %d; show: %s" % (y, year["shows"][s]["display_date"]))
            print("Status: %d" % r.status_code)

        show = json.loads(r.text)
        shows["shows"][s]["sources"] = show["sources"]

    with open(shows_dir / ("%d_shows.json"%y) , "w") as f:
        #json.dump(shows, f, indent=4)
        json.dump(shows, f)
    
    print("%5.2f, %5.2f" % (time.time()-last_time, time.time()-start))
    last_time = time.time()
    