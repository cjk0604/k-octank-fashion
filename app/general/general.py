from flask import Flask, Blueprint, render_template, request, jsonify, url_for, redirect

import requests
import json

import pymysql
import os

rds_host = os.environ['DATABASE_HOST']
db_user = os.environ['DATABASE_USER']
password = os.environ['DATABASE_PASSWORD']
db_name = os.environ['DATABASE_DB_NAME']
port = 3306




general_bp = Blueprint("general_bp", __name__ , template_folder="templates/general", static_url_path="/static")
@general_bp.route("/")
def home():
    conn = pymysql.connect(rds_host, user=db_user, passwd=password, db=db_name, connect_timeout=10000, port=port, charset='utf8mb4')

    try:
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = 'select * from fashion limit 10;'
            cursor.execute(sql)
            rs = cursor.fetchall()
            for row_1 in rs:
                for row in rs:
                    print(row)
    finally:
        conn.commit()
        conn.close()
    return render_template("index.html", title="Home")

@general_bp.route("/analytic")
def analytics():
	return redirect('https://57gq98nfmg.execute-api.us-east-1.amazonaws.com/test/anonymous-embed-sample')

@general_bp.route("/search")
def search():
    query = request.args['keyword']
    products = requests.get("http://localhost:5000/api/products/groceries/"+query)
    return render_template("search_results.html",search_results={"products":products.json(), "number":len(products.json())}, title=query)

