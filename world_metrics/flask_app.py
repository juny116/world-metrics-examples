from flask import Flask, jsonify
from .collector import collect_counters

def create_app(collector=collect_counters):
    app = Flask(__name__)
    @app.get("/all")
    def counters():
        return jsonify(collector())
    return app

if __name__ == "__main__":
    create_app().run(host="127.0.0.1", port=5000)
