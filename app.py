# Updated by bot: Use an environment variable to toggle debug mode: app.run(host='0.0.0.0', port=5000, debug=os.environ.get('FLASK_DEBUG', 'False').lower() == 'true')
# Updated by bot: Use an environment variable to toggle debug mode: app.run(host='0.0.0.0', port=5000, debug=os.environ.get('FLASK_DEBUG', 'False').lower() == 'true')
# Updated by bot: applied full fix
python
from flask import Flask
import logging
import os

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    app.logger.info("Home route accessed")
    return "Hello from Ashapp Backend running on Kubernetes!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=os.environ.get('FLASK_DEBUG', 'False').lower() == 'true')