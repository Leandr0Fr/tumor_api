from flask import Flask, request, jsonify, render_template, make_response
import os
from model import prediction
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@cross_origin
@app.route('/')
def index():
    return render_template("index.html")

@cross_origin
@app.route("/ping", methods=["GET"])
def ping():
    response = make_response(jsonify(message='API on!'))
    response.status_code = 200
    return response

@cross_origin
@app.route('/predict', methods=['POST'])
def predict():
    #Recibe y guarda la imagen
    image = request.files['image']
    if image.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        image.save("image.png")
        return jsonify(message = prediction()), 200
    else:
        response = make_response(jsonify(message="I'm a teapot!"))
        response.status_code = 418
        return response 
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))