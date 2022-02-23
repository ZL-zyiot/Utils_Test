#!/usr/bin/python
#coding=UTF-8
import struct

def data_u16_to_BE(data_in):
    data_out = struct.pack('H', data_in)
    return data_out

def data_u32_to_BE(data_in):
    data_out = struct.pack('L', data_in)
    return data_out

def data_read_u8(data_in):
    data_out = data_in[0]
    return data_out

def data_read_u8_BE(data_in):
    data_out = data_in[0]
    return data_out

def data_read_u16(data_in):
    data_out = data_in[1]<<8 | data_in[0]
    return data_out

def data_read_u16_BE(data_in):
    data_out = data_in[0]<<8 | data_in[1]
    return data_out

def data_read_u32(data_in):
    data_out = data_in[3]<<24 | data_in[2]<<16 | data_in[1]<<8 | data_in[0]
    return data_out

def data_read_u32_BE(data_in):
    data_out = data_in[0]<<24 | data_in[1]<<16 | data_in[2]<<8 | data_in[3]
    return data_out

def data_write_u16(data_in):
    data_out = [0,0]
    data_out[0] = data_in & 0xFF
    data_out[1] = (data_in>>8) & 0xFF
    return data_out

def data_write_u16_BE(data_in):
    data_out = [0,0]
    data_out[1] = data_in & 0xFF
    data_out[0] = (data_in>>8) & 0xFF
    return data_out

def data_write_u32(data_in):
    data_out = [0,0,0,0]
    data_out[0] = (data_in>>24) & 0xFF
    data_out[1] = (data_in>>16) & 0xFF
    data_out[2] = (data_in>>8) & 0xFF
    data_out[3] = data_in & 0xFF
    return data_out

def data_write_u32_BE(data_in):
    data_out = [0,0,0,0]
    data_out[3] = (data_in>>24) & 0xFF
    data_out[2] = (data_in>>16) & 0xFF
    data_out[1] = (data_in>>8) & 0xFF
    data_out[0] = data_in & 0xFF
    return data_out

def utils_uint16_t_memclr(src, size):
    i = 0
    for i in range(0, size):
        src[i] = 0
    
    return size


def utils_uint16_t_memcpy(des, src, size):
    i = 0
    for i in range(0, size):
        des[i] = src[i]
    
    return i


def utils_uint16_t_BE_memcpy(des, src, size):
    i = 0
    temp = 0
    for i in range(0, size):
        temp = src[i]
        des[i] = ((temp>>8)&0xFF) | ((temp&0xFF)<<8)
    
    return i

def utils_uint16_t_memcmp(des, src, size):
    i = 0
    for i in range(0, size):
        if des[i] != src[i]:
            return 1
    return 0


def utils_uint16_t_BE_memcmp(des, src, size):
    i = 0
    temp = 0
    for i in range(0, size):
        temp = src[i]
        temp_swap = ((temp>>8)&0xFF) | ((temp&0xFF)<<8)
        if des[i] != temp_swap:
            return 1
    return 0
