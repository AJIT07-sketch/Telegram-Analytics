from flask import Flask, jsonify, request
import logging
import os
from logs_config import app_logger, error_logger  # Import logging setup
from code_file import total_groups, group_type_distribution
from auth import authenticate_request

app = Flask(__name__)

@app.route("/")
def home():
    app_logger.info("Home endpoint accessed")
    return jsonify({"message": "Telegram Analytics Dashboard Running!"})

@app.route("/analytics/total_groups")
def total_groups_api():
    token = request.headers.get("Authorization")
    if not token or not authenticate_request(token):
        error_logger.error("Unauthorized access to total_groups")
        return jsonify({"error": "Unauthorized"}), 401

    try:
        count = total_groups()
        app_logger.info("Fetched total group count successfully.")
        return jsonify({"total_groups": count})
    except Exception as e:
        error_logger.error(f"Error fetching total groups: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500

@app.route("/analytics/group_type_distribution")
def group_type_distribution_api():
    token = request.headers.get("Authorization")
    if not token or not authenticate_request(token):
        error_logger.error("Unauthorized access to group_type_distribution")
        return jsonify({"error": "Unauthorized"}), 401

    try:
        distribution = group_type_distribution()
        app_logger.info("Fetched group type distribution successfully.")
        return jsonify(distribution)
    except Exception as e:
        error_logger.error(f"Error fetching group type distribution: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == "__main__":
    app.run(debug=True)

