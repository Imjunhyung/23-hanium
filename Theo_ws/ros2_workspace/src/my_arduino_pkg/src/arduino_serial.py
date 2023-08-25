from time import sleep
import serial

class VirtualSerialClient():
	def __init__(self):
		self.recieving_device = '/dev/ttyACM0' #device we are recieving messages from
		self.serial_send = serial.Serial(self.transmitting_device, 9600, #Note: Baud Rate must be the same in the arduino program, otherwise signal is not recieved!
            timeout=.1)
		self.serial_recieve = serial.Serial(self.recieving_device,
						9600, #Note: Baud Rate must be the same in the arduino program, otherwise signal is not recieved!
						timeout=.1)
	# def send_cmd(self, cmd):
	# 	print("Sending: " + cmd)
	# 	self.serial_send.write(bytes(cmd,'utf-8'))
 
	def recieve_cmd(self):
		#try normal way of recieving data
		sleep(.01) #sleep to allow time for serial_data to arrive. Otherwise this might return nothing
		self.line = self.serial_recieve.readline().decode('utf-8').rstrip()
		
		print(self.line)


def main(args=None):
	virtual_serial_client = VirtualSerialClient()
	while True:
		virtual_serial_client.recieve_cmd()

while True:
	main()
