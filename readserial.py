import serial
import sys
import os
import time
import dbhepler
import threading

def usage():
    print("usage:")
    print("     ", sys.argv[0] , "dev", "baud", "read")
    print("     ", sys.argv[0] , "dev", "baud", "write", "value")
    os._exit(0)

class Ser:
    def __init__(self, dev, baud, tm):
#        self.ser = serial.Serial(dev , baud)
        self.ser = serial.Serial(dev , baud, timeout=0.1)

    def read(self, length):
        return self.ser.read(length)

    def write(self, val):
        return self.ser.write(val)


#def get_data(dev, baud):
def get_data():
    print("======read_serail ......")
    test = Ser("COM2", int(115200), 1) 
    while True:
        cmd = [0xFF, 0x21, 0x80, 0x00, 0x00, 0xA1, 0xFE]
        test.write(cmd) 
        ret = test.read(1024).hex()
        if len(ret) >=34 and ret[0]=='f' and ret[1]=='f' and ret[-1]=='e' and ret[-2]=='f':
            id = int(ret[-12:-4], 16)
            print("++++++++++++++++++++Id:", id)
            if id != int(0):
                dbhepler.update_finger_id(id)

        #s = int(ret[-12:-4], 16)
        #print(len(ret), "----->", ret, "====", s)
        #print("================",ret[0], ret[1], ret[-1], ret[-2])
        time.sleep(0.5)
        
        
def get_finger_id():
    return dbhepler.get_finger_id()
        
def start_get_finger():
    print("===================start read finger.....")
    t = threading.Thread(target=get_data, name='LoopThread')
    t.start()

if __name__ ==  '__main__':

    try:
        dev = sys.argv[1] 
        baud = sys.argv[2]
        get_data(dev, baud)
    except Exception as e:
        print("Unexpected Error: {}".format(e))
        usage()

    
    try:
        test = Ser(dev, int(baud), 1)
    except Exception as e:
        print("Unexpected Error: {}".format(e))
        
    try:
        if(sys.argv[3] == 'read'):
            print("read:")
            while 1:
                s = test.read(1024).decode("UTF-8")
                if(s != ''):
                    print("%s" % s)
        elif sys.argv[3] == 'write' and sys.argv[4].strip():
            print("write:")
            test.write(sys.argv[4].encode("UTF-8"))
        else:
            usage()
    except Exception as e:
        print("Unexpected Error: {}".format(e))
