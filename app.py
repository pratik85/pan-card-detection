from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask App is running successfully on Windows 🚀"

@app.route("/api/health")
def health():
    return jsonify({
        "status": "OK",
        "message": "Application is healthy"
    })

if __name__ == "__main__":
    app.run(debug=True)
