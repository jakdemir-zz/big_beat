import sys,re



def parseLines(fp,outfp):
	dateReg = re.compile('[0-9]{4}')
	date = ""
	for line in fp.readlines():
		line = line.strip()
		hit = re.match(dateReg,line)
		record = ""
		print line
		if line and hit:
			date = hit.group()
		elif line and date:
			line = line.decode('ascii','ignore')
			rest,artist = line.split('- ')
			rank,song = rest.split('.',1)
			record = rank+","+song+","+artist+","+date+"\n"
			outfp.write(record)
	
if __name__ == '__main__':
	print "usage: <infile> <outfile>"
	print "starting parsing" 
	
	
	inFile = open(sys.argv[1],'r')
	outFile = open(sys.argv[2],'w')
	
	parseLines(inFile,outFile)
	inFile.close()
	outFile.close()