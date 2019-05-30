
from urllib.request import*
from datetime import*


# function to get weather response

def weather_response(location, API_key):
	url = 'http://api.openweathermap.org/data/2.5/forecast?q='+location+'&APPID='+API_key
	resp = urlopen(url)
	resp_data = str(resp.read())
	return resp_data 

json= weather_response("India","1b51de2b8b1a00efe9e9d1c5cdd5c759") 

# function to check for valid response

def has_error(location,json):
	
	
	if(json.find(location)==-1):
		return True
	


# function to get attributes on nth day


def get_temperature(json, n=0,t="03:00:00"):   #Code to fetch temperature value.
	json = str(json)
	b= date.today()
	c= str(b + timedelta(days=n))
	d=c + " " + t
	z=json.find(d)

	l=json.rfind('"temp"',0,z)
	i=json.find(',',l,z)
	k=json[l+7:i]
	return float(k)
			
		
def get_humidity(json, n=0,t="03:00:00"):      #Code to fetch humidity value. 
	
	json = str(json)
	#if (a>=0 and a<=4):
				

	b= date.today()
	c= str(b + timedelta(days=n))
	d=c + " " + t
	z=json.find(d)

	l=json.rfind('"humidity"',0,z)
	i=json.find(',',l,z)
	k=json[l+11:i]
	return float(k)
			
def get_pressure(json, n=0,t="03:00:00"):       #Code to fetch pressure value.
	json=str(json)
	b= date.today()
	c= str(b + timedelta(days=n))
	d=c + " " + t
	l = str(d)
	z=json.find(l)

	l=json.rfind('"pressure"',0,z)
	i=json.find(',',l,z)
	k=json[l+11:i]
	return float(k)

def get_wind(json, n=0,t="03:00:00"):           #Code to fetch wind value.
	
	
	#if (a>=0 and a<=4):
	json = str(json)	

	b= date.today()
	c=  str(b + timedelta(days=n))

	d=c + " " + t

	l = str(d)

	z=json.find(l)



	l=json.rfind('"wind"',0,z)
	i=json.find(',',l,z)
	k=json[l+16:i]
	return float(k)
			
def get_sealevel(json, n=0,t="03:00:00"):        #Code to fetch sealevel value.
	
	
	#if (a>=0 and a<=4):
				
	json = str(json)
	b= date.today()
	c=  str(b + timedelta(days=n))
	d=c + " " + t

	l = str(d)

	z=json.find(l)

	l=json.rfind('"sea_level"',0,z)
	i=json.find(',',l,z)
	k=json[l+12:i]
	return float(k)


