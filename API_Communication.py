#Aim of this program is getting data from ISS endpoint and also
#Getting data from anothet endpoint to find the sunrise and sunset time
#Compare them and try to see the ISS on sky

import requests
import datetime as dt
#Constants
NL_MIDDELBURG_POS = (51.498795,3.610998 ) # put in the coordinates of the city you live in.
ISS_API = "http://api.open-notify.org/iss-now.json"
SUNSET_RISE_API = " https://api.sunrise-sunset.org/json"

#----------------------------------------------------------------
#Get ISS Position
iss_req = requests.get(ISS_API)
iss_data = iss_req.json()['iss_position']
iss_lat = float(iss_data["latitude"])
iss_long = float(iss_data["longitude"])
iss_pos = (iss_lat, iss_long)

#------------------------------------------------------------------------
#GET Current Sunset and Rise
#To get the your positions data and time in 24 format add parameters
# sample api 
#https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400&formatted=0

parameters = {
    "lat" : NL_MIDDELBURG_POS[0],
    "lng" : NL_MIDDELBURG_POS[1],
    "formatted" : 0
}


req = requests.get(SUNSET_RISE_API, params=parameters)
data = req.json()
sunrise = float(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = float(data["results"]["sunset"].split("T")[1].split(":")[0])

#--------------------------------------------------------------------------------------


#Get the Current hour 

now = float(dt.datetime.utcnow().hour)

def check_is_ISS_over_middelburg():
    
    is_over_you_check = (abs(iss_lat-NL_MIDDELBURG_POS[0])<=3 and abs(iss_long-NL_MIDDELBURG_POS[1]<=3))
    is_night_check = (sunset < now) and (now < sunrise) 
    
    
    if is_over_you_check:
      if is_night_check:
          print("Look Up, It is some Where up you right now")
      else:
          print("ISS is over you but Since it is daytime you can not see It!")
          print(iss_pos)
    else:
        print(f"Unfortunately ISS Position is {iss_pos}")

#-------------------------------------------------------------

#Lets try

check_is_ISS_over_middelburg()