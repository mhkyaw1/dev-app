from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world! Blah Blah version 2'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
