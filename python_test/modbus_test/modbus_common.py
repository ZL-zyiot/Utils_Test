#!/usr/bin/python
#coding=UTF-8

MACRO_MODBUS_OK = 0
MACRO_MODBUS_ERROR = -1
MACRO_MODBUS_READ_ERROR = -2
MACRO_MODBUS_PARAM_ERROR = -3
MACRO_MODBUS_CRC_ERROR = -4
MACRO_MODBUS_NOT_SUPPORT = -255
MACRO_MODBUS_READ_TIMEOUT = 1000
MACRO_MODBUS_WRITE_TIMEOUT = 0x2fff


MACRO_MODBUS_ILLEGAL_FUNCTION = 0X01
MACRO_MODBUS_ILLEGAL_DATA_ADDRESS = 0x02
MACRO_MODBUS_ILLEGAL_DATA_VALUE = 0x03
MACRO_MODBUS_SERVICE_DEVICE_FAILURE = 0x04
MACRO_MODBUS_ACKNOWLEDGE = 0x05
MACRO_MODBUS_SERVICE_DEVICE_BUSY = 0x06
MACRO_MODBUS_MEMORY_PARITY_ERROR = 0x08
MACRO_MODBUS_GATEWAY_PATH_UNAVAILABLE = 0x0A
MACRO_MODBUS_GATEWAY_TARGET_DEVIE_FAILED_TO_RESPOND = 0x0B


MACRO_MODBUS_MESSAGE_READ_COILS = 0x1
MACRO_MODBUS_MESSAGE_READ_DISCRETE_INPUTS = 0x2
MACRO_MODBUS_MESSAGE_READ_HOLDING_REGISTERS = 0x3
MACRO_MODBUS_MESSAGE_READ_INPUT_REGISTERS = 0x4
MACRO_MODBUS_MESSAGE_WRITE_SINGLE_COIL = 0x5
MACRO_MODBUS_MESSAGE_WRITE_SINGLE_REGISTER = 0x6
MACRO_MODBUS_MESSAGE_READ_EXCEPTION_STATUS = 0x7
MACRO_MODBUS_MESSAGE_DIAGNOSTICS = 0x8
MACRO_MODBUS_MESSAGE_GET_COMMON_EVENT_COUNTER = 0xB
MACRO_MODBUS_MESSAGE_GET_COMMON_EVENT_LOG = 0xC
MACRO_MODBUS_MESSAGE_WRITE_MULTIPLE_COILS = 0xF
MACRO_MODBUS_MESSAGE_WRITE_MULTIPLE_REGISTERS = 0x10
MACRO_MODBUS_MESSAGE_REPORT_SERVER_ID = 0x11
MACRO_MODBUS_MESSAGE_IAP = 0x77
MACRO_MODBUS_MESSAGE_IAP_CHECK = 0x78

MACRO_MODBUS_MAX_BUFFER_SIZE = 260
MACRO_MODBUS_HEADER_SIZE = 2
MACRO_WIN_DEV_BUFFER_SIZE = 1024

MACRO_MODBUS_MASTER_DEV = 1
MACRO_MODBUS_SLAVE_DEV = 0