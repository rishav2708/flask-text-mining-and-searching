import requests
import json
import glob
import re
import simplejson as js
def removeNoise(fcontent):
	l=fcontent.split("\n")
	for i in l:
		if re.findall('[a-zA-Z]+',i)==[]:
			l.remove(i)
	return l
classes=['enjoy', 'shopping', 'friends', 'dating', 'sleep', 'school', 'relax', 'family']
#classes.remove("extractor.py")
#classes.remove("inntell.json")
#lasses.remove("search.py")
#classes.remove("theFlask.py")
info=js.loads(open("inntell.json").read())
#indexing the files
url="http://localhost:9200/"
for i in classes:
	temp_url=url+i+"/first/1"
	print temp_url
	fcontent=(open(i).read()).replace(" ","")
	fcontent=removeNoise(fcontent)
	places=info[i]["true"]
	d={"matching_words":fcontent,"places":places}
	t=requests.put(temp_url,data=json.dumps(d))
	print t
