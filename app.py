from flask import Flask,render_template ,request ,send_file 
import qrcode as qr

app = Flask(__name__)

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