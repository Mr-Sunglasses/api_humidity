from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('renderer.html')

app.run(port=5000, debug=True)