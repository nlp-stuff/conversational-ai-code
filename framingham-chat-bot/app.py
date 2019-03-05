from flask import Flask, render_template, redirect, request as flask_request
import apiai
import json
import sys
import os
from notebook.framingham_predict import model_prediction


APIAI_CLIENT_ACCESS_TOKEN = "680699e618e64cf1be6575d137e1f05d"


app = Flask(__name__)

api_ai = apiai.ApiAI(APIAI_CLIENT_ACCESS_TOKEN)


def __parse_input_params(params): 
    
    data = { 
        'male':0,
        'age': 0,
        'cigsPerDay': 0,
        'BPMeds':0,
        'prevalentStroke':0,
        'prevalentHyp':0,
        'diabetes':0,
        'totChol': 0,
        'BMI': 0,
        'heartRate':0
    }
    
    if params.get('number'):
        data['male'] = 1
        
    if params.get('number1'):
        data['age'] = int(params.get('number1'))

    if params.get('number2'):
        data['cigsPerDay'] = int(params.get('number2'))

    if params.get('number3'):
        data['BPMeds'] = int(params.get('number3'))

    if params.get('number4'):
        data['prevalentStroke'] = int(params.get('number4'))

    if params.get('number5'):
        data['prevalentHyp'] = int(params.get('number5'))

    if params.get('number6'):
        data['diabetes'] = int(params.get('number6'))
  
    if params.get('number7'):
        data['totChol'] = int(params.get('number7'))
    
    if params.get('number8'):
        data['BMI'] = int(params.get('number8'))

    if params.get('number9'):
        data['heartRate'] = int(params.get('number9'))

    return data


@app.route("/")
def root():
    return render_template('index.html')


@app.route('/api_ai_test', methods=['POST'])
def apiAiTEst():

    requestData = flask_request.json

    if requestData["query"]:
        session_id = "1234567890"
        if requestData["session_id"]:
            session_id = str(requestData["session_id"])

        request = api_ai.text_request()
        request.session_id = session_id

        request.query = requestData["query"]

        response = request.getresponse()
        response = json.loads(response.read().decode('utf-8'))

        # print(json.dumps(response, indent=2))

        print("~" * 30)

        if response.get("result").get("parameters").get("number9"):
            data = __parse_input_params(response.get("result").get("parameters"))
            print(data)

            return_message = 'Congratulations!! Your chances of getting a heart attack is very less. But keep doing regular Exercises and go for regular health check up'

            result = model_prediction(data)
            print('result =', result)
            
            if result:
                return_message = 'Looks like you have chances of getting a heart attach in next 10 years. Please consult a physician and get a thorough medical check up done.'

            returnData = {
                "status": True,
                "message": return_message,
                "session_refresh": True
            }

            return json.dumps(returnData)
        else:
            responseValue = response.get("result").get(
                "fulfillment").get("speech")

            returnData = {
                "status": True,
                "message": responseValue
            }

            return json.dumps(returnData)
    else:

        returnData = {
            "status": False,
            "message": ""
        }

    return json.dumps(returnData)


if __name__ == '__main__':
    app.debug = True
    app.run(port=9967)
