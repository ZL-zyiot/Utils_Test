#!/usr/bin/python
#coding=UTF-8
import serial #导入模块
import serial.tools.list_ports
from serial.tools.list_ports_windows import NULL
import threading
import time
from crc import get_modbus_crc16
from utils import data_u16_to_BE
from utils import data_u32_to_BE
from utils import data_read_u16
from utils import data_read_u16_BE
from utils import data_read_u32
from utils import data_read_u32_BE
from utils import data_write_u16
from utils import data_write_u16_BE
from utils import data_write_u32
from utils import data_write_u32_BE
from utils import utils_uint16_t_memclr
from utils import utils_uint16_t_memcpy
from utils import utils_uint16_t_BE_memcpy
from utils import utils_uint16_t_memcmp
from utils import utils_uint16_t_BE_memcmp


serial_write_data = [0x1, 0x2, 0x3, 0x4, 0x5, 0x6]
serial_read_data = [0]
serial_enable = True
usr_serial = NULL

def read_data_serial_thread(serial):
    global serial_read_data
    print(serial.portstr)
    print(serial.baudrate)
    while serial_enable:
        if serial.in_waiting:
            serial_read_data = serial.read(serial.in_waiting).hex()

class creat_thread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        global serial_read_data
        global usr_serial
        print("run serial thread")
        print(usr_serial.portstr)
        print(usr_serial.baudrate)
        while serial_enable:
            if usr_serial.in_waiting:
                try:
                    serial_read_data = usr_serial.read(usr_serial.in_waiting).hex()
                    print(serial_read_data)
                except:
                    print("read error")


def get_serial_portlist():
    port_list = list(serial.tools.list_ports.comports())
    print(port_list)
    if len(port_list) == 0:
        print('无可用串口')
    else:
        for i in range(0,len(port_list)):
            print(port_list[i])

def open_serial(portx, buad):
    result = False
    try:
        open_serial = serial.Serial(portx, buad)
        if open_serial.isOpen():
            print("open serial sucess")
            result = True
            # thread.start_new_thread(target=read_data_serial_thread, args=(open_serial,))
            serial_thread = creat_thread(1, "serial", 1)
            serial_thread.start()
        else:
            print("open serial failed")
            result = False
    except Exception as e:
        if open_serial.isOpen():
            open_serial.close()
        print("error accure while open serial")
    return open_serial, result

def close_serial(serial):
    global serial_enable
    serial_enable = False
    serial.close()
    print("close serial")

def write_serial(serial, string):
    result = serial.write(string.encode("utf-8"))
    return result

def write_hex_serial(serial, data):
    result = serial.write(data)
    return result

def read_serial(serial):
    global serial_read_data
    data = serial_read_data
    serial_read_data = {0}
    return data

def crc_fun_test():
    crc_data = [0x1, 0x2, 0x3, 0x4, 0x5, 0x6]
    crc16 = get_modbus_crc16(crc_data, len(crc_data))
    print("crc16 = 0x", data_u16_to_BE(crc16).hex())

def utils_fun_test():
    test = [0x12, 0x34, 0x56, 0x78]
    print("u16 be = ", data_read_u16_BE(test))
    print("u32 be = ", data_read_u32_BE(test))
    testdata = 0x12345678
    print("u16 be = ", data_write_u16_BE(testdata))
    print("u32 be = ", data_write_u32_BE(testdata))
    utils_uint16_t_memclr(test, len(test))
    print("test = ", test)
    test1 = [0xaa00, 0xbb11, 0xcc22]
    utils_uint16_t_BE_memcpy(test, test1, len(test1))
    print("test = ", test)
    print("test1 = ", test1)
    print("test and test1 compare result = ", utils_uint16_t_BE_memcmp(test, test1, len(test1)))


get_serial_portlist()
serial_port = "COM7"
serial_buad = 115200
ret = False
usr_serial, ret = open_serial(serial_port, serial_buad)
time.sleep(2)
if ret == True:
    serial_write_string = "this is serial test\r\n"
    count = write_serial(usr_serial, serial_write_string)
    print("write count :", count)
    count = write_hex_serial(usr_serial, serial_write_data)
    print("write count :", count)
    read_serial(usr_serial)
    
    # close_serial(usr_serial)

