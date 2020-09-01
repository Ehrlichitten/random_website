from flask import Flask, render_template, redirect, request
from PIL import Image
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('./index.html')

@app.route('/templates/<string:page_name>')
def every_page(page_name):
    return render_template(page_name)
def write_to_csv(data):
    with open ('data.csv',mode='a',newline='') as file:
        email = data["email"]
        info = data["info"]
        message = data["message"]
        writer = csv.writer(file, delimiter=' ',  quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(f'email:{email}, subject:{info}, message:{message}')
@app.route('/templates/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            print(data)
            return "done"
        except:
            return"such a shame:("
from flask import Flask, render_template, redirect, request
from PIL import Image
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('./index.html')

@app.route('/templates/<string:page_name>')
def every_page(page_name):
    return render_template(page_name)
def write_to_csv(data):
    with open ('data.csv',mode='a',newline='') as file:
        email = data["email"]
        info = data["info"]
        message = data["message"]
        writer = csv.writer(file, delimiter=' ',  quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(f'email:{email}, subject:{info}, message:{message}')
@app.route('/templates/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            print(data)
            return "done"
        except:
            return 'smth is clearly wrong'