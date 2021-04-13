from flask import Flask, Blueprint, render_template, request, jsonify, url_for, redirect
from flask_restful import Api, Resource

import requests
import json

import pymysql
import os

app = Flask(__name__)
api = Api(app)

class Koctank(Resource):
    def get(self):
        return {"octank": "abp test"}

api.add_resource(Koctank, '/test')


general_bp = Blueprint("general_bp", __name__ , template_folder="templates/general", static_url_path="/static")
@general_bp.route("/")
def home():
    return render_template("index.html", title="Home")



@general_bp.route("/analytic")
def analytics():
	return redirect('https://57gq98nfmg.execute-api.us-east-1.amazonaws.com/test/anonymous-embed-sample')


@general_bp.route("/search")
def search():
    query = request.args['keyword']
    products = requests.get("http://localhost:5000/api/products/groceries/"+query)
    return render_template("search_results.html",search_results={"products":products.json(), "number":len(products.json())}, title=query)

