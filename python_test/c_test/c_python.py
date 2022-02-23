#!/usr/bin/python
#coding=UTF-8

from ctypes import *
from ctypes import cdll

#load the shared object file
mylib = CDLL('hello.so')

ret = mylib.hello("python")
print(mylib._name)

