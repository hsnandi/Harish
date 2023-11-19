from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Home"
'''
Some function of API include
GET
POST
PUT 
DELETE
'''


if __name__== "__main__":
    app.run(debug=True)
