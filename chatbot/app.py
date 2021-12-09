from flask import Flask  
from flask import render_template
from flask_cors import CORS, cross_origin

# creates a Flask application, named app
app = Flask(__name__, static_url_path='/static')

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# a route to display our html page gotten from [react-chat-widget](https://github.com/mrbot-ai/rasa-webchat)
@app.route("/")
@cross_origin()
def index():  
    return render_template('index.html')

# run the application
if __name__ == "__main__":  
    app.run(debug=True, host='0.0.0.0')