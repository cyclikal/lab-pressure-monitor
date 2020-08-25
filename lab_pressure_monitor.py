import signal
import logging
import sys
import time
from sensor_data import Sensor_Pack
import gspread


def signal_handler(sig, frame):
	data_sheet.update('A2', data_sheet.get('A2'), value_input_option="USER_ENTERED")
	data_sheet.update('B2', data_sheet.get('B2'), value_input_option="USER_ENTERED")
	print('Exiting script...')
	sys.exit(0)


# IMPORTANT: the Pi service account MUST have edit access to the spreadsheet.
# This can be done like a normal user, by sharing it with the email found in service_account.json
SPREADSHEET_NAME = "Lab Monitor Data"  # Name of the spreadsheet for data to be uploaded
SPREADSHEET_TAB = "Raw Data"  # Name of the tab for data to be dumped in
LOOP_FREQUENCY = 60  # Seconds between each upload
DHT_PIN = 27  # The lone pin (green heatshrink) for the DHT22 sensor

logging.basicConfig(filename='pressure_monitor_log.log',format='%(asctime)s %(levelname)-8s %(message)s',level=logging.INFO,datefmt='%Y-%m-%d %H:%M:%S')
logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
logging.info('Intitializing...')

start_time = time.time()
signal.signal(signal.SIGINT, signal_handler)
gc = gspread.service_account(filename='service_account.json')  # Held locally, should not be shared
data_sheet = gc.open(SPREADSHEET_NAME).worksheet(SPREADSHEET_TAB)

sensors = Sensor_Pack(DHT_PIN)

while True:
	try:
		logging.info("---------- LOOP START ----------")
		data_sheet.insert_row(sensors.get_data(), 2, value_input_option="USER_ENTERED")
	except OSError as i2c_error:
		logging.error("\n\n\n")
		logging.error("OSError:")
		logging.error(i2c_error.args)
		logging.error("\n\n\n")
	except Exception as a_problem:
		logging.error("\n\n\n")
		logging.error("Exception:" + a_problem.args[0])
		logging.error("\n\n\n")
		if a_problem.args[0] == "BME280 not connected!":
			logging.error("SCRIPT ENDED DUE TO I2C CONNECTION ERROR")
			sys.exit(0)
	else:
		# Make timestamps static (the "NOW()" function in Google Sheets updates at each reload otherwise)
		# Note that these are called in the exit handler too, so a script that is user-terminated will 
		# update the data before exiting.
		data_sheet.update('A2', data_sheet.get('A2'), value_input_option="USER_ENTERED")
		data_sheet.update('B2', data_sheet.get('B2'), value_input_option="USER_ENTERED")

		logging.info("---------- LOOP END ({:.2f} sec) ----------\n\n".format(time.time() - start_time))
		start_time = time.time()
		time.sleep(LOOP_FREQUENCY - time.time() % LOOP_FREQUENCY)
