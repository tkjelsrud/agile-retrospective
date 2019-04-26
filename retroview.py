from flask import Flask, render_template, request, url_for, redirect, make_response, jsonify
import json, datetime
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["DEBUG"] = True
counter = 0

#db = SQLAlchemy(app)

class JsonModel(object):
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Board(JsonModel):
    id = 123

class Postit(JsonModel):
    id = 123
    #__tablename__ = "notes"
    #id = db.Column(db.Integer, primary_key=True)
    #scope = db.Column(db.Integer)
    #title = db.Column(db.String(1024))
    #typ = db.Column(db.String(128))
    #json = db.Column(db.String(8192))
    #dt = db.Column(db.DateTime, default = datetime.datetime.utcnow())

@app.route("/retro/board/<int:board_id>", methods=["GET", "POST", "DELETE"])
def board():
    if request.method == "GET":
        return make_response(jsonify({'result': 'Some text here'}), 200)

@app.route("/retro", methods=["GET"])
def index():
    if request.method == "GET":
        counter = counter + 1
        return make_response(jsonify({'result': 'Some text here' + counter}), 200)
        #return render_template("index.html")