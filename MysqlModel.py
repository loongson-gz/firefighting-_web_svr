from db.MysqlTool import  db

#人员
class Member(db.Model):
    __tablename__ ='t_member'
    id = db.Column(db.Integer,primary_key=True)
    finger_id = db.Column(db.Integer,unique=True)
    name = db.Column(db.String(255), default="")
    department = db.Column(db.String(255),default="")
    role_id = db.Column(db.Integer, unique=True)

#角色
class Role(db.Model):
    __tablename__ ='t_role'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)
    level = db.Column(db.Integer, unique=True)


#车辆
class Car(db.Model):
    __tablename__ ='t_car'
    id = db.Column(db.Integer,primary_key=True)
    plate_num = db.Column(db.String(255))
    car_type = db.Column(db.String(255), default="")
    #qr_code = db.Column(db.String(255),default="")
    member_id = db.Column(db.Integer)

#待检查的部件
class CarCompent(db.Model):
    __tablename__ ='t_car_compent'
    id = db.Column(db.Integer,primary_key=True)
    car_id = db.Column(db.Integer)    
    name = db.Column(db.String(255))
    qr_code = db.Column(db.String(255), unique=True)


#司机检查记录
class Record(db.Model):
    __tablename__ ='t_record'
    id = db.Column(db.Integer,primary_key=True)
    car_id = db.Column(db.Integer,unique=True)
    member_id = db.Column(db.Integer,unique=True)
    compent_id = db.Column(db.Integer,unique=True)
    # 0:未检测， 1:已检测   
    check_status = db.Column(db.Integer,default=0)
    # 0:异常， 1:正常       
    compent_status = db.Column(db.Integer, default=1)
    desc = db.Column(db.String(255),default="")
   # date_time = db.Column(db.DateTime)
    date = db.Column(db.Date)
    time = db.Column(db.Time)
    

#技师审核记录
class Record_Mechanic(db.Model):
    __tablename__ ='t_record_mechanic'
    id = db.Column(db.Integer,primary_key=True)
    record_id = db.Column(db.Integer)
    # 0:未审核， 1:已审核, 2:打回
    status = db.Column(db.SmallInteger)
    desc = db.Column(db.String(255), default="")
    #date_time = db.Column(db.DateTime)
    date = db.Column(db.Date)
    time = db.Column(db.Time)

#值班领导审核记录
class Record_Leader(db.Model):
    __tablename__ ='t_record_leader'
    id = db.Column(db.Integer,primary_key=True)
    record_mechanic_id = db.Column(db.Integer)
    # 0:未审核， 1:已审核
    status = db.Column(db.SmallInteger)
    desc = db.Column(db.String(255), default="")
    #date_time = db.Column(db.DateTime)
    date = db.Column(db.Date)
    time = db.Column(db.Time)

#待检车辆
class Task(db.Model):
    __tablename__ = 't_task'
    id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer)
    date = db.Column(db.Date)
    # 0:未检 1:已检 2:技师已审核 3:领导已审核
    status = db.Column(db.SmallInteger, default=0)
    # 0:正常 1:故障 2:待修     
    result = db.Column(db.SmallInteger, default=0)
    

#日常检测项
class Task_Normal(db.Model):
    __tablename__ ='t_task_normal'
    id = db.Column(db.Integer,primary_key=True)
    compent_id = db.Column(db.Integer)

#周检测项
class Task_Week(db.Model):
    __tablename__ ='t_task_week'
    id = db.Column(db.Integer,primary_key=True)
    compent_id = db.Column(db.Integer)    

#月检测项
class Task_Month(db.Model):
    __tablename__ ='t_task_month'
    id = db.Column(db.Integer,primary_key=True)
    compent_id = db.Column(db.Integer)

#指纹ID
class Param(db.Model):
    __tablename__ ='t_param'
    id = db.Column(db.Integer,primary_key=True)    
    finger_id = db.Column(db.Integer)
    

