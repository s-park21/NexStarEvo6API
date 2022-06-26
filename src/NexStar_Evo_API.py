# import Serial
import time

class NexStar_Evo:
    def __init__(self, comPort):
        print("INitpi")
    # Function to set location 
    # Latitude and longitude is in form [degrees, minutes, seconds]
    def setLocation(self, lat, lng):
        print("hello")
    
    
    def setTime(self, ):
        ## Set time
        print("Hello")

    # Converts degrees.degrees to deg, min, sec
    def decdeg2dms(dd):
        mult = -1 if dd < 0 else 1
        mnt,sec = divmod(abs(dd)*3600, 60)
        deg,mnt = divmod(mnt, 60)
        return mult*deg, mult*mnt, mult*sec

