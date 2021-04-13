from flask import Flask, Blueprint, render_template, request, jsonify, url_for, redirect


foo_bp = Blueprint('foo', __name__)


class Hello(Resource):
    def get(self):
        return 'Hello, World!', 200