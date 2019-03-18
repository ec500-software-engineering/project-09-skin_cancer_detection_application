from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route("/") # Home Directory 
def home_dir():
    return "Welcome to Home Dir"

@app.route("/photo_ML", methods = ['GET'])
def photo_classify():
    img_data = {request.data}
    return jsonify(img_data), 200


if __name__ == "__main__":
    app.run(debug=True)