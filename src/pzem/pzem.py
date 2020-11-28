"""
Peacefair PZEM energy meter data logger.
Requires Python serial library.
"""
import sys
import argparse
import logging
import serial 
import csv 

BYTESIZE = 8
PARITY = 'N'
STOPBITS = 1
TIMEOUT = 5 # 5 seconds serial timeout
XONXOFF = 0
RTSCTS = 0

CMD_RESET = [0xf8,0x42,0xc2,0x41]
CMD_QUERY = [0xf8,0x04,0x00,0x00,0x00,0x0a,0x64,0x64]

log = logging.getLogger(__name__)

class PZEM:
    def __init__(self, args):
        self.__cfg = args
        self.__ser = None
        # self.__ser = serial.Serial(args.port, baudrate=args.baudrate, bytesize=BYTESIZE, parity=PARITY, 
        #                            stopbits=STOPBITS, timeout=TIMEOUT, xonxoff=XONXOFF, rtscts=RTSCTS)

    @property
    def cfg(self):
        return self.__cfg

    @property
    def ser(self):
        return self.__ser

    def log(self):
        '''
        Query device and log data to csv file
        '''
        queries_time = self.cfg.queries_time
        queries_number = self.cfg.queries_number
        writer = csv.writer(self.cfg.outfile, quoting=csv.QUOTE_MINIMAL)
        while True:
            pass
        self.cfg.outfile.close()

    def reset(self):
        '''
        Send reset energy to device
        '''

    def gui(self):
        '''
        Start GUI
        '''
