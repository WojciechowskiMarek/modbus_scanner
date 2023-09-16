from pymodbus.client.serial import ModbusSerialClient as ModbusClient
import logging
#logging.basicConfig();
#log = logging.getLogger();
#log.setLevel(logging.DEBUG);
while True:
    client = ModbusClient(port="COM3",stopbits = 1, bytesize = 8, parity = 'N', baudrate= 9600)
    for number in range(33):        
        PV = client.read_holding_registers(0x01,1,number) # example with 0x01 - holding register from slave, to change depends on needs :)
        if PV.isError():
            print("Not found slave with number", number)
        if not PV.isError():
            print("Found device with number",number)
