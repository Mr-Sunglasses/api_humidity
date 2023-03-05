from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

# my_webpage = requests.get('http://127.0.0.1:5000/')




from flask import Flask, jsonify, request



app = Flask(__name__)


@app.route('/temperature', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):
        my_webpage = requests.get('http://127.0.0.1:5000/')
        # my_webpage = requests.get('https://fluffy-bubblegum-36cf63.netlify.app/')
        my_webpage_data = my_webpage.text
        my_soup = BeautifulSoup(my_webpage_data, 'html.parser')
        get_temperature = (my_soup.find(id="temperature").get_text())

        return jsonify({'temperature': get_temperature})
  
@app.route('/humidity', methods = ['GET', 'POST'])
def humidity():
    if(request.method == 'GET'):
        my_webpage = requests.get('https://fluffy-bubblegum-36cf63.netlify.app/')
        my_webpage_data = my_webpage.text
        my_soup = BeautifulSoup(my_webpage_data, 'html.parser')
        get_humidity = (my_soup.find(id="temperature").get_text())
        return jsonify({'humidity': get_humidity})
    


if __name__ == '__main__':
  
    app.run(port=5050 ,debug = True)
