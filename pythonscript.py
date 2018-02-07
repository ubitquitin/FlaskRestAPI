#!/usr/bin/python
# -*-coding: utf-8 -*-

from __future__ import division
import sys, os
import re

def basestats(filename):
    regexname = re.compile(r"^(\w+\s\w+) batted (\d) times with (\d) hits and (\d) runs$")
    playerbats = dict()
    playerhits = dict()
    playeravg = dict()

    with open(filename) as f:
        for line in f:
            # print("Read line: %s" % line.rstrip())
            match = regexname.match(line.rstrip())
            if match is not None:
                player = match.group(1)
                bats = int(match.group(2))
                hits = int(match.group(3))
		#print("Player [%s] Bats [%s] Hits [%s] Runs [%s]" % (match.group(1),match.group(2),match.group(3),match.group(4)) )
                if player in playerbats:
                    playerbats[player] = playerbats[player] + bats
                else:
                    playerbats[player] = bats
                if player in playerhits:
                    playerhits[player] = playerhits[player] + hits
                else:
                    playerhits[player] = hits

        for player in playerbats:
            playeravg[player] = (playerhits[player] / playerbats[player])
        
        for key,value in sorted(playeravg.items(),key=lambda kv:kv[1],reverse=True):
            print ("%s: %0.3f" % (key,value))

if __name__ == "__main__":

    if len(sys.argv) <2:
        sys.exit("Usage: %s filename" % sys.argv[0])

    filename = sys.argv[1]

    if not os.path.exists(filename):
        sys.exit("Error: File '%s' not found" % sys.argv[1])

    basestats(filename)
