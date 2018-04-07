import datetime
import time
import calendar
from db.MysqlTool import db
#from MysqlModel import Member, Role
from MysqlModel import *
from log.log import *


#############################################################################
def get_all_car():
    logging.debug("==========================all car========================")    
    L = Car.query.all()
    for car in L:
        print(car.id, car.plate_num,  car.member_id)
    return L

def get_all_car_compent():
    logging.debug("==========================get_all_car_compent========================")    
    L = CarCompent.query.all()
    for r in L:
        print(r.id, r.name, r.qr_code)
    return L

def get_all_member():
    logging.debug("==========================get_all_member========================")    
    L = Member.query.all()
    for r in L:
        print(r.id, r.finger_id, r.name, r.department, r.role_id)
    return L

def get_all_role():
    logging.debug("==========================all role========================")
    L = Role.query.all()
    for r in L:
        print(r.id, "-->", r.name, "-->", r.level)
    return L


def get_all_record():
    logging.debug("==========================get_all_Record========================")    
    L = Record.query.all()
    for r in L:
        print(r.id, r.car_id, r.member_id, r.compent_id, r.check_status, r.compent_status, r.desc, r.date, r.time)
    return L

def get_all_record_mechanic():
    logging.debug("==========================get_all_Record_Mechanic=======================")    
    L = Record_Mechanic.query.all()
    for r in L:
        print(r.id, r.record_id, r.status, r.desc, r.date, r.time)
    return L

def get_all_record_leader():
    logging.debug("==========================get_all_Record_Leader========================")    
    L = Record_Leader.query.all()
    for r in L:
        print(r.id, r.record_mechanic_id, r.status, r.desc, r.date, r.time)
    return L


def get_all_task():
    logging.debug("==========================get_all_Task========================")    
    L = Task.query.all()
    for r in L:
        print(r.id, r.car_id, r.status, r.date)
    return L

def get_all_task_normal():
    logging.debug("==========================get_all_Task_Normal========================")    
    L = Task_Normal.query.all()
    ret = []
    for r in L:
        print(r.id, r.compent_id)
        tmp=[r.id, r.compent_id]
        ret.append(tmp)
    return ret

def get_all_task_week():
    logging.debug("==========================get_all_Task_Week========================")    
    L = Task_Week.query.all()
    ret = []
    for r in L:
        print(r.id, r.compent_id)
        tmp=[r.id, r.compent_id]
        ret.append(tmp)
    return ret

def get_all_task_month():
    logging.debug("==========================get_all_Task_Month========================")    
    L = Task_Month.query.all()
    ret = []
    for r in L:
        print(r.id, r.compent_id)
        tmp=[r.id, r.compent_id]
        ret.append(tmp)
    return ret

##########################################查询所有###################################
def get_all_data():
     get_all_car()
     get_all_car_compent()
     get_all_member()
     get_all_role()
     get_all_record()
     get_all_record_mechanic()
     get_all_record_leader()
     get_all_task()
     get_all_task_normal()
     get_all_task_week()
     get_all_task_month()
     #get_all_record()

##########################################更新所有###################################
def update_finger_id(id):
    finger = Param.query.filter_by(id=1).first()
    finger.finger_id = id
    db.session.add(finger)
    db.session.commit()
    
def update_record(member_id, car_id, compent_id):
    #dt_now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    #dt = '{}{}'.format(datetime.date.today(), " 00:00:00")
    dt=datetime.date.today()
    dt_now = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    tm_now = time.strftime('%H:%M:%S', time.localtime(time.time()))
    print(dt)
    #r = Record.query.filter_by(car_id=car_id, compent_id=compent_id, date_time=dt_now).first()
    #r.member_id = member_id
    #r.date_time = dt_now
    #r.check_status = 1
    #db.session.add(r)
    #db.session.commit()
    tmp="update t_record set member_id={mem_id}, date='{now}', time='{time}', check_status=1 WHERE car_id={car_id} and compent_id={compent_id} and date='{dt}'"
    sql=tmp.format(mem_id=member_id, now=dt_now, time=tm_now, car_id=car_id, compent_id=compent_id, dt=dt)
    print(sql)
    db.session.execute(sql)

def update_record_desc(car_id, compent_id, desc):
    dt=datetime.date.today()
    print(dt)
    #r = Record.query.filter_by(car_id=car_id, compent_id=compent_id, date_time=dt_now).first()
    #r.member_id = member_id
    #r.date_time = dt_now
    #r.check_status = 1
    #db.session.add(r)
    #db.session.commit()
    tmp="update t_record set `desc`='{desc}' WHERE car_id={car_id} and compent_id={compent_id} and date='{dt}'"
    sql=tmp.format(desc=desc, car_id=car_id, compent_id=compent_id, dt=dt)
    print(sql)
    db.session.execute(sql)
#############################################################################

def get_role(id):
   role = Role.query.filter_by(id=id).first()
   print(role.id, "-->", role.name, "-->", role.level) 
   return role

def get_mem(id):
    print("===============================================id", id)
    mem = Member.query.filter_by(finger_id=id).first()
    print(mem.name, "--->", mem.department, "--->",mem.role_id)
    mem_role = get_role(mem.id)
    return mem, mem_role
##
def get_task_by_date(d):
    L = Task.query.filter_by(date=d)
    ret = []
    for i in L:
        tmp =[i.car_id, i.status]
        ret.append(tmp)
    return ret

def get_car_by_id(id):
    c = Car.query.filter_by(id=id).first()
    #print(c)
    return c

#获取部件名称
def get_compent_by_id(id):
    compent = CarCompent.query.filter_by(id=id).first()
    return compent

