from flask import Flask
from flask import request
from flask import jsonify
app = Flask(__name__)

@app.route("/api/order", methods = ["GET"])
def test():
	return jsonify(success = True)

@app.route("/api/test_order", methods = ["POST"])
def test_post():
	print(request.form)
	return jsonify(success = True)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)