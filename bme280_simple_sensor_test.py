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
    '''# setup the sensor
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
    mySensor.mode = mySensor.MODE_NORMAL'''

    # Calibration stuff from the BME280 memory map
    '''print("ID(0xD0): 0x%.2x" % mySensor._i2c.readByte(
        mySensor.address, mySensor.BME280_CHIP_ID_REG))
    print("Reset register(0xE0): 0x%.2x" %
          mySensor._i2c.readByte(mySensor.address, mySensor.BME280_RST_REG))
    print("ctrl_meas(0xF4): 0x%.2x" % mySensor._i2c.readByte(
        mySensor.address, mySensor.BME280_CTRL_MEAS_REG))
    print("ctrl_hum(0xF2): 0x%.2x\n" % mySensor._i2c.readByte(
        mySensor.address, mySensor.BME280_CTRL_HUMIDITY_REG))

    print("Displaying all regs:")
    memCounter = 0x80
    for row in range(8, 16):
        print("0x%.2x 0:" % row, end='')
        for column in range(0, 16):
            tempReadData = mySensor._i2c.readByte(mySensor.address, memCounter)
            print("0x%.2x " % tempReadData, end='')

            memCounter += 1
        print("")

    print("Displaying concatenated calibration words:")
    print("dig_T1, uint16: %d" % mySensor.calibration["dig_T1"])
    print("dig_T2, int16: %d" % mySensor.calibration["dig_T2"])
    print("dig_T3, int16: %d" % mySensor.calibration["dig_T3"])
    print("dig_P1, uint16: %d" % mySensor.calibration["dig_P1"])
    print("dig_P2, int16: %d" % mySensor.calibration["dig_P2"])
    print("dig_P3, int16: %d" % mySensor.calibration["dig_P3"])
    print("dig_P4, int16: %d" % mySensor.calibration["dig_P4"])
    print("dig_P5, int16: %d" % mySensor.calibration["dig_P5"])
    print("dig_P6, int16: %d" % mySensor.calibration["dig_P6"])
    print("dig_P7, int16: %d" % mySensor.calibration["dig_P7"])
    print("dig_P8, int16: %d" % mySensor.calibration["dig_P8"])
    print("dig_P9, int16: %d" % mySensor.calibration["dig_P9"])
    print("dig_H1, uint8: %d" % mySensor.calibration["dig_H1"])
    print("dig_H2, int16: %d" % mySensor.calibration["dig_H2"])
    print("dig_H3, uint8: %d" % mySensor.calibration["dig_H3"])
    print("dig_H4, int16: %d" % mySensor.calibration["dig_H5"])
    print("dig_H6, int8: %d" % mySensor.calibration["dig_H6"])'''

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
