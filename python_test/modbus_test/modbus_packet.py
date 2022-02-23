#!/usr/bin/python
#coding=UTF-8

import modbus_common
import utils
import ctypes

modbus_packet = {'id':0, 'addr':0, 'code':16, 'buffer':[0]*(modbus_common.MACRO_MODBUS_MAX_BUFFER_SIZE), 'crc':0, 'length':0, 'exception':0, 'parsed':[0]}

def left_shift_buffer(buf, len):
    i = 0
    for i in range(0, len):
        buf.pop(0)
    return modbus_common.MACRO_MODBUS_OK

def _get_packet_length(packet):
    len = 0
    if packet['exception'] == 1:
        packet['length'] = 1
        return
    if packet['code'] == modbus_common.MACRO_MODBUS_MESSAGE_READ_HOLDING_REGISTERS:
        len = 4
    elif packet['code'] == modbus_common.MACRO_MODBUS_MESSAGE_WRITE_SINGLE_REGISTER:
        len = 4
    elif packet['code'] == modbus_common.MACRO_MODBUS_MESSAGE_WRITE_MULTIPLE_REGISTERS:
        len = 5
    else:
        len = 0
    packet['length'] = len


def read_remain_buffer(serial, packet):
    if packet['exception'] == 1:
        return modbus_common.MACRO_MODBUS_OK
    len = 0
    pos = 1
    rc = 0
    if packet['code'] == modbus_common.MACRO_MODBUS_MESSAGE_READ_HOLDING_REGISTERS:
        len = 0
    elif packet['code'] == modbus_common.MACRO_MODBUS_MESSAGE_WRITE_SINGLE_REGISTER:
        len = 0
    elif packet['code'] == modbus_common.MACRO_MODBUS_MESSAGE_WRITE_MULTIPLE_REGISTERS:
        pos = 5
        len = packet['buffer'][4]
    else:
        len = 0
    print("pos = ", pos)
    if len > 0:
        packet['length'] += len
        # rc = serial.read(packet['buffer'][pos:], len, modbus_common.MACRO_MODBUS_READ_TIMEOUT)
        if rc <= 0:
            return modbus_common.MACRO_MODBUS_READ_ERROR
    return modbus_common.MACRO_MODBUS_OK

def _check_header(packet):
    code = packet['code']&0x7F
    if (packet['id'] == packet['addr']) and ( code == modbus_common.MACRO_MODBUS_MESSAGE_READ_HOLDING_REGISTERS or code == modbus_common.MACRO_MODBUS_MESSAGE_WRITE_SINGLE_REGISTER or code == modbus_common.MACRO_MODBUS_MESSAGE_WRITE_MULTIPLE_REGISTERS ):
            _get_packet_length(packet)
            return modbus_common.MACRO_MODBUS_OK
    else :
        return modbus_common.MACRO_MODBUS_ERROR

def _header_deserialize(bytes, packet):
    pos = 0
    packet['addr'] = utils.data_read_u16_BE(bytes[pos:])
    pos += 1
    packet['code'] = utils.data_read_u8_BE(bytes[pos:])
    pos += 1
    if (packet['code'] & 0x80) == 0x80 :
        packet['exception'] = 1
    else :
        packet['exception'] = 0
    return pos

def _header_deserialize(bytes, packet):
    pos = 0
    packet['addr'] = utils.data_read_u8_BE(bytes[pos:])
    pos += 1
    packet['code'] = utils.data_read_u8_BE(bytes[pos:])
    pos += 1
    if (0x80 == (packet['code'] & 0x80)):
        packet[exception] = 1
    else :
        packet[exception] = 0
    return pos

buffer[0]*modbus_common.MACRO_MODBUS_HEADER_SIZE = [0]
new_header = 0

def _find_header(packet):
    global buffer
    global new_header
    rc = 0
    if (new_header == 0):
        ctypes.memset(buffer, 0, modbus_common.MACRO_MODBUS_HEADER_SIZE)

    # int len = port->length();
    if (len < 1 or (new_header == 0 and (len < modbus_common.MACRO_MODBUS_HEADER_SIZE))):
        return modbus_common.MACRO_MODBUS_READ_ERROR
    elif(modbus_common.MACRO_WIN_DEV_BUFFER_SIZE == len):
        return modbus_common.MACRO_MODBUS_READ_ERROR
    while True:
        # if (new_header == 0):
        #     rc = port->read(buffer, modbus_common.MACRO_MODBUS_HEADER_SIZE, modbus_common.MACRO_MODBUS_READ_TIMEOUT)
        # else :
        #     rc = port->read(&buffer[modbus_common.MACRO_MODBUS_HEADER_SIZE - 1], 1, modbus_common.MACRO_MODBUS_READ_TIMEOUT)
        # new_header = 1;
        # if rc <= 0:
        #     return modbus_common.MACRO_MODBUS_READ_ERROR
        _header_deserialize(buffer, packet);
        if (_check_header(packet) == modbus_common.MACRO_MODBUS_OK)
            new_header = 0;
            return modbus_common.MACRO_MODBUS_OK;
        left_shift_buffer(buffer, modbus_common.MACRO_MODBUS_HEADER_SIZE)