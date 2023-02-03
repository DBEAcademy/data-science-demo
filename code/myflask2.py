from flask import Flask, request

app23 = Flask(__name__)

@app23.route("/")
def hello_world():
    return "<h1>Test</h1><p>Hello, World!</p>"



@app23.route("/temperatur", methods = ['GET', 'POST'] )
def hello_userhzhhh2():
    if request.method == 'POST':
        print(request.form['temp'])
        datei = open('temperatur.txt', 'w')
        datei.write(request.form['temp'])

        return request.form['temp']
    else:

        datei = open('temperatur.txt', 'r')
       # print(datei.read())

        return datei.read()

