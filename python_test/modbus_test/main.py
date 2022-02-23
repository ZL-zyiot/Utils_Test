#!/usr/bin/python
#coding=UTF-8

import modbus_packet

test_data = [1, 2, 3, 4, 5]
print("test_data = ", test_data)
modbus_packet.left_shift_buffer(test_data, 1)
print("test_data = ", test_data)
# modbus_packet._get_packet_length(modbus_packet.modbus_packet)
# len = modbus_packet.modbus_packet['length']
# print("len = ", len)

# modbus_packet.read_remain_buffer(0, modbus_packet.modbus_packet)
# len = modbus_packet.modbus_packet['buffer'][4]
# print("len = ", len)

# modbus_packet._check_header(modbus_packet.modbus_packet)
# len = modbus_packet.modbus_packet['length']
# print("len = ", len)