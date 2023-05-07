# Dead set

Guess what is the Greatful Dead / Dead and company will play next.


## Steps to run from the begining

1. Download set lists
    1. Find the slug on [setlist.fm](https://www.setlist.fm/) for the artist you're interested in. Eg. `grateful-dead` for the Grateful Dead
    2. Run the [download_set.py](download_set.py) script with the first argument the slug for your artist (e.g. `python download_set.py grateful-dead`). This will save the setlists in the [sets](sets) folder.
2. Clean the set lists
    1. 

## Structure

* [sets](/sets): Download location for sets


## Sets

Using the [Setlist.fm](https://api.setlist.fm/docs/1.0/index.html) API. The initial work to figure out the API was done [here](https://github.com/BenSDuggan/weekend-projects/tree/master/dead-sets).
