from flask import Flask
from flask import send_file
from flask import render_template
from flask import request
from flask import jsonify
from floaty import *

app = Flask(__name__)

@app.route("/")
def home():
    return "Website down! please contact IT for more information"

@app.route("/robots.txt")
def robots():
    return send_file('robots.txt')

@app.route("/contactIT", methods=['GET', 'POST'])
def submitted():
    f = floaty()
    if request.method == 'POST':
        content = request.get_json()
        sender = content.get('email')
        messege = content.get('messege')
        f.setSender(sender)
        f.checkResponds(messege)
    else:
        return "Post:Json Request Only"
    return "Email Sent!"

@app.route("/countdown")
def countdown():
    return render_template("countdown.html")

if __name__ == "__main__":
    app.run(
        debug=True,
        host='0.0.0.0',
        port=80,
        threaded=True
    )

