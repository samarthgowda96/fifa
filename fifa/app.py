from flask import Flask,jsonify, render_template, request
import json


app = Flask(__name__)
jData = json.loads(open('./teams.json').read())
data=jData["teams"]

@app.route('/')
def teams_main():
    return render_template("index.html")

@app.route('/getteams/')
def teams_all():
    myList=[]
    for element in data:
        myList.append(element)
    # result = jsonify(myList)
    return render_template("index.html",items=myList)

@app.route('/getteams/<string:points>/')
def teams(points=''):
    myList=[]
    for element in data:
        if element["points"] == points:
            myList.append(element)
    #result = jsonify(myList)
    return render_template("index.html",items=myList)

@app.route('/getteams/<string:points>/<string:id>/')
def teams_id(points='', id=''):
    team= []
    myList=[]
    for element in data:
        if element["points"] == points:
            myList.append(element)
    for element in myList:
        if element["ID"] == id:
            team.append(element)        
    # result = jsonify(car)
    return render_template("index.html",items=team)



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
