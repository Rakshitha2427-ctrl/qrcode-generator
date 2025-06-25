import io,base64
from qrcode import QRCode
from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)
# print(__name__)#__main__
@app.route('/',methods=['GET','POST'])
def index():
    if request.method =='POST':
        qr = QRCode(border=10)
        data=request.form['data']
        qr.add_data("data")
        qr.make(fit=True)
        img =qr.make_image(fill_color='orange',back_color='pink')
        buffer=io.BytesIO()
        img.save(buffer,format='PNG')
        img_str=base64.b64encode(buffer.getvalue()).decode('utf-8')
        return redirect(url_for('qrcode',img_str=img_str))
        # img.show()
    return render_template('index.html')
@app.route('/qrcode')
def qrcode():
    img_str=request.args.get('img_str')
    return render_template('qrcode.html',img_str=img_str)

if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)



