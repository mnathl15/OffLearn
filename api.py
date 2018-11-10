from flask import Flask, jsonify
app = Flask(__name__)
from crawler import getFileNames
 
@app.route("/search=<query>")
def search(query):
    resp = jsonify({"data": "Hello World"})
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route("/fileList")
def getFileList(query):
    data = getFileNames()
    resp = jsonify({"data": data})
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route("/filename=<filename>")
def getFile(filename):
    resp = jsonify({"data": "Hello World"})
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp
 
if __name__ == "__main__":
    app.run()
