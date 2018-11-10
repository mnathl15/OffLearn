from flask import Flask, jsonify, render_template
app = Flask(__name__, template_folder='templates')
from crawler import getFileNames, searchInternet
import os, pdfkit
 
@app.route("/search=<query>")
def search(query):
    print(query)
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
 
if __name__ == "__main__":
    app.run()
