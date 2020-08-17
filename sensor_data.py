from __future__ import print_function
import qwiic_bme280
import Adafruit_DHT as dht
import time
import sys
import random

DHT_PIN = 4  # MAKE SURE THIS IS CORRECT


def connect():
    '''
    Connects to the BME280 module over the default i2c address (0x77)
    '''
    
    # TODO: uncomment once testing/running on the pi
    '''
    sensor = qwiic_bme280.QwiicBme280()
    sensor.set_pressure_oversample(4)
    sensor.set_tempature_oversample(2)  # Yes it's misspelled, the library has an error lol
    sensor.set_humidity_oversample(4)
    return sensor.begin()
    '''
    print("Connected to sensor")


def get_data():
    '''
    Gathers data from the BME280 sensor and the DHT22 and reports them in the spreadsheet format (a list with date, time, and some Google Sheets formulas)
    '''

    # TODO: uncomment once testing/running on the pi
    ''' 
    sensor.set_mode(MODE_NORMAL)

    if not sensor.connected:
        raise Exception

    lab_hum, lab_temp_c = dht.read_retry(dht.DHT22, DHT_PIN)
    lab_temp_f = (lab_temp_c * 9/5) + 32

    gb_temp_c = sensor.get_temperature_celsius() / 100.0  # In C
    gb_temp_f = (gb_temp_c * 9/5) + 32  # In F

    gb_hum = sensor.read_humidity() / 1024.0  # In %

    gb_pressure_hpa = sensor.read_pressure() / 25600.0  # In hPa
    gb_presssure_h2o = (pressure - 1013.25) / 2.488  # In inches water

    time.sleep(0.1)
    sensor.set_mode(MODE_SLEEP)
    '''

    # TODO: comment/delete the code below once testing/running on the pi
    lab_temp_c = random.uniform(20.0, 24.0)
    lab_temp_f = (lab_temp_c * 9/5) + 32
    lab_hum = random.uniform(45.0, 55.0)
    gb_temp_c = random.uniform(20.0, 23.0)
    gb_temp_f = (gb_temp_c * 9/5) + 32
    gb_hum = random.uniform(25.0, 30.0)
    gb_pressure_hpa = random.uniform(1013.25, 1025.0)
    gb_presssure_h2o = (pressure - 1013.25) / 2.488

    return ['=TEXT(NOW(),"yyyy/mm/dd")', '=TEXT(NOW(),"hh:mm:ss")', lab_temp_c, lab_temp_f, lab_hum, gb_temp_c, gb_temp_f, gb_hum, gb_pressure_hpa, gb_presssure_h2o]
