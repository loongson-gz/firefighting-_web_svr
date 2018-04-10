#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#from flask_sqlalchemy import SQLAlchemy
import datetime
import time

from flask import Flask, render_template, request

import dbhepler
import readserial
from db.MysqlTool import app

finger_id = 0
car_id = 0
plate = ""
#app = Flask(__name__) 

##获取车辆数据
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
            tmp = [t[0], t[2]]
            checked_.append(tmp)
    return not_check_, checked_, not_mechanic_, mechanic_

#根据指纹跳转 
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
        return render_template('driver.html', level=level, department=department_, name=name_, car=L[4], t=w, year=y,month=m,day=d, items=items)
    elif level == 2:
        return render_template('mechanic.html', not_check=not_check_)
    elif level == 3:
        return render_template('leader.html', not_check=not_check_)
    else :
        dbhepler.update_finger_id(0)
        return render_template("gohome.html")
                        
        #return render_template('error.html')

#提交检查结果        
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

    print(request.values)
    table_cxt_ = request.form['table_cxt']
    print(table_cxt_)
    print("********************")        
    rows = table_cxt_.split("#")
    result = 0
    ret = []
    if len(rows) > 0:
        ret = rows[1:]
        tmp = rows[0].split(',')
        if len(tmp) >=3 :
            result = tmp[3].strip()
    
    for l in ret:
        if len(l) > 0:
            cols = l.split(',')
            print(cols) 
            desc = cols[3].strip()           
            if desc :
                compent = dbhepler.get_compent_id_by_name(cols[1].strip())
                dbhepler.update_record_desc(car_id, compent.id, desc)
                
    for qr in qr_L:   
        print("compent_qr_code--->",qr)
        compent = dbhepler.get_compent_by_qr_code(qr)
        for c in compent:
            print(L[0], car_id, c.id)
            dbhepler.update_record(L[0], car_id, c.id)

    compent_lst = []
    if level == 1:
        compent_lst = dbhepler.get_compent_lst_by_plate(L[4])
    else :
        compent_lst = dbhepler.get_compent_lst_by_plate(plate)
    
    compent_set = set(compent_lst)
    compent_l = list(compent_set)
    qr_L.sort()
    compent_l.sort()
    if len(compent_l) > 0 :
        bFinished = 0
    else :
        bFinished = 1
            
    if bFinished == 1:
        print("finished .....")
        #更新task 表
        dbhepler.update_task(car_id, 3, int(result)) 
        if level == 1:
            finger_id = 0
            dbhepler.update_finger_id(0)
            return render_template("success.html")
        elif level == 2:
            not_check_, checked_, not_mechanic_, mechanic_ = get_plate_data()
            return render_template('mechanic.html', not_check=not_check_)
        elif level == 3:
            not_check_, checked_, not_mechanic_, mechanic_ = get_plate_data()
            return render_template('leader.html', not_check=not_check_)
        else :
            dbhepler.update_finger_id(0)
            return render_template("gohome.html")      
    else :
        print("unfinished .....")        
        today=datetime.date.today()
        y = today.year
        m = today.month
        d = today.day
        w, items = dbhepler.get_compent_by_car_id(car_id)
        return render_template("driver_not_finished.html", level=level, department=department_, name=name_, car=L[4], t=w, year=y,month=m,day=d, items=items)
    

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

##提交成功
@app.route('/success', methods=['GET'])
def go_sucess():
    finger_id = 0
    dbhepler.update_finger_id(0)
    return render_template("success.html")

##回到主页
@app.route('/gohome', methods=['GET'])
def go_home():
    global finger_id
    finger_id = 0
    dbhepler.update_finger_id(0)
    return render_template("gohome.html")

## 领导或技师检查车辆
@app.route('/gotocar', methods=['POST'])
def goto_check_car():
    print("goto check car ....")
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
    return render_template('driver.html', level=level, department=department_, name=name_, car=plate, t=w, year=y,month=m,day=d, items=items)

## 查看已检查车辆
@app.route('/viewcar', methods=['POST'])
def goto_view_car():
    print("viewcar ....")
    global plate
    plate = request.form['plate_num']
    print("plate:",plate)
    today=datetime.date.today()
    y = today.year
    m = today.month
    d = today.day
    car_ = dbhepler.get_car_id_by_plate(plate)
    w, items = dbhepler.get_compent_by_car_id(car_.id)
    return render_template('view_car.html',  car=plate, t=w, year=y,month=m,day=d, items=items)


if __name__ == '__main__':
    #重启后重置为无人使用状态
    dbhepler.update_finger_id(0)
    #readserial.start_get_finger()
    app.run()
