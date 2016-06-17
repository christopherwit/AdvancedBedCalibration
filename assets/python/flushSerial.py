import serial
import ConfigParser
serialconfig = ConfigParser.ConfigParser()
serialconfig.read('/var/www/lib/serial.ini') 
serial_port = serialconfig.get('serial', 'port')
serial_baud = serialconfig.get('serial', 'baud')

#initialize serial
serial = serial.Serial(port, baud, timeout=0.6)
serial.flushInput()
print "Done"
