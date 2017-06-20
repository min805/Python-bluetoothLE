'''
Created on Jun 14, 2017
@author: min
'''
from gattlib import BeaconService
import time

class MyAdvertising(object):
    '''Beacon advertising class'''

    def __init__(self, sec=5):
        self.my_uuid  = "11111111-2222-3333-4444-555555555555"
        self.my_major = 1
        self.my_minor = 1
        self.my_txpower = 1
        self.my_interval = 200
        
        self.service = BeaconService("hci0")
        self.advertise(sec)
        
    def advertise(self,sec=5):
        print("start Advertising.")
        self.service.start_advertising(self.my_uuid,
                                       self.my_major,
                                       self.my_minor,
                                       self.my_txpower,
                                       self.my_interval)
        #service.start_advertising("11111111-2222-3333-4444-555555555555",1,1,1,200)

        time.sleep(sec)
        self.service.stop_advertising()

        print("Done Advertising.")


if __name__ == '__main__':
    MyAdvertising()
    print("Done.")

