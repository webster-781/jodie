#!/bin/bash

#wget http://snap.stanford.edu/jodie/reddit.csv -P data/
#wget http://snap.stanford.edu/jodie/wikipedia.csv -P data/
#wget http://snap.stanford.edu/jodie/mooc.csv -P data/
#wget http://snap.stanford.edu/jodie/lastfm.csv -P data/

wget http://snap.stanford.edu/data/CollegeMsg.txt.gz -P data/
gzip -d CollegeMsg.txt.gz