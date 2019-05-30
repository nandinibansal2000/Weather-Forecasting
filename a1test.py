import unittest
from a1 import weather_response
from a1 import has_error
from a1 import get_temperature 
from a1 import get_humidity
from a1 import get_pressure
from a1 import get_wind
from a1 import get_sealevel

# TEST cases should cover the different boundary cases.




class testpoint(unittest.TestCase):
	
			
	def test_has_error(self):
		self.assertFalse(has_error("Delhi",(weather_response("Delhi","1b51de2b8b1a00efe9e9d1c5cdd5c759"))))
		self.assertFalse(has_error("Mumbai",(weather_response("Mumbai","1b51de2b8b1a00efe9e9d1c5cdd5c759"))))
		self.assertFalse(has_error("Ludhiana",(weather_response("Ludhiana","1b51de2b8b1a00efe9e9d1c5cdd5c759"))))
		self.assertFalse(has_error("Australia",(weather_response("Australia","1b51de2b8b1a00efe9e9d1c5cdd5c759"))))
		self.assertFalse(has_error("India",(weather_response("India","1b51de2b8b1a00efe9e9d1c5cdd5c759"))))


	def test_get_temperature(self):
		self.assertAlmostEqual((get_temperature(weather_response("Delhi","1b51de2b8b1a00efe9e9d1c5cdd5c759"),4,"03:00:00")),304.867,delta=20)
		self.assertAlmostEqual((get_temperature(weather_response("Mumbai","1b51de2b8b1a00efe9e9d1c5cdd5c759"),2,"12:00:00")),299.145,delta=55)
		self.assertAlmostEqual((get_temperature(weather_response("Ludhiana","1b51de2b8b1a00efe9e9d1c5cdd5c759"),1,"06:00:00")),298.929,delta=55)
		self.assertAlmostEqual((get_temperature(weather_response("Australia","1b51de2b8b1a00efe9e9d1c5cdd5c759"),3,"09:00:00")),300.605,delta=55)
		self.assertAlmostEqual((get_temperature(weather_response("India","1b51de2b8b1a00efe9e9d1c5cdd5c759"),0,"21:00:00")),295.46,delta=55)
							  
								  
								  
	def test_get_humidity(self):
		self.assertAlmostEqual((get_humidity(weather_response("Delhi","1b51de2b8b1a00efe9e9d1c5cdd5c759"),4,"03:00:00")),66,delta=20)
		self.assertAlmostEqual((get_humidity(weather_response("Mumbai","1b51de2b8b1a00efe9e9d1c5cdd5c759"),2,"12:00:00")),99,delta=55)
		self.assertAlmostEqual((get_humidity(weather_response("Ludhiana","1b51de2b8b1a00efe9e9d1c5cdd5c759"),1,"06:00:00")),88,delta=55)
		self.assertAlmostEqual((get_humidity(weather_response("Australia","1b51de2b8b1a00efe9e9d1c5cdd5c759"),3,"09:00:00")),77,delta=55)
		self.assertAlmostEqual((get_humidity(weather_response("India","1b51de2b8b1a00efe9e9d1c5cdd5c759"),0,"21:00:00")),98,delta=55)
										   
											   
											   
	def test_get_pressure(self):
		self.assertAlmostEqual((get_pressure(weather_response("Delhi","1b51de2b8b1a00efe9e9d1c5cdd5c759"),4,"03:00:00")),1005.75,delta=20)
		self.assertAlmostEqual((get_pressure(weather_response("Mumbai","1b51de2b8b1a00efe9e9d1c5cdd5c759"),2,"12:00:00")),1022.39,delta=55)
		self.assertAlmostEqual((get_pressure(weather_response("Ludhiana","1b51de2b8b1a00efe9e9d1c5cdd5c759"),1,"06:00:00")),990.27,delta=55)					   
		self.assertAlmostEqual((get_pressure(weather_response("Australia","1b51de2b8b1a00efe9e9d1c5cdd5c759"),3,"09:00:00")),1023.76,delta=55)						   
		self.assertAlmostEqual((get_pressure(weather_response("India","1b51de2b8b1a00efe9e9d1c5cdd5c759"),0,"21:00:00")),1010.2,delta=55)			   
							   
										   
							   
	def test_get_wind(self):
		self.assertAlmostEqual((get_wind(weather_response("Delhi","1b51de2b8b1a00efe9e9d1c5cdd5c759"),4,"03:00:00")),1.31,delta=5)
		self.assertAlmostEqual((get_wind(weather_response("Mumbai","1b51de2b8b1a00efe9e9d1c5cdd5c759"),2,"12:00:00")),3.57,delta=5)						   
		self.assertAlmostEqual((get_wind(weather_response("Ludhiana","1b51de2b8b1a00efe9e9d1c5cdd5c759"),1,"06:00:00")),1.35,delta=5)							   
		self.assertAlmostEqual((get_wind(weather_response("Australia","1b51de2b8b1a00efe9e9d1c5cdd5c759"),3,"09:00:00")),2.9,delta=5)					   
		self.assertAlmostEqual((get_wind(weather_response("India","1b51de2b8b1a00efe9e9d1c5cdd5c759"),0,"21:00:00")),2.36,delta=5)						   
							   
							   
							   
							   
							   

	def test_get_sealevel(self):
		self.assertAlmostEqual((get_sealevel(weather_response("Delhi","1b51de2b8b1a00efe9e9d1c5cdd5c759"),4,"03:00:00")),1030.97,delta=20)
		self.assertAlmostEqual((get_sealevel(weather_response("Mumbai","1b51de2b8b1a00efe9e9d1c5cdd5c759"),2,"12:00:00")),1023.17,delta=55)					   
		self.assertAlmostEqual((get_sealevel(weather_response("Ludhiana","1b51de2b8b1a00efe9e9d1c5cdd5c759"),1,"06:00:00")),1016.55,delta=55)						   
		self.assertAlmostEqual((get_sealevel(weather_response("Australia","1b51de2b8b1a00efe9e9d1c5cdd5c759"),3,"09:00:00")),1027.47,delta=55)				   
		self.assertAlmostEqual((get_sealevel(weather_response("India","1b51de2b8b1a00efe9e9d1c5cdd5c759"),0,"21:00:00")),1026.35,delta=55)				   
							   
							   
							   
							   
							   
							   
							   
	
if __name__=='__main__':
	unittest.main()
