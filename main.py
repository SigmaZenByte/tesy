from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route("/delay")
def delay():
    time.sleep(60)
    return jsonify({"status": "success", "message": "Response after 1 minute"})

def handler(request):
    return app(request.environ, lambda *args: None)
