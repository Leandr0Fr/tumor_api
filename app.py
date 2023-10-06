from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "HOOOOLAAAA"
    
@app.route("/ping", methods=["GET"])
def ping():
    return jsonify(message='API on!'), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))