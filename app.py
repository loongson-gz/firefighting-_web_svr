#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template
from db.MysqlTool import app
#from flask_sqlalchemy import SQLAlchemy
import datetime
import time
import dbhepler
import readserial

finger_id = 0
car_id = 0
plate = ""
#app = Flask(__name__) 

def get_plate_data():
    L = dbhepler.get_task()
    not_check_ = []
    checked_ = []
    not_mechanic_ = []
    mechanic_ = []
    for t in L:
        if t[1] == 0:
            not_check_.append(t[0])
        elif t[1] == 1:
            not_mechanic_.append(t[0])
        elif t[1] == 2:
            mechanic_.append(t[0])
        elif t[1] == 3:
            checked_.append(t[0])
    return not_check_, checked_, not_mechanic_, mechanic_

@app.route('/', methods=['GET', 'POST'])
def home():
    global finger_id
    finger_id = readserial.get_finger_id()
    print("finger_id:",finger_id)
    
    not_check_, checked_, not_mechanic_, mechanic_ = get_plate_data()
    if finger_id == 0:
        #return render_template('home.html') 
        return render_template('home.html', not_check_car=not_check_, not_mechanic_car=not_mechanic_, mechaniced_car=mechanic_, checked_car=checked_)
    else:
        return render_template('gosignin.html')         
        #return render_template('home_jump.html', not_check_car=not_check_, checked_car=checked_, not_mechanic_car=not_mechanic_, mechaniced_car=mechanic_)

##进入登录页         
@app.route('/signin', methods=['GET'])
def signin_form():
    #finger_id = readserial.get_finger_id()
    print("finger_id:",finger_id)
    ret = dbhepler.get_info_by_finger_id(finger_id)
    if len(ret) == 0:
        dbhepler.update_finger_id(0)
        return render_template("gohome.html")
        #return render_template('error.html')
    L = ret[0]
    print(L)
    level = L[-1]
    name_ = L[1]
    department_ = L[2]
    global car_id
    car_id = L[3]

    today=datetime.date.today()
    y = today.year
    m = today.month
    d = today.day
    w, items = dbhepler.get_compent_by_car_id(car_id)
    not_check_, checked_, not_mechanic_, mechanic_ = get_plate_data()
    if level == 1:
        #return render_template('driver.html')
        return render_template('driver.html', department=department_, name=name_, car=L[4], t=w, year=y,month=m,day=d, items=items)
    elif level == 2:
        return render_template('mechanic.html', not_check=not_check_)
    elif level == 3:
        return render_template('leader.html', not_check=not_check_)
    else :
        dbhepler.update_finger_id(0)
        return render_template("gohome.html")
                        
        #return render_template('error.html')

#提交        
@app.route('/signin', methods=['POST'])
def signin():
    print("***********qr_code***************")    
    qr_code = request.form['qr_code_text']
    qr_lst = qr_code.split('\n')
    tmp = []
    for line in qr_lst:
        s = line.strip()
        if s:
            tmp.append(s)
    qr_s = set(tmp)
    qr_L = list(qr_s)
    print(qr_L)
    bFinished = 0 

    finger_id = readserial.get_finger_id()
    ret = dbhepler.get_info_by_finger_id(finger_id)
    L = ret[0]
    print(L)
    level = L[-1]
    name_ = L[1]
    department_ = L[2]   
    compent_lst = []
    if level == 1:
        compent_lst = dbhepler.get_compent_lst_by_plate(L[4])
    else :
        compent_lst = dbhepler.get_compent_lst_by_plate(plate)
    
    compent_set = set(compent_lst)
    compent_l = list(compent_set)
    if len(compent_l) != len(qr_L):
         bFinished = 0
    else :
        qr_L.sort()
        compent_l.sort()
        if qr_L == compent_l:
            bFinished = 1
    
    for qr in qr_L:   
        print("compent_qr_code--->",qr)
        compent = dbhepler.get_compent_by_qr_code(qr)
        for c in compent:
            print(L[0], car_id, c.id)
            dbhepler.update_record(L[0], car_id, c.id)
            
    if bFinished == 1:
        print("finished .....")
        #更新task 表
        dbhepler.update_task(car_id, 3) 
        if level == 1:
            finger_id = 0
            dbhepler.update_finger_id(0)
            return render_template("success.html")
        elif level == 2:
            not_check_, checked_, not_mechanic_, mechanic_ = get_plate_data()
            return render_template('mechanic.html', not_check=not_check_)
        elif level == 3:
            go_home()       
    else :
        print("unfinished .....")        
        today=datetime.date.today()
        y = today.year
        m = today.month
        d = today.day
        w, items = dbhepler.get_compent_by_car_id(car_id)
        return render_template("driver_not_finished.html", department=department_, name=name_, car=L[4], t=w, year=y,month=m,day=d, items=items)
    

@app.route('/commit', methods=['GET'])
def commit_get():
    home()

@app.route('/commit', methods=['POST'])
def commit():
    print("commit ......................")
    #items = request.form['table_items']    
    #print(items)
    dbhepler.update_finger_id(0)
    return render_template("jump.html")


@app.route('/mechanic', methods=['GET'])
def mechanic_tech():
    return render_template("t_fixed.html")


@app.route('/success', methods=['GET'])
def go_sucess():
    finger_id = 0
    dbhepler.update_finger_id(0)
    return render_template("success.html")


@app.route('/gohome', methods=['GET'])
def go_home():
    global finger_id
    finger_id = 0
    dbhepler.update_finger_id(0)
    return render_template("gohome.html")

## 领导或技师检查车辆
@app.route('/gotocar', methods=['POST'])
def go_to_car():
    print("gotocar ....")
    global plate
    plate = request.form['plate_num']
    print("plate:",plate)
    print("finger_id:",finger_id)
    ret = dbhepler.get_info_by_finger_id(finger_id)
    if len(ret) == 0:
        return render_template('error.html')
    L = ret[0]
    print(L)
    level = L[-1]
    name_ = L[1]
    department_ = L[2]
    today=datetime.date.today()
    y = today.year
    m = today.month
    d = today.day
    car_ = dbhepler.get_car_id_by_plate(plate)
    global car_id
    car_id = car_.id
    w, items = dbhepler.get_compent_by_car_id(car_id)
    return render_template('driver.html', department=department_, name=name_, car=plate, t=w, year=y,month=m,day=d, items=items, level=level)

if __name__ == '__main__':
    readserial.start_get_finger()
    app.run()