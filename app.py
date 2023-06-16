from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'My first flask Project'

if __name__ == '__main__':
    app.run(HOST='0.0.0.0', PORT=5000)
