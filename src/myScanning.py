'''
Created on Jun 14, 2017
@author: root
'''

from gattlib import BeaconService



class MyScanning(object):
    '''Beacon Scanning class'''

    def __init__(self, scan_addr=0,sec=3):
        
        self.found=False
        print("Start scanning.")
        self.service = BeaconService("hci0")
        self.devices = self.service.scan(sec)
        self.print_device(scan_addr)
        print("Done scanning.")
        
    def __str__(self):
        ret = "No"
        if(self.found==True):
            ret = "Yes"
            
        return ret
        
    
    def print_device(self,scan_addr):   
        
        print("Result")        
#       for address,name in list(self.devices.items()):
#           print ("name:{}, address:{}".format(name,address))
        
        for addr,data in list(self.devices.items()):
            my_addr = addr
            my_uuid = data[0]
            my_major = data[1]
            my_minor = data[2]
            my_power = data[3]
            my_rssi = data[4]
            
            print ("Beacon: Addr={ADDR} uuid={UUID} ver={MAJOR}.{MINOR} txpower={PWR} rssi={RSSI}"\
             .format(ADDR=my_addr,UUID=my_uuid,MAJOR=my_major,MINOR=my_minor,PWR=my_power,RSSI=my_rssi) )
        
            if(scan_addr!=0 and scan_addr==my_addr):
                self.found=True
            
if __name__ == '__main__':
    address="B8:27:EB:97:2B:42"
    #s=MyScanning()
    s=MyScanning(scan_addr=address)
    print(s)
    print("Done.")
        
           
         
         
         
         
         