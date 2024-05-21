from flask import Flask, request
import requests
import django

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the vulnerable Flask app!"

@app.route('/fetch')
def fetch():
    url = request.args.get('url')
    if url:
        response = requests.get(url)
        return response.content
    return "No URL provided."

if __name__ == '__main__':
    app.run(debug=True)

