#!/usr/bin/python
#encoding: utf-8

import httplib
import json
import os

HOST = "douban.fm"
URL = "/j/mine/playlist?type=s&sid=186609&pt=39.6&channel=1&pb=64&from=mainsite"
MAX_SONGS = 20

def get_songlist():
  conn = httplib.HTTPConnection(HOST)
  conn.request("GET", URL)
  
  resp = conn.getresponse()
  
  songlist = []
  if resp.status == 200:
    data = json.loads(resp.read())
    for song in data["song"]:
      songlist.append(song["url"])
  else:
    print "Get songlist error"
  
  conn.close()
  return songlist


def clear_old_songs():
  count = int(os.popen('mpc playlist|wc -l').read())
  print "Thre is %d songs in current play list" % count
  if count > MAX_SONGS:
    print "Clear old songs...."
    for i in xrange(count - 10):
      os.system("mpc del 1")
  else:
    print "Neednet clear"


def add_songs():
  songs = get_songlist()
  for song in songs:
    print "add %s to list" % song
    os.system("mpc add %s" % (song))
    
  

if __name__ == "__main__":
  add_songs()
  clear_old_songs()
