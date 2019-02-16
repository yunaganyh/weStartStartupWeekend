from flask import (Flask, url_for, render_template,redirect,request,flash)
from flask_mail import Mail,Message
import sys,os
import random
from datetime import datetime, timedelta
app = Flask(__name__)
app.config['MAIL_SERVER']='imap.gmail.com'
app.config['MAIL_PORT'] = 993
app.config['MAIL_USERNAME'] = 'ygan@wellesley.edu'
app.config['MAIL_PASSWORD'] = 'Ekrus1996'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

app.secret_key = ''.join([ random.choice(('ABCDEFGHIJKLMNOPQRSTUVXYZ' +
                                          'abcdefghijklmnopqrstuvxyz' +
                                          '0123456789'))
                           for i in range(20) ])

@app.route('/', methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/email/', methods=['POST'])
def email():
    print(request.form)    
    try:
        name=request.form['name']
        email=request.form['email']
        message=request.form['message']
        print(name,email,message)
    except:
        print('couldnt access dict')
    try:
        msg = Message("Startup Weekend inquiry",sender=(name,email),recipients=['ygan@wellesley.edu'])
        msg.body = """
      From: %s <%s>
      %s
      """ % (name, email, message)
        mail.send(msg)
        flash('Message was successfully sent.')
    except Exception as err:
        print(err)
        flash('Message was not sent.' + str(err))
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0',8080)