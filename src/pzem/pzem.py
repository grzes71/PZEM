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

log = logging.getLogger(__name__)

class PZEM:
    def __init__(self, args):
        self.__cfg = args
        self.__ser = serial.Serial(args.port, baudrate=args.baudrate, bytesize=BYTESIZE, parity=PARITY, 
                                   stopbits=STOPBITS, timeout=TIMEOUT, xonxoff=XONXOFF, rtscts=RTSCTS)

    @property
    def cfg(self):
        return self.__cfg

    @property
    def ser(self):
        return self.__ser

    def log_to_csv(self):
        spamwriter = csv.writer(self.cfg.outfile, quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
        spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
