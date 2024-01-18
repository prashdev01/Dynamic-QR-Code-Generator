from flask import Flask,render_template ,request ,send_file 
import qrcode as qr
from flask import Flask, render_template, request
from flask_pymongo import pymongo
from urllib.parse import quote_plus
import pymongo

app = Flask(__name__)



client =pymongo.MongoClient("mongodb+srv://prashantwadhave5:Prash2002@cluster0.wkfocs3.mongodb.net/?retryWrites=true&w=majority")
db = client.test
db = client.DYNAMIC_QR_GENERATOR  # Use your actual database name
collection = db['contact_list'] 

@app.route('/submit_contact_form', methods=['POST'])
def submit_contact_form():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        print(f"Name: {name}, Email: {email}, Message: {message}")

        # Store the form data in MongoDB
        collection.insert_one({
            'name': name,
            'email': email,
            'message': message
        })

        return  render_template('formsub.html')
    else:
        return "Method Not Allowed", 405

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    url = request.form.get('url')
    if not url:
        return "Please enter a URL"

    # Genrate QR code 
    
    img = qr.make(url)
    img.save("./static/qrcode.png")
    # return send_file("static/qrcode.png" ,as_attachment=True),
    return render_template('qr_gen.html')
# Disable caching for development
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

    
if __name__ == ('__main__'):
    app.run(debug=True)