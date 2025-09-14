
# Updated by bot: Ensure debug mode is disabled in production by setting debug=False or using an environment variable: app.run(host='0.0.0.0', port=5000, debug=os.environ.get('FLASK_DEBUG', 'False').lower() == 'true')
# Updated by bot: Add 'from flask import Flask' at the beginning of the file.
# Updated by bot: Ensure debug mode is disabled in production by setting debug=False or using an environment variable.
import os

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    app.logger.info("Home route accessed")
    return "Hello from Ashapp Backend running on Kubernetes!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=os.environ.get('FLASK_DEBUG', 'False').lower() == 'true')