#获取记录
def get_record_by_car_id(id, dt):
    r = Record.query.filter_by(car_id=id, date=dt)
    return r

#获取当前输入的指纹
def get_finger_id():
    p = Param.query.filter_by(id=1).first()
    return p.finger_id

def get_compent_by_qr_code(qr):
   L= CarCompent.query.filter_by(qr_code=qr)
   return L

def get_compent_id_by_name(name):
    L= CarCompent.query.filter_by(name=name).first()
    return L

def get_compent_info_by_car_id(id):
    c=CarCompent.query.filter_by(car_id=id)
    return c

#############################################################################
#获取任务类型： 0：日常， 1：周日， 2：月底
def get_task_type():
    today=datetime.date.today()
    dayofweek = today.isoweekday()
    dayofmonth = today.day
    day_now = time.localtime()
    wday,month_range = calendar.monthrange(day_now.tm_year, day_now.tm_mon)
    print("dayofweek", dayofweek, "dayofmonth:", dayofmonth, "month_range:", month_range)
    # 0 日常 1 周日 2 月末
    t = 0
    if dayofmonth == month_range:
        print("month")
        t = 2
    elif dayofweek == 7:
        print("week")        
        t = 1        
    else:
        print("normal")                
        t = 0     
    return t

#获取当天的车辆待检测项
def get_compent():
    L = []
    # 0 日常 1 周日 2 月末
    t = get_task_type()
    if t == 2:
        print("month")
        L = get_all_task_month()
    elif t == 1:
        print("week")        
        L = get_all_task_week()
    else:
        print("normal")                
        L = get_all_task_normal()
    return L

#添加待检测车辆的部件
def add_compent():
    print("=====================add_compent")
    #dt = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    dt = datetime.date.today()
    tm = "00:00:00"
    ret = get_all_car()
    for c in ret :
        print("--------------->", c.id)
        L = get_compent_info_by_car_id(c.id)        
        for t in L:
            print("----compent:", t.id, t.name)
            r = Record(car_id=c.id, member_id=c.member_id, compent_id=t.id, date=dt, time=tm)
            db.session.add(r)
    db.session.commit()

#添加待检测车辆
def add_task():
    print("=====================add_task")
    today = datetime.date.today()
    ret = get_all_car()
    for c in ret :
        print(c.id)
        t = Task(car_id=c.id, date=today)
        db.session.add(t)
    db.session.commit()


#获取当天的车辆查检测情况(粤A12345 0)
def get_task():
    today = datetime.date.today()
    print(today)
    taskList = get_task_by_date(today)
    if len(taskList) == 0 :
        add_task()
        add_compent()
    taskList = get_task_by_date(today)    
    L = []
    for t in taskList:
        #print(t.status)
        c = get_car_by_id(t[0])
        print(c.plate_num, t[1], t[0])
        r = [c.plate_num, t[1], t[0]]
        L.append(r)
    return L

#获取当天的车辆待检测项及检测状态
def get_compent_by_car_id(id):
    t = get_task_type()
    today=datetime.date.today()
    L = get_record_by_car_id(id, today)
    ret = []
    i = 1
    for r in L: 
        compent = get_compent_by_id(r.compent_id)
        tmp = [i, compent.name, r.check_status, r.compent_status, r.desc]
        i = i+1
        ret.append(tmp)
    return t, ret

#通过指纹获取信息 ('张三', '三班', 1, '粤A12345', 1)
def get_info_by_finger_id(id):
    tmp="select a.id, a.name, a.department, b.id, b.plate_num, c.level from t_member a left join t_car b on a.id=b.member_id left join t_role c on a.role_id=c.id where a.finger_id={id}"
    sql=tmp.format(id=id)
    L = db.session.execute(sql)
    ret = []
    for r in L:
        print(r)
        ret.append(r)
    return ret

def update_task(car_id, status):
    today=datetime.date.today()
    t = Task.query.filter_by(car_id = car_id, date=today).first()
    t.status = status
    db.session.add(t)
    db.session.commit()


def get_car_id_by_plate(plate):
    print("plate:", plate)
    c = Car.query.filter_by(plate_num=plate).first()
    return c
    #tmp="select id from t_car where plate_num='{plate}'"
    #sql=tmp.format(plate=plate)
    #L = db.session.execute(sql)
    #ret = []
    #for r in L:
     #   print(r)
     #   ret.append(r)
    #return ret

#通过车牌号及日期来查部件
'''
def get_compent_lst_by_plate(plate):
    c = get_car_id_by_plate(plate)
   # today=datetime.date.today()
    print(c.id, plate)
    r = CarCompent.query.filter_by(car_id=c.id)
    L = []
    for i in r:
        L.append(i.qr_code)
    return L
'''

def get_compent_lst_by_plate(plate):
    c = get_car_id_by_plate(plate)
    print(c.id, plate)
    today=datetime.date.today()
    r = Record.query.filter_by(car_id=c.id, check_status=0, date=today)
    L = []
    for i in r:
        compent_=CarCompent.query.filter_by(id=i.compent_id).first()
        L.append(compent_.qr_code.strip())
    return L


#############################################################################

def my_main():
  #  get_all_data()
    c = get_compent_lst_by_plate("xj123")


    L = get_task()
    print("++++++++++++++++++++++++++++++")
    for i in L:
        t = i
        print(t[0], t[1])
    L = get_info_by_finger_id(66)
    for i in L:
        print(i)
    print(L[0][0])
    t, L =get_compent_by_car_id(6)
    print("type:", t)
    for l in L:
        print(l)

if __name__ == '__main__':
    my_main()
