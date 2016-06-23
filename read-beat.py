import pickle

dict_file = open('fulldictionary.p', 'rb')

#assuming we're getting dictionart of type a['<year>] = [<beat1>,<beat2>...]
def meanBeats(beatByYearDict):

	result = {}
	for key in beatByYearDict:
		sum = reduce(lambda x,y: x+y, beatByYearDict[key] )
		avg = sum / key.length
		result[key] = avg
		
	return result


def generateAvgVec(dictionary,normalize=False):
	normalized = []
	for key in dictionary.keys():
		year,rank = key.split('-')
		tempo = dictionary[key][2]['tempo']
		note = dictionary[key][2]['key']
		live = dictionary[key][2]['liveness']
		dance = dictionary[key][2]['danceability']
		speech = dictionary[key][2]['speechiness']
		loud = dictionary[key][2]['loudness']
		length = dictionary[key][2]['duration']
		
		normalized.append([year,speech,tempo,note,live,dance,rank,loud,length])

			
	if normalize:
		return meanBeats(normalized)
	else:
		return normalized
    #print "%s,%s"%(year,dictionary[key][2]['tempo'])

def printDictToCSV(arr):
	#print "%s,%s,%s,%s,%s,%s,%s,%s,%s"%("year","speech","tempo","key","live","dance","rank","loud","length")
	for key in arr:
		print "%s,%s,%s,%s,%s,%s,%s,%s,%s"%(key[0],key[1],key[2],key[3],key[4],key[5],key[6],key[7],key[8])
		#print "%s,%s"%(key,dict[key])
	

if __name__ == '__main__':
	if sys.argv[1] == 'dump':
		dictionary = pickle.load(dict_file)
		normalizedAvgVec = generateAvgVec(dictionary)
		printDictToCSV(normalizedAvgVec)
