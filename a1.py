
from urllib.request import*
from datetime import*


# function to get weather response

def weather_response(location, API_key):
	url = 'http://api.openweathermap.org/data/2.5/forecast?q='+location+'&APPID='+API_key
	resp = urlopen(url)
	resp_data = str(resp.read())
	return resp_data 


# function to check for valid response

def has_error(location,json):
	
	
	if(json.find(location)==-1):
		return True
	


# function to get attributes on nth day

"""Code to fetch temperature value."""
def get_temperature(json, n=0,t="03:00:00"):   
	json = str(json)
	b= date.today()
	c= str(b + timedelta(days=n))
	d=c + " " + t
	z=json.find(d)

	l=json.rfind('"temp"',0,z)#to find index of "temp" corresponding to date and time that we give input from index 0 to index of d(i.e. index of date and time)
	i=json.find(',',l,z)# to find "," from index of "temp" to index of d
	k=json[l+7:i]
	return float(k)
			
"""Code to fetch humidity value."""		
def get_humidity(json, n=0,t="03:00:00"):
	
	json = str(json)
	#if (a>=0 and a<=4):
				

	b= date.today()
	c= str(b + timedelta(days=n))
	d=c + " " + t
	z=json.find(d)

	l=json.rfind('"humidity"',0,z)#to find index of "humidity" corresponding to date and time that we give input from index 0 to index of d(i.e. index of date and time)
	i=json.find(',',l,z)# to find "," from index of "humidity" to index of d
	k=json[l+11:i]
	return float(k)

"""Code to fetch pressure value."""			
def get_pressure(json, n=0,t="03:00:00"):       
	json=str(json)
	b= date.today()
	c= str(b + timedelta(days=n))
	d=c + " " + t
	l = str(d)
	z=json.find(l)

	l=json.rfind('"pressure"',0,z)#to find index of "pressure" corresponding to date and time that we give input from index 0 to index of d(i.e. index of date and time)
	i=json.find(',',l,z)# to find "," from index of "pressure" to index of d
	k=json[l+11:i]
	return float(k)

"""Code to fetch wind value."""
def get_wind(json, n=0,t="03:00:00"):           
	
	
	#if (a>=0 and a<=4):
	json = str(json)	

	b= date.today()
	c=  str(b + timedelta(days=n))

	d=c + " " + t

	l = str(d)

	z=json.find(l)



	l=json.rfind('"wind"',0,z)#to find index of "wind" corresponding to date and time that we give input from index 0 to index of d(i.e. index of date and time)
	i=json.find(',',l,z)# to find "," from index of "wind" to index of d
	k=json[l+16:i]
	return float(k)
"""Code to fetch sealevel value."""
def get_sealevel(json, n=0,t="03:00:00"):
	
	
	#if (a>=0 and a<=4):
				
	json = str(json)
	b= date.today()
	c=  str(b + timedelta(days=n))
	d=c + " " + t

	l = str(d)

	z=json.find(l)

	l=json.rfind('"sea_level"',0,z)#to find index of "sea_level" corresponding to date and time that we give input from index 0 to index of d(i.e. index of date and time)
	i=json.find(',',l,z)# to find "," from index of "sea_level" to index of d
	k=json[l+12:i]
	return float(k)


