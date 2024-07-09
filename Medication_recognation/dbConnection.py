import mysql.connector as con
import sys
import mysql
from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%Y/%m/%d %H/%M/%S")
import json
def db_login(email, password):
        
        db = con.connect(host="localhost", user="root", password="7777777", database="db_medicine")
        cur = db.cursor()
    
        query="SELECT *  FROM tbl_patient where email='"+email+"' and password='"+password+"'"
        cur.execute(query)
        names=cur.fetchall()
        if(int(len(names))>0):
            print("User Available")
            return "yes"
        else:
             return "no"
        
        


def db_register(name,password,email,mobile,address,r_mobile,disease):
        
        db = con.connect(host="localhost", user="root", password="7777777", database="db_medicine")
        cur = db.cursor()
    
        query="SELECT *  FROM tbl_patient where email='"+email+"'"
        cur.execute(query)
        names=cur.fetchall()
        if(int(len(names))>0):
            print("User already exist..")
        
           
                                
        else:
                query="insert into tbl_patient(name, password, email, mobile, address, r_mobile, disease) values(%s,%s,%s,%s,%s,%s,%s)"
                value=[name, password, email, mobile, address, r_mobile, disease]
                cur.execute(query,value)
                db.commit()
            
        
        
                print('Inserted')
        





#check_insert_or_update('apple',10.0,23,dt_string)     
def db_add_medicine(name, brand_name, type_, text_, use_, mfg, expiry, dosage,colour,l_name):
        
        db = con.connect(host="localhost", user="root", password="7777777", database="db_medicine")
        cur = db.cursor()
    
        
        query="insert into tbl_medicine(name, brand_name, type_, text_, use_, mfg, expiry, dosage,colour,l_name) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        value=[name, brand_name, type_, text_, use_, mfg, expiry, dosage,colour,l_name+".jpg"]
        cur.execute(query,value)
        db.commit()
            
        
        
        print('Inserted')

def delete(id):
        
        db = con.connect(host="localhost", user="root", password="7777777", database="db_medicine")
        cur = db.cursor()
    
        
        query="delete from tbl_medicine where id='"+str(id)+"' "
        
        cur.execute(query)
        db.commit()
            
        
        
        print('deleted')
def db_fetch_all_medicine():
        
        db = con.connect(host="localhost", user="root", password="7777777", database="db_medicine")
        cur = db.cursor()
    
        query="SELECT *  FROM tbl_medicine"
        cur.execute(query)
        #names=cur.fetchall()
        print("hello")
        row_headers=[x[0] for x in cur.description]
        
        rv = cur.fetchall()
        print(rv)
        return rv
##        json_data=[]
##        for result in rv:
##                json_data.append(dict(zip(row_headers,result)))
##        return json.dumps(json_data)
##        
##        
            

def db_fetch_medicine(name):
        
        db = con.connect(host="localhost", user="root", password="7777777", database="db_medicine")
        cur = db.cursor()
        ss="no"
        query="SELECT *  FROM tbl_medicine where l_name='"+name+"'"
        cur.execute(query)
        #names=cur.fetchall()
        row_headers=[x[0] for x in cur.description] #this will extract row headers
        rv = cur.fetchall()
        json_data=[]
        
        for result in rv:
                print(result)
               
               
                ss="The medicine name is  "+ result[1]+" , brand name is  "+result[2] +" , medicine type is "+result[3]+" , Uses of medicine are "+ result[5] +" , doses are "+result[8]+" , it will get expired on "+ result[7] 
                print(ss)
                
        return ss
            
        
          
                                
##def db_add_medicine1(row):
##        
##        db = con.connect(host="localhost", user="root", password="root", database="db_medicine")
##        cur = db.cursor()
##        print(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9])
##        
##        query="insert into tbl_medicine(name, brand_name, type_, text_, use_, mfg, expiry, dosage,colour,l_name) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
##        value=[row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]+".jpg"]
##
##         
##        cur.execute(query,value)
##        db.commit()
##            
##        
##        
##        print('Inserted')        
##from csv import reader
### open file in read mode
##with open('data.csv', 'r') as read_obj:
##    # pass the file object to reader() to get the reader object
##    csv_reader = reader(read_obj)
##    # Iterate over each row in the csv using reader object
##    for row in csv_reader:
##        
##       # print(row)
##        db_add_medicine1(row) 
