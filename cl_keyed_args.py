import argparse
import sys

# py .\cl_keyed_args.py 1 2 -s asfsASFAFsffas -v 0 -n 5 -l -b 4 -pp 

parser = argparse.ArgumentParser(description="Print song a certain number of times with optional formatting",formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument("-v","--verbose", help="increase output verbosity",type=int,default=1,choices=[0, 1, 2])
parser.add_argument("-s","--song",help="lyrics to sing",type=str,required=True)
parser.add_argument("-n","--num",help="repeat song n times",type=int,default=1)
parser.add_argument("pos1",help="positional #1",type=int,default=0)
parser.add_argument("pos2",help="positional #2",type=int,default=0)
parser.add_argument("-b","--base",help="square this number by p",type=int)
parser.add_argument("-p","--power",help="times to multiply base",action="count")

size = parser.add_mutually_exclusive_group()
size.add_argument("-l","--lower",help="smol text",action="store_true")
size.add_argument("-u","--upper",help="TEXT MAKE BIG",action="store_true")

# args = parser.parse_args(args=None if sys.argv[1:] else ['--help']) # help if no arguments
args = parser.parse_args()
print(args)

print("This is a song:" if args.verbose == 1
else "A song is a musical composition intended to be vocally performed by the human voice." if args.verbose == 2 else "Song:")

if (args.song):
    for i in range(args.num):
        print(args.song.upper() if args.upper else args.song.lower() if args.lower else args.song)

if (args.pos1 is not None and args.pos2 is not None):
    print("pointless math: ",args.pos1 * args.pos2 + args.pos1)

if (args.base and args.power):
    print("pointless math #2: ",args.base ** args.power)
