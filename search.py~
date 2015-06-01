from flask import Flask,render_template,request
import requests
import json
import sys
app=Flask(__name__)
@app.route('/')
def hello():
	return render_template("index.html")
@app.route("/geoData")
def queryData():
	lat=request.args["lat"]
	lon=request.args["lon"]
	typeof=request.args["place"]
	cypherUrl="http://localhost:7474/db/data/cypher"
	query="start n=node:restaurant('withinDistance:["+str(lat)+","+str(lon)+",10.0]') where n.type='"+typeof+"' return n.name"
	print query
	q={"query":query}
	t=requests.post(cypherUrl,q).json()
	print t
	return json.dumps(t)

@app.route('/dispResults')
def myfunc():
	url="http://localhost:9200/_search"
	query=request.args["query"]
	
	d={  "query":
		     {
		     	"query_string":
		     			{
		     			 "query":query
		     			}
		     	}
		     
		}
	response=requests.post(url,data=json.dumps(d)).json()
	k=[]
	try:
		for i in response['hits']['hits']:
			index=i['_index']
			places=i['_source']['places']
			score=i['_score']
			l=[index,score,places]
			print index,score,places
			k.append(l)
	except:
		print "Data not there"
#print response.keys()		 
	return json.dumps(k)
if __name__=="__main__":
	app.run()
