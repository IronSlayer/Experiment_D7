#!/usr/bin/python
import signal, sys, time, threading, bladeRF_transceiver, datetime, serial
from gnuradio import gr
from time import sleep

def signal_handler(signal, frame):
    global rf
    print('You pressed Ctrl+C!')
    rf.stop()
    sys.exit(0)

def send_str(payload):
    rf.msg_source_msgq_in.insert_tail(gr.message_from_string(payload))

if __name__ == '__main__':

    signal.signal(signal.SIGINT, signal_handler)
    try:
        rf = bladeRF_transceiver.bladeRF_transceiver()
        ID = 'B101'
        FID = '1'
        SN = '1'
        D_CID = 'A101'
        S_CID = 'B101'
        M = '0'
        rf.set_frequency_tx(long(470e6))
        rf.set_frequency_rx(long(476e6))
        rf.set_tx_rf_gain(15)                   # [0,25]
        rf.set_tx_bb_gain(-10)                  # [-35,-4]
        rf.set_rx_rf_gain(3)                    # {0, 3, 6}
        rf.set_rx_bb_gain(40)                   # [5,60]

        rf.start()
        rf.set_tx_valve_value(True)
        while True:
                if rf.msg_sink_msgq_out.count():
                        data = rf.msg_sink_msgq_out.delete_head().to_string()
                        if data[24:28] == ID:
                                rf.set_tx_valve_value(False)
                                TS = str(datetime.datetime.now())
                                TS = TS[:19]
                                frame = gr.message_from_string(FID+','+SN+','+TS+','+D_CID+','+S_CID+','+M+','+data[36:52])
                                rf.msg_source_msgq_in.insert_tail(frame)
                                print data
                                print rf.probe_signal_1.level()
                                print rf.probe_signal_2.level()
                                print rf.avg_mag_sqrd.level()
                                sleep(0.1)
                                rf.set_tx_valve_value(True)
                        else:
                                print 'NO VALID ID'    
            
    except KeyboardInterrupt:
        print("W: interrupt received, proceeding")



