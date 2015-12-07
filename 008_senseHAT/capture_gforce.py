#setup the sense HAT
from time import sleep
from sense_hat import SenseHat
hat = SenseHat()

file = open('csv_gforce.csv', 'w')
file.write("time, x, y, z\n")
time = 0.0

print("running!")
try:
        while True:
                #get acceleration data in G's
                acceleration = hat.get_accelerometer_raw()
                #values to 3.d.p. strings
                x = str(round(acceleration['x'], 3))
                y = str(round(acceleration['y'], 3))
                z= str(round(acceleration['z'], 3))

                #write to CSV
                file.write(str(round(time, 1))+", "+x+", "+y+", "+z+"\n")

                #increase time
                time = time + 0.1
                sleep(0.1)
except KeyboardInterrupt:
        file.close()

