import signal
import sys
import time
import sensor_data
import gspread


def signal_handler(sig, frame):
    data_sheet.update('A2', data_sheet.get(
        'A2'), value_input_option="USER_ENTERED")
    data_sheet.update('B2', data_sheet.get(
        'B2'), value_input_option="USER_ENTERED")
    print('Exiting script...')
    sys.exit(0)


# IMPORTANT: the Pi service account MUST have edit access to the spreadsheet.
# This can be done like a normal user, by sharing it with the email found in service_account.json
SPREADSHEET_NAME = "Lab Monitor Data"  # Name of the spreadsheet for data to be uploaded
SPREADSHEET_TAB = "Raw Data"  # Name of the tab for data to be dumped in
LOOP_FREQUENCY = 30  # Seconds between each upload

start_time = time.time()
signal.signal(signal.SIGINT, signal_handler)
gc = gspread.service_account(filename='service_account.json')  # Held locally, should not be shared
data_sheet = gc.open(SPREADSHEET_NAME).worksheet(SPREADSHEET_TAB)

sensor_data.connect()

while True:
    try:
        data_sheet.insert_row(sensor_data.get_data(), 2, value_input_option="USER_ENTERED")
    except:
        print("Sensor error! Likely not connected, either electrically or i2c.")
    else:
        data_sheet.update('A2', data_sheet.get(
            'A2'), value_input_option="USER_ENTERED")
        data_sheet.update('B2', data_sheet.get(
            'B2'), value_input_option="USER_ENTERED")
        print(time.time() - start_time)
        start_time = time.time()

        time.sleep(LOOP_FREQUENCY - time.time() % LOOP_FREQUENCY)
