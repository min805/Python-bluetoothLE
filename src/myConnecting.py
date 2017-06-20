'''
Created on Jun 15, 2017
@author: root
'''

from __future__ import print_function
import sys
from gattlib import GATTRequester
#from myScanning import MyScanning

class MyConnecting(object):
    '''Connecting class'''

    def __init__(self, address):
        self.requester = GATTRequester(address,False)
        
        i = self.requester.is_connected()
        print(i)
        self.connect()
        
    def connect(self):
        print("connecting...",end='')
        sys.stdout.flush()        
        self.requester.connect(True)
        print("Okay")
        

if __name__ =="__main__":
    if(len(sys.argv) < 2):
        print("Usage:{} <addr>".format(sys.argv[0]))
        sys.exit(1)
        
    MyConnecting(sys.argv[1])
    print("Done.")
