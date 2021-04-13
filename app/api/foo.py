from flask import Flask, Blueprint, render_template, request, jsonify, url_for, redirect


foo_bp = Blueprint('foo', __name__)


api_bp = Blueprint("api_bp", __name__)
@api_bp.route("/")
def get(self):
    return 'Hello, World!', 200