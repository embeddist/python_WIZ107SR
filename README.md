Python Simple Script for WIZ107SR
================
<markdown>

## WIZ107SR  
WIZ107SR is a gateway module that converts serial protocol (RS-232) into TCP/IP protocol by using W7100A.  

Link WIZ107SR materials - [WIZ107SR](http://wiznet.co.kr/sub_modules/en/product/Product_Detail.asp?cate1=5&cate2=8&cate3=0&pid=1090)  


## SW - Download & Install  
 * python3.2 - [python3.2version](https://www.python.org/download/releases/3.2/)   
 * pyserial2.7 - [pyserial2.7](https://pypi.python.org/pypi/pyserial)   
 * ConfigTool for WIZ107SR - [ConfigTool](http://wiznet.co.kr/sub_modules/en/product/product_detail.asp?Refid=706&page=1&cate1=5&cate2=8&cate3=0&pid=1090&cType=2)

## Script descriptions - TCPClient
 
 * Init. serial port number and baudrate 
```c
	serial.Serial("COM1", 57600)  
```

 * Change to serial commond mode

  Change to serial command mode; when serial command switch code is '123'.
  Just only input serial command mode switch code of 3bytes without '\r\n'.
  Serial command mode switch code is set by using ConfigTool.
```c
	ser.write(b'123')           
```

 * Setting TCPClient mode  

 ```c
	ser.write(b'LP5000\r\n')                # Source port number : ex.) 5000
	ser.write(b'RP3000\r\n')                # TCP server port number : ex.) 3000
	ser.write(b'RH192.168.10.100\r\n')      # TCP server IP address : ex.) '192.168.10.100'
	ser.write(b'OP0\r\n')                   # Set TCP Client mode : OP0 - TCPClinet
	ser.write(b'SV\r\n')                    # Save Setting  
	ser.write(b'RT\r\n')                    # Reboot 
```

 * Send  

```c 
	ser.write(b'hello\r\n')
```  

 * recv  

```c 
	serial_recv_buf =  10
	line = ser.read(serial_recv_buf) 
  ... 
```

### FAQ; How know the status of TCP connections ?
  We can know the TCP connection by using 8pin.

	In the initial time, this pin is INPUT for Hardware Trigger(for 
	serial command mode). After that, this pin is OUTPUT for 
	connection status. When the connection is established, this pin 
	goes Low. And, it will go HIGH when connection is closed. 


</markdown>
