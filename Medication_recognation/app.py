#!/usr/bin/env python

from flask import Flask, render_template, Response
import io
from flask import Flask, flash, redirect, render_template, request, session, abort
import json
import cv2
from datetime import datetime
app = Flask(__name__)
vc = cv2.VideoCapture(0)
import dbConnection as dc
import time
from flask import jsonify

import capture




from flask import Flask, render_template, request, redirect, url_for, session 

import re 
 
from gtts import gTTS 

import os 


language = 'en'

  
app = Flask(__name__) 



@app.route('/hello')
def index():

    
    return render_template('index.html')




@app.route('/', methods=['GET','POST'])
def index1(): 
    #username=request.form['username']
    #password = request.form['password']
    #print(username)
    msg='welcome user'
    return render_template('login.html', msg = msg)


@app.route('/login_nav', methods=['GET','POST'])


def login_nav(): 
    
    msg='Fill details..'
    return render_template('login.html', msg = msg)

@app.route('/admin1', methods=['GET','POST'])
def admin1(): 
    msg='Fill details..'
    return render_template('add_medicine.html', msg = msg)

@app.route('/admin2', methods=['GET','POST'])
def admin2():  
    data=dc.db_fetch_all_medicine()
    
    return render_template('medicinelist.html', data = data) 
    

@app.route('/add_medicine', methods=['GET','POST'])


def add_medicine(): 
    
    msg='Medicine Added Successfully..'
    name=request.form['name1']
    brand_name=request.form['brand_name']
    type_=request.form['type_']
    text_=request.form['text_']
    use_=request.form['use_']
    mfg=request.form['mfg']
    expiry=request.form['expiry']
    doses=request.form['doses']
    colour=request.form['colour']
    capture.capture1(name)
    dc.db_add_medicine(name, brand_name, type_, text_, use_, mfg, expiry, doses,colour,name)
    return render_template('add_medicine.html', msg = msg) 


@app.route('/login', methods=['GET','POST'])

def login(): 
    username=request.form['username']
    password = request.form['password']
    print(username)
    if username=="admin" and password=="admin":
        msg='Welcome Admin'
        return render_template('admin_home.html', msg = msg)
    else:
        
        out=dc.db_login(username,password)
    
        if out=="yes":
        
            msg='login success'
            return render_template('user_home.html', msg = msg)
        else:
            msg='login Failed'
            return render_template('login.html', msg = msg)
        
  
@app.route('/logout') 
def logout(): 
   
    return redirect(url_for('login_nav')) 
  
@app.route('/register_nav', methods =['GET', 'POST'])
def register_nav():
    msg = 'Please fill details !'
    return render_template('register.html', msg = msg)
@app.route('/register', methods =['GET', 'POST'])
def register(): 
    msg = '' 
    

    name = request.form['name'] 
    password = request.form['password'] 
    email = request.form['email']
    mobile = request.form['mobile']
    address = request.form['address']
    r_mobile = request.form['r_mobile']
    disease = request.form['disease']
    print(name,password,email,mobile,address,r_mobile,disease)
       
    if not re.match(r'[^@]+@[^@]+\.[^@]+', email): 
            msg = 'Invalid email address !'
    elif not re.match(r'[A-Za-z0-9]+', name): 
            msg = 'Username must contain only characters and numbers !'
    
    else: 
            dc.db_register(name,password,email,mobile,address,r_mobile,disease)
            msg = 'You have successfully registered !'
    
    return render_template('register.html', msg = msg)  


@app.route('/med_list')


def med_list(): 
    
    msg='add'
    data=dc.db_fetch_all_medicine()
    
    return render_template('medicinelist.html', data = data) 


@app.route('/delete/<int:data>')


def delete(data): 
    
    msg='add'
    print(data)
    d=dc.delete(data)
    
    data=dc.db_fetch_all_medicine()
    
    return render_template('medicinelist.html', data = data)

import capture1
import img_compare as cmp
@app.route('/compare')
def compare(): 
    
    msg='add'
    name=capture1.capture1()
    mystring=dc.db_fetch_medicine(name)
    print(mystring)
    
    myobj = gTTS(text=mystring, lang=language, slow=False) 
  
 
    myobj.save("welcome.mp3") 
  
# Playing the converted file 
    os.system("welcome.mp3") 
    """Video streaming home page."""
    
    
    return render_template('medicinedetails.html', data = mystring) 


  
# Playing the converted file 
#os.system("welcome.mp3") 
     

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)
