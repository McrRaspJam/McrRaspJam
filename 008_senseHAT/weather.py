#setup the sense HAT
from sense_hat import SenseHat
hat = SenseHat()

#Say hello
print("Manchester Raspberry Jam weather station")
print()

#get the temperature
temperature = hat.get_temperature()
temperature = round(temperature, 1)
print("Temperature: "+str(temperature)+" Celsius")

#get the humidity
humidity = hat.get_humidity()
humidity = round(humidity, 1)
print("Humidity: "+str(humidity)+"%")

#get the atmoshpheric pressure
hat.get_pressure()
pressure = hat.get_pressure()
pressure = round(pressure, 1)
print("Pressure: "+str(pressure)+" millibars")
