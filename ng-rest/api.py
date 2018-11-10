from flask import Flask, jsonify
app = Flask(__name__)
from crawler import getFileNames
 
@app.route("/search=<query>")
def search(query):
    print(query)
    resp = jsonify({"data": "Hello World"})
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route("/fileList")
def getFileList():
    data = getFileNames()
    dataJson=[topic.serialize() for topic in data]
    resp = jsonify({"data": dataJson})
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route("/filename=<filename>")
def getFile(filename):
    resp = jsonify({"data": "Hello World"})
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return app.send_static_file("data/" + filename)
 
if __name__ == "__main__":
    app.run()
