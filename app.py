from flask import Flask, jsonify
from flask_cors import CORS
from database.models import db

app = Flask(__name__)

# Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///rootcausez.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Enable CORS for Base44 frontend
CORS(app)

# Initialize database
db.init_app(app)

# Create database tables
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return jsonify({
        "status": "success",
        "message": "RootCauseZ Backend is running!"
    })


@app.route("/api/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "RootCauseZ ML Backend"
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
