import os
import time

mins = int(input("Set Timer in minutes:"))
t = mins*60
while t:
    mins = t//60
    secs = t%60
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(timer, end='\r')
    time.sleep(1)
    t-=1

print("Now it shuts down")

# #Shut Down
# os.system('shutdown -s')