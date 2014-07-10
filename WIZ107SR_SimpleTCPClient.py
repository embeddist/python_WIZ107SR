import serial
import string
import sys
import time
import io

ser = serial.Serial("COM1", 57600)          # Init. serial port number and baudrate
print (ser.isOpen())

msg = ser.read(152)                         # print welcome message from WIZ107SR (size is 152bytes)
print(msg)
time.sleep(3)                                  

print ("Change to serial commond mode")
ser.write(b'123')           # Change to serial command mode; when serial command switch code is '123'
                            # just only input serial command mode switch code of 3bytes with '\r\n' 
                            # Serial command mode switch code is set by using ConfigTool. 
time.sleep(1)    


print ("Check Version")
ser.write(b'VR\r\n')        # check Firmware version
time.sleep(1)    
#ret = ser.read(8)          # print respones
#print(ret)

        
print ("Setting TCPClient mode")
ser.write(b'LP5000\r\n')                # Source port number : ex.) 5000
ser.write(b'RP3000\r\n')                # TCP server port number : ex.) 3000
ser.write(b'RH192.168.10.100\r\n')      # TCP server IP address : ex.) '192.168.10.100'
ser.write(b'OP0\r\n')                   # Set TCP Client mode : OP0 - TCPClinet
ser.write(b'SV\r\n')                    # Save Setting  
ser.write(b'RT\r\n')                    # Reboot 
time.sleep(1)                           # delay for Init. of WIZ107SR    

print ("send data to TCPServer")
ser.write(b'hello\r\n')

print ("recv data from TCPServer")
serial_recv_buf =  10
line = ser.read(serial_recv_buf)         
print(line)

ser.close()
