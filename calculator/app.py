from flask import Flask, render_template, request, jsonify, Response
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text1 = int(request.form['text1'])
    text2 = int(request.form['text2'])
    add =  text1 + text2    
    return render_template('result.html', data=add)
