Python Simple Script for WIZ107SR
================
<markdown>

## WIZ107SR  
WIZ107SR is a gateway module that converts serial protocol (RS-232) into TCP/IP protocol by using W7100A.  

Link WIZ107SR matrials - [WIZ107SR](http://wiznet.co.kr/sub_modules/en/product/Product_Detail.asp?cate1=5&cate2=8&cate3=0&pid=1090)  


## SW - Download & Install  
 * python3.2 - [python3.2version](https://www.python.org/download/releases/3.2/)   
 * pyserial2.7 - [pyserial2.7](https://pypi.python.org/pypi/pyserial)   
 
 * gr_WebLED.cpp - Web Server & LED Blink  


## Script descriptions 
 
 * Configuration of IP address  
```c
IPAddress ip(192,168,1,177);
```

 * Initalize the Port (port80 is default for HTTP)  
```c
EthernetServer server(80);
```

 * Parsing of HTTP GET Message  

  When web-page address is http://192.168.1.177/G0 to on the Green LEN,
  the received HTTP GET Message is as below,  
```c
  GET /G0 HTTP/1.1  
  Accept: text/html, application/xhtml+xml,....
```

  So, 5th~7th data are parsed to control RGB LEDs.  
```c 
  //5th~7th data of HTTP GET Message is parsed as parse_arr  
  parse_arr[0] = '/'  
  parse_arr[1] = 'G'  
  parse_arr[2] = '0'  
```
 * Contorl RGB LEDs as data pased from HTTP GET Message  
```c 
 if(parse_arr[0] == '/'){  
   switch(parse_arr[1]){  
   case('R') :  
   // http://192.168.1.177:R0 => Red LED OFF			  	  
   if(parse_arr[2] == '0'){    
	   digitalWrite(led_red, HIGH);  
   // http://192.168.1.177:R1 => Red LED ON    			  
   }else if(parse_arr[2] == '1'){  
           digitalWrite(led_red, LOW);  
   }  
           break;  
  ... 
```  

 * Send a standard http response  
  Check current LED status as digitalRead() and Send http respoonse inclued the LED status.  
```c 
          int sensorReading = digitalRead(led_red);
          client.print("digitalRead(LED_RED)");//client.print(led_red);
          client.print(" is ");
          client.print(sensorReading);
          client.println("<br />");
  ... 
```

</markdown>
