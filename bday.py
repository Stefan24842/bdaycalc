import datetime as dt
import numpy as np

bdate=dt.date(1996,2,22)

tdate=dt.date.today()
#tdate=dt.date(2018,6,1)

days=365.2425 #NASA
#next pi bday
for i in range(100):
    pidate=bdate+dt.timedelta(days=days*i*np.pi) #todo correct
    if((pidate-tdate).days>=0):
        print("Your next Pi-Day is on",pidate," (",i,"pi)")
        break
for i in range(100):
    edate=bdate+dt.timedelta(days=days*i*np.e) #todo correct
    if((edate-tdate).days>=0):
        print("Your next e-Day is on",edate," (",i,"e)")
        break
for i in range(100):
    gdate=bdate+dt.timedelta(days=days*i*np.euler_gamma) #todo correct
    if((gdate-tdate).days>=0):
        print("Your next g-Day is on",gdate," (",i,"euler-gamma)")
        break
for i in range(100):
    ndate=bdate+dt.timedelta(days=days*i) #todo correct
    if((ndate-tdate).days>=0):
        print("Your next n-Day is on",ndate," (",i,"y)")
        break
