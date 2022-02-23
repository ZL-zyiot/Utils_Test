#!/usr/bin/python
#coding=UTF-8
import serial #导入模块
import serial.tools.list_ports

def get_serial_portlist():
    port_list = list(serial.tools.list_ports.comports())
    print(port_list)
    if len(port_list) == 0:
        print('无可用串口')
    else:
        for i in range(0,len(port_list)):
            print(port_list[i])

try:
    #端口，GNU / Linux上的/ dev / ttyUSB0 等 或 Windows上的 COM3 等
    portx="COM7"
    #波特率，标准值之一：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
    bps=115200
    #超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
    timex=5
    get_serial_portlist()
    # 打开串口，并得到串口对象
    ser=serial.Serial(portx,bps,timeout=timex)
    if ser.isOpen():
        print("open serial sucess")
    else:
        print("open serial failed")

    # 写数据
    senddata = {0x0, 0x1, 0x2, 0x3, 0x4, 0x5}
    result=ser.write(senddata)
    print("写总字节数:",result)

    # 读数据
    while True:
        if ser.in_waiting:
            str = ser.read(ser.in_waiting).hex()
            print("receive:",str)

    print("---------")
    ser.close()#关闭串口

except KeyboardInterrupt:
    if ser != None:
        ser.close()

except Exception as e:
    print("---异常---：",e)
