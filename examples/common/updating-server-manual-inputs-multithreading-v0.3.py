#!/usr/bin/env python
'''
Pymodbus Server With Updating Thread
--------------------------------------------------------------------------

This is an example of having a background thread updating the
context while the server is operating. This can also be done with
a python thread::

    from threading import Thread

    thread = Thread(target=updating_writer, args=(context,))
    thread.start()
'''
#---------------------------------------------------------------------------# 
# import the modbus libraries we need
#---------------------------------------------------------------------------# 
import thread
import time
from pymodbus.server.async import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.transaction import ModbusRtuFramer, ModbusAsciiFramer

#---------------------------------------------------------------------------# 
# import the twisted libraries we need
#---------------------------------------------------------------------------# 
from twisted.internet.task import LoopingCall


#---------------------------------------------------------------------------# 
# initialize your data store
#---------------------------------------------------------------------------# 
store = ModbusSlaveContext(
    co = ModbusSequentialDataBlock(0x01, [1]*100),
    di = ModbusSequentialDataBlock(0x01, [0]*100), 
    hr = ModbusSequentialDataBlock(0x01, [1]*100),
    ir = ModbusSequentialDataBlock(0x01, [4]*100))
context = ModbusServerContext(slaves=store, single=True)


#---------------------------------------------------------------------------# 
# initialize the server information
#---------------------------------------------------------------------------# 
identity = ModbusDeviceIdentification()
identity.VendorName  = 'pymodbus'
identity.ProductCode = 'PM'
identity.VendorUrl   = 'http://github.com/bashwork/pymodbus/'
identity.ProductName = 'pymodbus Server'
identity.ModelName   = 'pymodbus Server'
identity.MajorMinorRevision = '1.0'

#---------------------------------------------------------------------------# 
# Set up the X and Y
#---------------------------------------------------------------------------#
def updating_positions(a):
    register = 3
    slave_id = 0x01
    address1  = 0x01
    address2  = 0x02
    address3  = 0x03
    value3   = [0]
    NewData= "Yes"

    while NewData== "Yes":
    
        value1 = input("What is the value of X?")
        print "Set X as " + str(value1)
        context[slave_id].setValues(register, address1, value1)
    
        value2   = input("What is the value of Y?")
        print "Set Y as" + str(value2)
        context[slave_id].setValues(register, address2, value2)
        
        value3   = [v for v in value3]
        context[slave_id].setValues(register, address3, value3)
        print "Now UR5 is Moving "+ str(value3)

        #NewData= raw_input("Do you want to put new data ('Yes' or 'No')?")
        
            
    
#---------------------------------------------------------------------------# 
# run the server you want
#---------------------------------------------------------------------------#
thread.start_new_thread(updating_positions,(context,))
StartTcpServer(context, identity=identity, address=("169.254.45.85", 502))


