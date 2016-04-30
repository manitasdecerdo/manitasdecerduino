
import serial

DEVICE="/dev/ttyACM4"

s = serial.Serial(DEVICE, 9600, timeout=2)

while 1:
    print s.readline().strip()


# import time
# import sys
# import argparse
# from bluepy import btle, blescan



# def main():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('-i', '--hci', action='store', type=int, default=0,
#                         help='Interface number for scan')
#     parser.add_argument('-t', '--timeout', action='store', type=int, default=4,
#                                                             help='Scan delay, 0 for continuous')
#     parser.add_argument('-s', '--sensitivity', action='store', type=int, default=-128,
#                         help='dBm value for filtering far devices')
#     parser.add_argument('-d', '--discover', action='store_true',
#                         help='Connect and discover service to scanned devices')
#     parser.add_argument('-a','--all', action='store_true',
#                         help='Display duplicate adv responses, by default show new + updated')
#     parser.add_argument('-n','--new', action='store_true',
#                         help='Display only new adv responses, by default show new + updated')
#     parser.add_argument('-v','--verbose', action='store_true',
#                         help='Increase output verbosity')
#     arg = parser.parse_args(sys.argv[1:])
    
#     btle.Debugging = arg.verbose
    
#     scanner = btle.Scanner(arg.hci).withDelegate(blescan.ScanPrint(arg))

#     print ("Scanning for devices...")
#     devices = scanner.scan(arg.timeout)

#     if arg.discover:
#         print (ANSI_RED + "Discovering services..." + ANSI_OFF)
    
#         for d in devices:
#             print d
                                                     
#if __name__ == "__main__":
#    main()
        
