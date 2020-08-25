from __future__ import print_function
import qwiic_bme280
import Adafruit_DHT
import time
import sys
import random
import logging

DHT_PIN = 27  # MAKE SURE THIS IS CORRECT

class Sensor_Pack:
	def __init__(self, dht_pin):
		self.DHT_PIN = dht_pin
		self.dht22 = Adafruit_DHT.DHT22

		self.bme280 = qwiic_bme280.QwiicBme280()
		self.bme280.set_pressure_oversample(1)
		self.bme280.set_tempature_oversample(1)
		self.bme280.set_humidity_oversample(1)
		self.bme280.begin()

	def get_data(self):
		logging.info("----- DATA START -----")

		if not self.bme280.connected:
			raise Exception("BME280 not connected!")

		dht22_start = time.time()

		# DHT22 Readings ---------------------------------------------------------
		lab_hum = -1.0
		lab_temp_c = -1.0

		# Glitchy timing-sometimes it won't get data, in which case we'll try again
		while lab_hum == -1.0 and lab_temp_c == -1.0:
			lab_hum, lab_temp_c = Adafruit_DHT.read_retry(self.dht22, DHT_PIN)
		lab_temp_f = (lab_temp_c * 9/5) + 32

		logging.debug("DHT22 (lab sensor): {:.3f} sec".format(time.time() - dht22_start))
		bme280_start = time.time()

		# BME280 Readings --------------------------------------------------------
		gb_temp_c = self.bme280.get_temperature_celsius()  # In C
		gb_temp_f = (gb_temp_c * 9/5) + 32  # In F

		gb_hum = self.bme280.read_humidity()  # In %

		gb_pressure_hpa = self.bme280.read_pressure() / 100.0  # In hPa
		gb_presssure_h2o = (gb_pressure_hpa - 1013.25) / 2.488  # In inches water

		logging.debug("BME280 (glove box sensor): {:.3f} sec".format(time.time() - bme280_start))

		logging.info("----- DATA END ({:.2f} sec) -----".format(time.time() - dht22_start))
		return ['=TEXT(NOW(),"yyyy/mm/dd")', '=TEXT(NOW(),"hh:mm:ss")', lab_temp_c, lab_temp_f, lab_hum, gb_temp_c, gb_temp_f, gb_hum, gb_pressure_hpa, gb_presssure_h2o]


#sensors = Sensor_Pack(DHT_PIN)

#while True:
#	data = sensors.get_data()
#	print(data)
#	time.sleep(3)

