from flask import Flask
from flask_cors import CORS, cross_origin
import requests
import json
from flask import request


VoteID = '48d75c359ce4'
QuestionsURI = 'https://api.mentimeter.com/questions/'+VoteID
ResultsURI = 'https://api.mentimeter.com/questions/'+VoteID+'/result'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'}
GetQuestions = requests.get(QuestionsURI, headers=headers)
Questions=GetQuestions.json()
GetResults = requests.get(ResultsURI, headers=headers)
Results=GetResults.json()
resultDict = {
  "question": Questions['question'],
  "results": Results['results']
}
		
JsonArray = json.dumps(resultDict)
    
app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/48d75c359ce4')
@cross_origin(supports_credentials=True)
def index():
   #print (request.args.get('questionid'))
   #return (request.args.get('questionid'))
   #return (GetURL(request.args.get('questionid')))
   return JsonArray

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    
#