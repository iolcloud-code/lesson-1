from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'My first flask Project'

def app():
    app.run(host='0.0.0.0', port=$PORT)
