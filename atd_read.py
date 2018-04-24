# Simple demo of reading each analog input from the ADS1x15 and printing it to
# the screen.
# Author: Tomer Aharoni
# Project Venom -The Creative Machines Lab
import time
# Import the ADS1x15 module.
import Adafruit_ADS1x15
# Create an ADS1115 ADC (16-bit) instance.
# Change the I2C address to (0x48), on the I2C on bus 1
adc = Adafruit_ADS1x15.ADS1115(address=0x48, busnum=1)

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
GAIN = 1

print('Reading ADS1x15 values, press Ctrl-C to quit...')
# Print nice channel column headers.
print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*range(4)))
print('-' * 37)

#Average sensor readings 
def readSensor(int port):
    #initial val to average sensor readings 
    averaging = 0
    #get sampling of 5 readings per sensor
    for i in range(5):
        #read sensor raw value
        distance = adc.read_adc(port, gain=GAIN)
        #average reading
        averaging = averaging + distance
        #wait 5ms between readings
        #According to datasheet time between each read
        #is-38ms +/- 10ms. Waiting 55 ms assures each
        #read is from a different sample
        time.sleep(0.55)
    distance = averaging / 5
    return(distance)   

#Takes raw reading val in volts and call the appropriate function
#to convert it to distance in cm
def convert_to_cm(sensor_number, reading_value):
    if sensor_number is 1:
        return ir1(reading_value)
    elif sensor_number is 2:
        return ir2(reading_value)
    elif sensor_number is 3:
        return ir3(reading_value)
    else
        return 0 
           
# Main loop.
while True:
    # Read all the ADC channel values in a list.
    raw_values = [0]*4
    dist_values = [0]*4
    for i in range(4):
        # Read the specified ADC channel using the previously set gain value.
        raw_values[i] = readSensor(i)
        #dist_values[i] = convert_to_cm(readSensor(i))
        #values[i] = adc.read_adc(i, gain=GAIN)
        # Note you can also pass in an optional data_rate parameter that controls
        # the ADC conversion time (in samples/second). Each chip has a different
        # set of allowed data rate values, see datasheet Table 9 config register
        # DR bit values.
        #values[i] = adc.read_adc(i, gain=GAIN, data_rate=128)
        # Each value will be a 16 bit signed integer value on the ADS1115 DtA
    # Print the ADC values.
    print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*raw_values))
    # Pause for half a second.
    time.sleep(0.5)

###############################
#distance functions:
#take a raw reading and returns a distance
###############################
def ir1(raw_value):
    dist = #TODO: put function for IR1 here

def ir2(raw_value):
    dist = #TODO: put function for IR2 here

def ir3(raw_value):
    dist = #TODO: put function for IR3 here