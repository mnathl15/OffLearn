from flask import Flask, jsonify, render_template, send_file
app = Flask(__name__, template_folder='templates')
from crawler import getFileNames, searchInternet

import os, pdfkit
 
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

@app.route("/file/<folder>/<filename>")
def getFileByPath(folder,filename):
    path = "../data/" + folder + "/" + filename
    return send_file(open(path, 'rb'), attachment_filename='file.pdf')
 
if __name__ == "__main__":
    app.run()
