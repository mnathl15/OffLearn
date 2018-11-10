from flask import Flask, jsonify, render_template
app = Flask(__name__, template_folder='templates')
from crawler import getFileNames, searchInternet
import os
 
@app.route("/search=<query>")
def search(query):
    searchInternet(query)
    resp = jsonify({"data": "Success"})
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route("/fileList")
def getFileList():
    data = getFileNames()
    dataJson=[topic.serialize() for topic in data]
    resp = jsonify({"data": dataJson})
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route('/topic=<topic>&filename=<filename>')
def getFile(topic, filename):
    path = topic + "/" + filename + ".html"
    file = open(path, "r")
    # rawText = file.read()
    rawText = "FIX ME"
    file.close()
    return rawText
 
if __name__ == "__main__":
    app.run()
