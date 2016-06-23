import csv
import pickle
from time import sleep
import time
import sys

from pyechonest import config
config.ECHO_NEST_API_KEY="D7DYPFYLZEHVH8TDM"
from pprint import pprint
from pyechonest import song
#rkp_results = song.search(artist='radiohead', title='karma police')
#karma_police = rkp_results[0]
#print karma_police.artist_location
#print 'tempo:',karma_police.audio_summary['tempo'],'duration:',karma_police.audio_summary['duration']

def querySong(songName, artist):
	rkp_results = song.search(artist=artist, title=songName)
	karma_police = rkp_results[0]
	print karma_police.artist_location
	print 'tempo:',karma_police.audio_summary['tempo'],'duration:',karma_police.audio_summary['duration']
	print rkp_results[0]

def dump(file):
	dictionary = {}
	failedList = []
	with open("parsedHits.csv") as csv_file:
		i=0;
		for row in csv.reader(csv_file, delimiter=','):
				print i
				i=i+1
				sleep(3)
				#total = int(col)
				songArtist = row[2]
				songName = row[1]
				print "getting hits:%s from %s"%(songName,songArtist)
				startTime = time.time()
				record=song.search(artist = songArtist, title=songName)
				endTime  = time.time()
				print "time for api call was: %s ms"%(endTime - startTime)
				if record:
					dictionary[songName]=record[0]
					#dictionary[songName]=record[0].audio_summary['tempo']
					print "song name: %s , %s "%(songName,record[0].audio_summary)
				else:
					failedList.append([songArtist,songName])
				if(i>60):
					sleep(60)
					i=0;
	#print dictionary

	pickle.dump(failedList, open(failed.p,"wb")) 
	pickle.dump( dictionary, open( file+".p", "wb" ) ) 

	print "printing failedList..."
	for i in failedList:
		print i
	print "printed failedList..."

if __name__ == '__main__':
	print "usage: dump <outfile>"
	print "	 	  query <song_name> <artist>"
	if sys.argv[1] == 'dump':
		dump(sys.argv[2])
	if sys.argv[1] == 'query':
		querySong(sys.argv[2],sys.argv[3])
