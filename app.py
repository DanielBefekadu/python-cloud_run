import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Hello from Cloud Run 🚀",
        "status": "ok"
    })

@app.route("/health")
def health():
    return "healthy", 200

if __name__ == "__main__":
    # Cloud Run provides PORT env variable
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
