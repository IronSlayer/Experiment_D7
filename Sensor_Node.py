#!/usr/bin/python
import signal, sys, time, threading, bladeRF_transceiver, datetime, serial
from gnuradio import gr
from time import sleep

def signal_handler(signal, frame):
	global rf
	print('You pressed Ctrl+C!')
	arduinoPort.close()	
	rf.stop()
	sys.exit(0)

def send_str(payload):
	rf.msg_source_msgq_in.insert_tail(gr.message_from_string(payload))

if __name__ == '__main__':

	signal.signal(signal.SIGINT, signal_handler)
	try:
		rf = bladeRF_transceiver.bladeRF_transceiver()
		ID = 'C101'
		FID = '1'
		SN = '1'
		D_CID = 'A'
		S_CID = 'C'
		M = '1'
		rf.set_frequency_tx(long(470e6))
		rf.set_frequency_rx(long(476e6))
		rf.set_tx_rf_gain(15)                   # [0,25]
		rf.set_tx_bb_gain(-10)			# [-35,-4]
		rf.set_rx_rf_gain(3)			# {0, 3, 6}
		rf.set_rx_bb_gain(40)			# [5,60]

		arduinoPort = serial.Serial('/dev/ttyUSB0',9600,timeout=0.1)
		sleep(2)

		rf.start()
		rf.set_tx_valve_value(True)
		while True:
                        
			if rf.msg_sink_msgq_out.count():
				data = rf.msg_sink_msgq_out.delete_head().to_string()
				if data == ID:
                                        arduinoPort.write('a')
					SD = arduinoPort.readline()
					rf.set_frequency_tx(long(476e6))
                                        rf.set_frequency_rx(long(470e6))
                                        rf.set_tx_valve_value(False)
					TS = str(datetime.datetime.now())
					TS = TS[:19]
					frame = gr.message_from_string(FID+','+SN+','+TS+','+D_CID+','+S_CID+','+M+','+SD[4:19])
					rf.msg_source_msgq_in.insert_tail(frame)
					rf.msg_source_msgq_in.insert_tail(frame)
					rf.msg_source_msgq_in.insert_tail(frame)
					print data
					sleep(1)
					rf.set_tx_valve_value(True)
					rf.set_frequency_tx(long(470e6))
                                        rf.set_frequency_rx(long(476e6))
				else:
                                        print ''	
			
	except KeyboardInterrupt:
		print("W: interrupt received, proceeding")



