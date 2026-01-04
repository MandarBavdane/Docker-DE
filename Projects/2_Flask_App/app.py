from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Flask app running in a Docker container!'

@app.route('/about')
def about():
    return 'This is a simple Flask application running inside a Docker container!'

@app.route('/contact')
def contact():
    return 'Contact us at: mandarbavdane@gmail.com'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
