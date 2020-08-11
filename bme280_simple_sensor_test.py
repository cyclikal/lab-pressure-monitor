from __future__ import print_function
import qwiic_bme280
import time
import sys


def runExample():

    print("\nSparkFun BME280 Sensor  Example 1\n")
    mySensor = qwiic_bme280.QwiicBme280()

    if mySensor.connected == False:
        print("The Qwiic BME280 device isn't connected to the system. Please check your connection",
              file=sys.stderr)
        return

    mySensor.begin()

    # Fancy setup, see SparkFun BME280 documentation for more info
    # setup the sensor
    mySensor.filter = 1         # 0 to 4 is valid. Filter coefficient. See 3.4.4
    # 0 to 7 valid. Time between readings. See table 27.
    mySensor.standby_time = 0

    # 0 to 16 are valid. 0 disables temp sensing. See table 24.
    mySensor.over_sample = 1
    # 0 to 16 are valid. 0 disables pressure sensing. See table 23.
    mySensor.pressure_oversample = 1
    # 0 to 16 are valid. 0 disables humidity sensing. See table 19.
    mySensor.humidity_oversample = 1
    # MODE_SLEEP, MODE_FORCED, MODE_NORMAL is valid. See 3.3
    mySensor.mode = mySensor.MODE_NORMAL


    while True:
        print("Humidity:\t%.3f" % mySensor.humidity)

        print("Pressure:\t%.3f" % mySensor.pressure)

        print("Altitude:\t%.3f" % mySensor.altitude_feet)

        print("Temperature:\t%.2f" % mySensor.temperature_fahrenheit)

        print("")

        time.sleep(1)


if __name__ == '__main__':
    try:
        runExample()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Example 1")
sys.exit(0)
