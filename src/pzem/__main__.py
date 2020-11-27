#!/usr/bin/env python3
"""
Peacefair PZEM energy meter data logger.
Requires Python serial library.

Example (in your terminal):

    $ python3 -m pzem COM3 --baudrate 9600

"""

import sys
import argparse
import logging
import logging.config
import logging.handlers

from pzem.pzem import PZEM

LOGGING_CONFIG = { 
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': { 
        'standard': { 
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': { 
        'default': { 
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',  # Default is stderr
        },
    },
    'loggers': { 
        '': {
            'handlers': ['default'],
            'level': 'WARNING',
            'propagate': False
        },
        'pzem': { 
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': False
        },
        '__main__': {  
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': False
        },
    } 
}

def func_gui(args):
    PZEM(args).gui()

def func_log(args):
    PZEM(args).log()

def func_reset(args):
    PZEM(args).reset()

def cmdline_args():
    def add_serial_config(p):
        p.add_argument('-b', "--baudrate", default=9600, type=int,
                       help="baudrate (default 9600)")
        p.add_argument("port", help="port name (e.g. COM3)")

    parser = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    subparsers = parser.add_subparsers(help='commands')

    gui_parser = subparsers.add_parser("gui")
    add_serial_config(gui_parser)
    gui_parser.set_defaults(func=func_gui)

    reset_parser = subparsers.add_parser("reset")
    add_serial_config(reset_parser)
    reset_parser.set_defaults(func=func_reset)

    log_parser = subparsers.add_parser("log")
    add_serial_config(log_parser)
    log_parser.add_argument('outfile',  type=argparse.FileType('w'), 
                            help="output file")
    log_parser.add_argument('-s', "--sleep", type=float, default=1000.0,
                            help="sleep between queries [ms]")
    log_parser_queries_group = log_parser.add_mutually_exclusive_group(required=True)
    log_parser_queries_group.add_argument('-t', "--queries-time", type=int, help="logging time [seconds]")
    log_parser_queries_group.add_argument('-n', "--queries-number", type=int, help="number of queries")
    log_parser.set_defaults(func=func_log)
    
    parser.add_argument("-l", "--loglevel", choices=('ERROR', 'WARNING', 'INFO', 'DEBUG'), default='INFO',
                        help="change logging level")
    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    if sys.version_info<(3,5,0):
        sys.stderr.write("You need python 3.5 or later to run this script\n")
        sys.exit(1)
    logging.config.dictConfig(LOGGING_CONFIG)
    cmdline_args()
    

